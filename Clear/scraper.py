import requests
import random
from requests import get
from bs4 import BeautifulSoup
import re

def GET_UA():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]
    return random.choice(uastrings)

headers = {"User-Agent": GET_UA()}

i = 0
ips = []

for i in range (1,1000):

    results = requests.get("*WEBSITE URL*"+format(i), headers=headers)

    soup = BeautifulSoup(results.text, "html.parser")

    #imgtag = soup.find_all(class_='thumbnail-item__img img-responsive')

    imgtag = soup.find_all(class_="thumbnail-item__img img-responsive")
 
    str(imgtag)

    src = re.findall("src=\"http://\w\S*\"", str(imgtag))

    ip = re.findall("h.+?(?=\")", str(src))

    for x in ip:
        ips.append(x)

    i = i + 1

with open("ips_raw.txt", "w+") as f:
    f.write(str(ips))

#print(soup.prettify())