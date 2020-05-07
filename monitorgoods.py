import requests
import time

from message import  sendMail

def check_item_stock(url):
    session = requests.session()
    try:
        response = session.get(url)
        print(response)
        if (response.status_code != 200) :
            print("error occurs|response={0}|url={1}".format(response.text, url))
            return False
        if (response.text.find("Add to Cart") > 0 or response.text.find("Add to cart") > 0 or response.text.find("add to cart")> 0):
            return True
        return False
    finally:
        session.close()




def monitor(urls, mails):
    try:
        for url in urls:
            ans = check_item_stock(url)
            time.sleep(5)

            if (ans):
                print("have stock here;url={0}".format(url))
                sendMail(mails, "walmart goods coming, go!go!go!", url)

    except Exception as e:
        print("url={0}".format(url))
        print(e)


if __name__ == "__main__":

    url11 = "https://www.walmart.com/ip/2WG3Q2LA01RP?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=1e7f07c2-0928-409c-862e-b2b75be16172&registryId=undefined&selected=true"

    urls = [url11]

    ## fill email to send here

    emailtosend = ""
    while True:
        monitor(urls, emailtosend)

