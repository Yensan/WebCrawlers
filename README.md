# setup scrapy in Win10 Python 3.5
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
    pip install Scrapy-1.2.1-py2.py3-none-any.whl