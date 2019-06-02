# -*-coding:utf-8-*-

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from utils.recordVoice import recordVoice
from utils.getPictures import getPicsDatas
from utils.getHttpRequest import postRequest


class Window(QWidget):

    def __init__(self, voice_path, image_path):
        super(Window, self).__init__()
        self.labels = []
        self.texts = []
        self.voice_path = voice_path
        self.image_path = image_path
        self.topFiller = QWidget(self)
        self.scroll = QScrollArea(self)
        self.btn = QPushButton(self)
        self.setbackgroundcolor(255, 255, 255)
        self.resize(400, 600)
        self.setWindowTitle("语音转换手语图")
        self.scroll.resize(400, 500)
        self.scroll.move(0, 100)
        self.topFiller.setMinimumSize(360, 500)
        self.scroll.show()
        self.btn.setText("开始")
        self.btn.move(140, 30)
        self.btn.clicked.connect(self.record)
        self.show()

    def setbackgroundcolor(self, r, g, b):
        palette = QtGui.QPalette()
        palette.setColor(self.backgroundRole(), QColor(r, g, b))
        self.setPalette(palette)

    def record(self):
        recordVoice(self.voice_path)
        words = postRequest(self.voice_path)
        data = getPicsDatas(words, self.image_path)
        self.action(data)

    def action(self, data):
        size = len(data)
        for i in range(0, size):
            self.labels.append(QLabel(self.topFiller))
            self.labels[i].setText("")
            self.labels[i].setFixedSize(180, 150)
            self.labels[i].move(80, 50 + 200 * i)
            self.texts.append(QLabel(self.topFiller))
            self.texts[i].setText((data)[i])
            self.texts[i].setFixedSize(180, 20)
            self.texts[i].move(80, 50 + 200 * i + 150)
            self.topFiller.setMinimumSize(360, 50 + 200 * (i + 1))
            img = QPixmap(self.image_path + str(i) + '.png')
            self.labels[i].setPixmap(img)
            self.scroll.setWidget(self.topFiller)
            self.labels[i].show()
            self.texts[i].show()
