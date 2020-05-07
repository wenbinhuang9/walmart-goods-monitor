
import requests

headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        #'Host':'https://www.google.com/',
        'Connection':'keep-alive',
        'Accept':'application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5',
        'Referer':'https://www.google.com/',
        'Accept-Encoding':'gzip,deflate,sdch,gbk',
        'Accept-Language':'en-US,en;q=0.8'
    }
def getText(url):
   return getTextByHeaders(url, headers)

def getTextByHeaders(url, headers):
    session = requests.session()


    response = session.get(url, headers=headers )
    print( response)
    if (response.status_code != 200) :
        raise ValueError("exception in when loading page")

    response.encoding= "UTF-8"
    return response.text