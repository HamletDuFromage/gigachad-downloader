#!/usr/bin/env python3

import requests
from bs4 import  BeautifulSoup
import re
import wget
import os

src = requests.get("http://sleekntears.com/en/sleekntears/")

soup = BeautifulSoup(src.content, "html.parser")

images = soup.find_all('a', {'href': re.compile("http:\/\/sleekntears.com\/wp-content.+jpg$")})

os.mkdir("Gigachad")

c = 1
t = len(images)
for i in images:
    print("\nDownloading Gigachad " + str(c) + "/" + str(t))
    wget.download(i["href"], "Gigachad/gigachad" + str(c))
    c += 1

