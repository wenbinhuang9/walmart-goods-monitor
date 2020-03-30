


url = "https://www.amazon.com/dp/B07NFSZ9XN/?coliid=I25A82OVR77NYD&colid=1TO7CM1VPLTOZ&psc=0"

import requests
import time

from message import  sendMail

def check_item_stock(url):
    session = requests.session()
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
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