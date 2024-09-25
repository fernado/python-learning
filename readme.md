国内源：
新版ubuntu要求使用https源，要注意。

```
清华：https://pypi.tuna.tsinghua.edu.cn/simple

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

华中理工大学：http://pypi.hustunique.com/

山东理工大学：http://pypi.sdutlinux.org/ 

豆瓣：http://pypi.douban.com/simple/
```

临时使用：
可以在使用pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple

```
例如：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider，这样就会从清华这边的镜像去安装pyspider库。
```


pycharm cmder setting

`Settings -> Tools -> Terminal -> Shell path`
```
"cmd.exe" /k ""%CMDER_HOME%\vendor\init.bat"" 
```


`pdf2png_fitz.py` only install
```
pip install PyMuPDF
```
and can change the dpi to adjust the resolution



but `pdf2png_wand.py` must
```
pip install Wand
```
and [Ghostscript](https://www.ghostscript.com/releases/index.html)

otherwise an exception would be thrown
```
wand.exceptions.DelegateError: FailedToExecuteCommand "gswin64c.exe" -q ...
```


