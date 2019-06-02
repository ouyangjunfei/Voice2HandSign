import os
import sys
from urllib import request
import requests
from bs4 import BeautifulSoup


def getPicsDatas(sentence, image_path):
    html = requests.get('https://shouyu.51240.com/' + sentence + '__shouyus/')
    bsObject = BeautifulSoup(html.text, "html.parser")
    table = bsObject.body.find_all('table', {'width': '100%'})
    word = bsObject.find_all('td', {'width': '30', 'bgcolor': '#F5F5F5'})
    explain = bsObject.find_all('td', {'bgcolor': '#FFFFFF'})
    data = []
    table_len = len(table)
    path = image_path
    if not os.path.exists(path):
        os.mkdir(path)
    for i in range(1, table_len + 1):
        sentence = word[i - 1].text
        sentence = sentence + ' : ' + explain[(i - 1) * 2].text
        data.append(sentence)
        img_src = explain[2 * i - 1].find('img').get('src')
        request.urlretrieve('http:' + img_src, path + str(i - 1) + '.png')
    return data
