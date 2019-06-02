# -*-coding:utf-8-*-

from utils.getPictures import dataset
from utils.getHttpRequest import postRequest

if __name__ == '__main__':
    words = postRequest()
    print(words)
    data, img = dataset(words)
