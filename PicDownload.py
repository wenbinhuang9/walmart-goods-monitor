from uuid import uuid4
##
from  webutil import getText, getTextByHeaders
import ssl
import re
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Host':'ci.2tyl.icu',
        'Connection':'keep-alive',
        'Accept':'application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5',
        'Referer':'https://ci.2tyl.icu/htm_data/2003/16/3857453.html',
        'Accept-Encoding':'gzip,deflate,sdch,gbk',
        'Accept-Language':'en-US,en;q=0.8'
    }

## https://ci.2tyl.icu/htm_data/2003/16/3857453.html

def about_pic(source):
    p = re.compile(r'http.*?.jpg')
    pic_url = re.findall(p, source)

    print(pic_url)
    for i in pic_url:
        try:
            downloadPicUlr(i, "")
        except Exception as e:
            print(e)
            print(i)

def downloadPicUlr(picUrl, format):
    opener = urllib.request.build_opener()
    opener.addheaders = [(k, v) for k, v in headers.items()]
    urllib.request.install_opener(opener)

    try:

        img_name = str(uuid4())
        print(img_name)
        path = img_name + ".jpg"

        urllib.request.urlretrieve(picUrl, path)

    except Exception as e:
        print(e)

#url = "https://ci.2tyl.icu/htm_data/2003/7/3846210.html"

#url = "http://seopic.699pic.com/photo/40011/0709.jpg_wh1200.jpg"
#url ="https://www.privacypic.com/images/2020/03/21/1be5416145891be45.jpg"
#downloadPicUlr(url, "jpg")

url = "https://ci.2tyl.icu/htm_data/2003/16/3857453.html"
content =getTextByHeaders(url, headers)
about_pic(content)