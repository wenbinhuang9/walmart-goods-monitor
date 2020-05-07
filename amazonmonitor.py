



import requests
import time

from message import  sendMail

url = "https://www.amazon.com/Lysol-Handi-Pack-Disinfecting-4X80ct-Blossom/dp/B07CVB2WRT?ref_=ast_sto_dp"

def check_item_stock(url):
    session = requests.session()
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        #'Host':'https://www.google.com/',
        'Connection':'keep-alive',
        'Accept':'application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5',
        'Referer':'https://www.google.com/',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'en-US,en;q=0.8'
    }
    response = session.get(url, headers=h )
    print(response)
    print(response.text)
    if (response.status_code != 200) :
        raise ValueError("exception in when loading page")

    if (response.text.find("Currently unavailable") > 0):
        return False

    return True

print(check_item_stock(url))