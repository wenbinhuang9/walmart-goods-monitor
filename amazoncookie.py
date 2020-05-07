import requests
import time

from message import  sendMail


url  ="https://www.amazon.com/"

def check_item_stock(url):
    session = requests.session()
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        #'Host':'https://www.google.com/',
        'Connection':'keep-alive',
        'Accept':'application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5',
        'Referer':'https://www.google.com/',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'en-US,en;q=0.8',
        'Cookie':'at-main=Atza|IwEBIND3orqu1W1zsWvj2xi3ZkHWRucstWYgQSHoX9ZgD8psWqa_uLb848_yzkIniQAN-QEEbu5ISmwsUudsQ63TXXBuHbquxtwKTB948ZGv4NdaK3Jhbj2Eqcx1nW5kep7dlEoct7S844Ac-W6X-gz-SdGmv37tuwIoqH9mUjEBBG4rsdHsKJpeU19v2WeBzhztNbImmOXvt7paoc99G2Xl_ujXFThSiCNWECZ2PSXmtLy6fASLMQFvNsyZUnRGUxxyehMlhVwD9EwFUzS3ZQRrDujmQXE6FEOfoxKSIoOACdY2bYFzhgQ1zbI6WHR-HOwOEILyIVWcJGhr6jMiVSNdU6D-x9Bjvw1c_qeZ4csTgix9JmJl046dtDse46ccIPxreotXRNf-av_yMzuDtaeKRsoB'
    }
    response = session.get(url, headers=h )
    print(session.cookies)
    print(response)
    print(response.text)

    print(session.cookies)


check_item_stock(url)