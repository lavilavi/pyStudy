# -*- coding: utf-8 -*-

import urllib.request, urllib.error
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import math

url = 'http://vippers.jp/archives/9609278.html'


def extract_texts(soup1):
    texts = []
    # remove scripts
    for script in soup1(["script", "style"]):
        script.decompose()
    text = soup1.get_text().replace('。', '。\n').split('\n')
    for li in text:
        if '' == li:
            continue
        else:
            texts.append(li)
    return texts


def show_text(soup1):
    for each in extract_texts(soup1):
        each = each.replace(' ', '')
        ind = math.ceil(len(each) / 50)
        for i in range(0, int(ind)):
            print(each[i * 50:(i + 1) * 50])


def show_raw(soup2):
    print(soup2)


def search(word, soup1):
    for text in extract_texts(soup1):
        if word in text:
            print(text)


def list_link_and_title(soup):
    for s in soup.text.split('\n'):
        if 'permalink' in s:
            print(s)
        elif 'title' in s:
            print(s)

if __name__ == '__main__':
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
        request = urllib.request.Request(url=url, headers=headers)
        request.add_header('Host', request.host.encode('idna'))
        res = urllib.request.urlopen(request)
    except urllib.error.URLError as e:
        print(e.reason, e.strerror)
        pass
    else:
        html = res.read()
        soup = BeautifulSoup(html, features="html.parser")
        show_text(soup)
