import requests
from lxml import etree
import json
import urllib.request
from tqdm import tqdm


if __name__ == '__main__':
    # UA伪装
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        # 防盗链子
        , "Referer": "https://www.bilibili.com/"
        ,
        "Cookie": "buvid3=4608D78B-F867-9D5F-5623-EA2D9073754400140infoc; b_nut=1717426502; buvid4=015C00B5-2E0A-94F5-B250-593E9371154800140-024060314-Nk4u6e80UEPHxtOn7PC/wA%3D%3D; rpdid=|(kJYuRJRm~0J'u~u~RkYmku; _uuid=6FE347C10-DD4D-71E9-71DD-84A3FBA5197158429infoc; buvid_fp=5cdaa505a6d71eac5b8c1748203dab93; SESSDATA=6a4aa385%2C1732979074%2C49911%2A61CjALY_L_mOQjoFv0ZYLOh2Um-1U0HO8tOZLnSDX6rfarJNDHUx4WEqJVY_3IunOeFukSVnctNDk5bFEwOXhsRURMcDA4OXhQRU5rNEdkOUtRODdTem9Ja3A4NEs3UElSb25IVjJadDY3dDRxRDdRUGkyd3NDVUphUG5UOS1qU0JFY2I4RGF3UEhnIIEC; bili_jct=154210ab80cf68180900175817abcdeb; DedeUserID=453353235; DedeUserID__ckMd5=49714595c203cd9e; sid=8j2v4hii; is-2022-channel=1; CURRENT_BLACKGAP=0; enable_web_push=DISABLE; header_theme_version=CLOSE; CURRENT_QUALITY=80; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjQzMTc4MjEsImlhdCI6MTcyNDA1ODU2MSwicGx0IjotMX0.2LJ7vHaBSWUDdrhNrNCXbiZZwdLi11cGKeTYj6ywkwg; bili_ticket_expires=1724317761; bp_t_offset_453353235=967370829996228608; bsource=search_baidu; home_feed_column=4; browser_resolution=1280-710; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; b_lsid=B7C18383_1916ADF2AE7"
    }

    # 1、指定url
    # url = "https://www.bilibili.com/video/BV17w4m1e7PT/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=2a6e427465a2f829272f5863986dfa80"
    url = "https://www.bilibili.com/video/BV1tJ411V72k/?p=26&vd_source=f230a650621ce31e8709b0bd5a3826fb"

    # 2、发送请求
    response = requests.get(url, headers=head)

    # 3、获取响应的数据
    res_text = response.text

    # 4、数据解析
    tree = etree.HTML(res_text)

    with open("bili2.html", "w", encoding="utf-8") as f:
        f.write(res_text)

    base_info = "".join(tree.xpath("/html/head/script[4]/text()"))[20:]
    info_dict = json.loads(base_info)

    video_url = info_dict["data"]["dash"]['video'][0]["baseUrl"]
    audio_url = info_dict["data"]["dash"]['audio'][0]["baseUrl"]

    video_content = requests.get(video_url, headers=head).content
    audio_content = requests.get(audio_url, headers=head).content

    with open("video.mp4", "wb") as f:
        f.write(video_content)
    with open("audio.mp4", "wb") as fp:
        fp.write(audio_content)

