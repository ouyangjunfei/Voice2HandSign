from bs4 import BeautifulSoup
import requests
from urllib import request
from PIL import Image


def dataset(sentence):
    html = requests.get('https://shouyu.51240.com/' + sentence + '__shouyus/')
    bsObject = BeautifulSoup(html.text, "html.parser")
    table = bsObject.body.find_all('table', {'width': '100%'})
    word = bsObject.find_all('td', {'width': '30', 'bgcolor': '#F5F5F5'})
    explain = bsObject.find_all('td', {'bgcolor': '#FFFFFF'})
    data = []
    img = []
    table_len = len(table)
    for i in range(1, table_len + 1):
        sentence = word[i - 1].text
        sentence = sentence + ' : ' + explain[(i - 1) * 2].text
        data.append(sentence)
        img_src = explain[2 * i - 1].find('img').get('src')
        request.urlretrieve('http:' + img_src, str(i) + '.png')
    for i in range(1, table_len + 1):
        img.append(Image.open(str(i) + '.png'))
    return data, img
