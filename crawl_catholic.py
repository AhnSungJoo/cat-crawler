# -*- coding: utf-8 -*-
from urllib.request import urlopen, Request
import urllib
import bs4
import ssl
import datetime
ssl._create_default_https_context = ssl._create_unverified_context
import tgalarm as tg

def parse_catholic():
    url = 'https://www.catholic.ac.kr'
    notice_url = '/front/boardlist.do?cmsDirPkid=2053&cmsLocalPkid=1'
    req = Request(url + notice_url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html, features='lxml')
    temp = soup.find('div',class_='rbbs_list_normal_sec').findAll('li')
    notice_set = []
    href_set = []
    target_date = []
    for idx, div_info in enumerate(temp):
        data_info = div_info.find('div', class_='info_line').findAll('div')
        date_idx = str(data_info).find('작성일')
        if date_idx != -1:
            target_date.append(str(data_info)[date_idx+6: date_idx+16])
        else: 
            target_date.append('0')
        data = div_info.find('div', class_='text').text
        temp_href = div_info.find('a').get('href')
        href_set.append(url + temp_href)
        data = data.replace('새글', '')
        data = data.strip()
        notice_set.append(data)
    return notice_set, href_set, target_date

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
        

def send_notice():
    today = str(datetime.datetime.now())[:10]
    notice_set, href_set, target_date = parse_catholic()
    keywords = get_keywords()  # keywords 모음 

    for idx, notice in enumerate(notice_set):
        for keyword in keywords:
            if keyword in notice and target_date[idx] == today:
                tg.sendTo('catholic', notice + '\n' + href_set[idx])


if __name__ == '__main__':
    send_notice()
