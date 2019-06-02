# -*-coding:utf-8-*-

from gui.picsgui import *

import sys
import os

if __name__ == '__main__':
    voice_path = os.path.abspath('..') + "/resources/sample.wav"
    image_path = os.path.abspath('..') + "/resources/images/"

    app = QtWidgets.QApplication(sys.argv)
    window = Window(voice_path, image_path)
    sys.exit(app.exec_())
