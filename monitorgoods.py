import requests
import time

from message import  sendMail

def check_item_stock(url):
    session = requests.session()

    response = session.get(url)
    print(response)
    if (response.status_code != 200) :
        raise ValueError("exception in when loading page")

    if (response.text.find("Add to Cart") > 0):
        return True

    return False

def monitor(urls):
    for url in urls:
        ans = check_item_stock(url)
        time.sleep(30)
        try:
            if (ans):
                print("have stock here;url={0}".format(url))
                sendMail("yinjialiu003@gmail.com", "walmart goods coming, go!go!go!", url)

        except Exception as e:
            print("url={0}".format(url))
            print(e)


if __name__ == "__main__":
    url1 = "https://www.walmart.com/ip/3ZQ8YRFR0F4K?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=354fca58-9895-491a-adba-615d0f99b2cb&registryId=undefined&selected=true"
    url2 = "https://www.walmart.com/ip/1A4RHBN5T52K?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=f182ab01-7a54-42e8-8d51-f8f10b694dd0&registryId=undefined&selected=true"
    url3 = "https://www.walmart.com/ip/3KVWGEE9ZRO3?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=79ce57c3-9b5e-4caa-98d9-9e7eb4ecc275&registryId=undefined&selected=true"
    url4 = "https://www.walmart.com/ip/63XNX0SLD1ZA?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=cf27005e-e61a-4782-aa5c-784b77942ba4&registryId=undefined&selected=true"

    urls = [url1, url2, url3, url4]

    while True:
        monitor(urls)

        