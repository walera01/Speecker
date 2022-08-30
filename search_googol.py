import requests

from bs4 import BeautifulSoup
def search_google(query):
    print(query)
    url = f"https://www.google.com/search?q={query}&rlz=1C1GCEU_ruBY1016BY1016&sxsrf=ALiCzsb_BEF5OFGHvuXdgFC2TDPh57Hguw%3A1661856845330&ei=TewNY-LBE4HrrgTk7Lm4Ag&ved=0ahUKEwiinLuXs-75AhWBtYsKHWR2DicQ4dUDCA4&uact=5&oq=%D1%87%D1%82%D0%BE+%D1%82%D0%B0%D0%BA%D0%BE%D0%B5+%D0%B0%D1%81%D1%82%D1%80%D0%B0%D0%BB&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIECAAQCjIECAAQCjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgQIIxAnOgsIABCABBCxAxCDAToLCC4QgAQQsQMQgwE6DgguEIAEELEDEIMBENQCOggILhCxAxCDAToLCC4QsQMQgwEQ1AI6BAgAEEM6BAguEEM6BwgjEMkDECc6BQgAEJIDOggIABCABBCxA0oECEEYAEoECEYYAFAAWP05YPQ7aABwAXgAgAG-AYgBmBCSAQQwLjE2mAEAoAEBwAEB&sclient=gws-wiz-serp"
    headers = {
        "Accept":"*/*",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")
    try:
        explanation = soup.find(class_="PZPZlf hb8SAc").find_all("span")
    except:
        explanation = soup.find(class_="MjjYud")

    return explanation[2].text