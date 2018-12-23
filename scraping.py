# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 22:59:44 2018

@author: marcy

朝までハシゴの旅がある回の概要とその日付を出力
"""

import csv
import bs4
import re
from urllib import request

url = "http://www.ntv.co.jp/warakora/next/backnumber.html"
html = request.urlopen(url)
soup = bs4.BeautifulSoup(html, "html.parser")

tag = soup.find_all("li")
urllist = []
for i in tag:
    urllist.append("http://www.ntv.co.jp/warakora/next/" + i.a.get("href"))

hashigo_str = []
date = []
for j in urllist:
    url2 = j
    html2 = request.urlopen(url2)
    soup2 = bs4.BeautifulSoup(html2, "html.parser")
    hashigo = soup2.find("h3", text=re.compile("ハシゴ"))
    if bool(hashigo):
        hashigo_str.append(str(hashigo.find_next()))
        date.append(re.sub(r'\D', '', j))

hashigo_list = []
hashigo_list.append(date)
hashigo_list.append(hashigo_str)

with open('data/file.csv', 'w', encoding='CP932', errors='replace') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(hashigo_list)

