import requests
import time

from message import  sendMail

def check_item_stock(url):
    session = requests.session()

    response = session.get(url)
    print(response)
    if (response.status_code != 200) :
        print("error occurs|response={0}|url={1}".format(response.text, url))
        return False
    if (response.text.find("Add to Cart") > 0 or response.text.find("Add to cart") > 0 or response.text.find("add to cart")> 0):
        return True
    session.close()
    return False

def monitor(urls):
    for url in urls:
        ans = check_item_stock(url)
        time.sleep(5)
        try:
            if (ans):
                print("have stock here;url={0}".format(url))
                sendMail("yinjialiu003@gmail.com", "walmart goods coming, go!go!go!", url)

        except Exception as e:
            print("url={0}".format(url))
            print(e)


if __name__ == "__main__":
    url9 = "https://www.walmart.com/ip/Lysol-All-Purpose-Cleaner-Spray-Lemon-Breeze-Kills-Germs-2X32oz/483952655"

    url1 = "https://www.walmart.com/ip/3ZQ8YRFR0F4K?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=354fca58-9895-491a-adba-615d0f99b2cb&registryId=undefined&selected=true"
    url2 = "https://www.walmart.com/ip/1A4RHBN5T52K?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=f182ab01-7a54-42e8-8d51-f8f10b694dd0&registryId=undefined&selected=true"
    url3 = "https://www.walmart.com/ip/3KVWGEE9ZRO3?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=79ce57c3-9b5e-4caa-98d9-9e7eb4ecc275&registryId=undefined&selected=true"
    url4 = "https://www.walmart.com/ip/63XNX0SLD1ZA?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=cf27005e-e61a-4782-aa5c-784b77942ba4&registryId=undefined&selected=true"
    url5 = "https://www.walmart.com/ip/4DF0PXDXOMWG?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=483fe049-b7d1-4954-b58c-de0b50cfab56&registryId=undefined&selected=true"
    url7 = "https://www.walmart.com/ip/4XO0I9NJ6ULS?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=aa17add3-7b08-4356-b18b-a86feeaa0005&registryId=undefined&selected=true"

    url8 = "https://www.walmart.com/ip/6M3GJG5PIQJL?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=5a45690a-0f73-4cfb-b90e-edbe242abd75&registryId=undefined&selected=true"
    url9 = "https://www.walmart.com/ip/50J6L06NG27R?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=628f3c35-4102-4e03-b353-ad5df99ac51e&registryId=undefined&selected=true"
    url10 = "https://www.walmart.com/ip/3ZQ8YRFR0F4K?listId=f83f7815-d988-45df-a79f-a12aa1277294&listType=WL&listItemId=354fca58-9895-491a-adba-615d0f99b2cb&registryId=undefined&selected=true"
    urls = [url1, url2, url3, url4, url5, url7, url8, url9, url10]

    while True:
        monitor(urls)

