
# setup scrapy in Win10 Python 3.5
###### all of packages are ziped in 'Win10X64  Python3.5 packages.rar',download and enjoy!
1.upgrade PIP    
  
    download new version of PIP sourcefiles.Or download in this project folder.Unzip it
    run CMD.exe, and enter pip source folder. Such as:
    C:\Windows\System32>d:    # change disk
    d:\>cd d:\Download\pip-9.0.1   # enter pip source folder
then, run setup.Py  

    python setup.py install
2.install Dependence packages  

    download all of packages, and then enter the folder. Run pip:  
    
        pip install lxml-3.6.4-cp35-cp35m-win_32.whl
        pip install Twisted-16.5.0-cp35-cp35m-win_amd64.whl
        pip install requests-2.12.1-py2.py3-none-any.whl
        pip install pypiwin32-219-cp35-none-win_amd64.whl
        pip install Pillow-3.4.2-cp35-cp35m-win_amd64.whl
        pip install cryptography-1.6-cp35-cp35m-win_amd64.whl
3.install scrapy 

    # pip install Scrapy-1.2.1-py2.py3-none-any.whl




#　文件说明 
### scrapy.cfg:
    # project：是项目目录，内含settings和spiders。
    # default：指明settings.py路径，project.settings 
### settings.py：
    # BOT_NAME:就是项目目录。spiders_modules：spider模块所在的目录。
    # ITEM_PIPELINES:  指明一个Pipe类的路径


# Pycharm，运行配置说明:
### 用main.py驱动运行
    #from scrapy import cmdline
    #cmdline.execute("scrapy crawl PhotoSpider".split())
   PhotoSpider是class的属性，name="PhotoSpider"，然后直接运行main.py
###   在Pycharm直接运行rosi（spider）
   //TODO

# 更改目标网站，配置说明: 
### 存储路径配置
更改存储路径，避免多个网站的数据混杂
    settings.py，更改IMAGES_STORE = '../../data/rosi/'，改成'../../data/XXX/'
### 网址配置
rosi.py ，更改目标网站   

     #allowed_domains = ['rosiok.com']       
     #start_urls = ['http://www.rosiok.com/',]
pipelines.py ，更改图片匹配URL   

     #            if 'rosiok.com' not in image_url:
                        continue