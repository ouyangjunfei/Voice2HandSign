# -*-coding:utf-8-*-

from utils.getPictures import getPicsDatas
from utils.getHttpRequest import postRequest
from utils.recordVoice import record
from utils.gui import *

import sys
import os

if __name__ == '__main__':
    print(sys.path)
    voice_path = os.path.abspath('..')
    #"../resources/i_like_you.wav"
    image_path = os.path.abspath('..')
        #"../resources/images/"
    print(voice_path)
    print(image_path)
    # record(voice_path)
    #words = postRequest(voice_path)
    # print(words)
    #data = getPicsDatas(words, image_path)
    # print(data)
    #app = QtWidgets.QApplication(sys.argv)
    window = Window(image_path, data)
    #sys.exit(app.exec_())
