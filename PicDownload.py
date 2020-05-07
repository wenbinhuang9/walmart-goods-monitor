from uuid import uuid4
##
from  webutil import getText, getTextByHeaders
import ssl
import re
import urllib.request

import  os
ssl._create_default_https_context = ssl._create_unverified_context

headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Host':'c1.2tyl.icu',
        'Connection':'keep-alive',
        'Accept':'application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5',
        'Referer':'https://cl.330f.tk/htm_data/2004/16/3885758.html',
        'Accept-Encoding':'gzip,deflate,sdch,gbk',
        'Accept-Language':'en-US,en;q=0.8'
    }

## https://ci.2tyl.icu/htm_data/2003/16/3857453.html

def about_pic(source, filename = ""):
    p = re.compile(r'http.*?.jpg')
    pic_url = re.findall(p, source)

    print(pic_url)
    for i in pic_url:
        if i.find("ess-data=") > 0:
            i_split = i.split("' ess-data='")
            i = i_split[0]
            print("i={0}".format(i))
        if i.find("data-src=") > 0 :
            i_split = i.split("data-src='")
            i = i_split[1]
            print("i={0}".format(i))

        try:
            downloadPicUlr(i, filename = filename)
        except Exception as e:
            print(e)
            print(i)

def downloadPicUlr(picUrl, filename= "" , format = "jpg"):
    if picUrl.find("ad") > 0 :
        print(picUrl)
        return
    if os.path.exists(filename) == False:
        os.mkdir(filename)

    opener = urllib.request.build_opener()
    opener.addheaders = [(k, v) for k, v in headers.items()]
    urllib.request.install_opener(opener)

    try:
        img_name = str(uuid4())
        print(img_name)
        path =  filename +  img_name + "." + format

        urllib.request.urlretrieve(picUrl, path)

    except Exception as e:
        print(e)

#url = "https://ci.2tyl.icu/htm_data/2003/7/3846210.html"

#url = "http://seopic.699pic.com/photo/40011/0709.jpg_wh1200.jpg"
# url ="https://www.louimg.com/i/?i=u/20200328/18531045.jpg"
# downloadPicUlr(url, format="jpg" , filename="./")

url = "https://cc.2tyl.icu/htm_data/2004/7/3897848.html"
content =getTextByHeaders(url, headers)

file = "/Users/ben/Downloads/movie_korea/favor_pic/zhenshi99/"
about_pic(content, filename = file)