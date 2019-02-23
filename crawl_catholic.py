# -*- coding: utf-8 -*-
from urllib.request import urlopen, Request
import urllib
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def parse_catholic():
    url = 'https://www.catholic.ac.kr/front/boardlist.do?cmsDirPkid=2053&cmsLocalPkid=1'
    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html, features='lxml')
    temp = soup.find('div',class_='rbbs_list_normal_sec').findAll('li')
    notice_set = []
    for div_info in temp:
        data = div_info.find('div', class_='text').text
        data = data.replace('새글', '')
        data = data.strip()
        notice_set.append(data)
    return notice_set

print(parse_catholic())

