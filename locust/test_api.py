from fastapi import FastAPI, Request, HTTPException
from starlette.responses import JSONResponse
from asyncio import Lock
from collections import defaultdict


app = FastAPI()
# 用于存储路操作访问次数的字典
access_counts = defaultdict(int)
lock = Lock()


# 中间件，用于统计路操作的次数
@app.middleware("http")
async def count_method_calls(request: Request, call_next):
    method = request.method
    path = request.url.path
    endpoint = f"{method}:{path}"

    async with lock:
        access_counts[endpoint] += 1
        current_count = access_counts[endpoint]

    if current_count % 9 == 0:
        raise HTTPException(status_code=429, detail=f"Access limit reached for {endpoint}, count: {current_count}")

    response = await call_next(request)
    response.headers["X-Method-Visit-Count"] = str(current_count)

    return response


@app.get("/hello")
async def hello():
    return JSONResponse({"message": "Hello World 1"})


@app.get("/world")
async def world():
    return JSONResponse({"message": "Hello World 2"})


@app.get("/access_counts")
async def method_call_count():
    return JSONResponse(access_counts)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)