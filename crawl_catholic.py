# -*- coding: utf-8 -*-
from urllib.request import urlopen, Request
import urllib
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import data_set as config

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

"""
원하는 키워드를 받으면 로컬 파일에 추가하는걸로 
"""
# print(parse_catholic())
# config.my_list.append('3333')
# print(config.my_list)

def get_keywords():
    keywords = []
    with open('keyword_set.text', 'r') as f:
        while True:
            line = f.readline()
            if not line: break
            line = line.replace('\n', '')
            line = line.strip()
            keywords.append(line)
    return keywords
        

