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
        self.btn_start = QPushButton(self)
        self.btn_clear = QPushButton(self)
        self.setbackgroundcolor(255, 255, 255)
        # self.resize(400, 600)
        self.setFixedSize(800, 800)
        self.setWindowTitle("语音转换手语图")
        self.scroll.resize(800, 700)
        self.scroll.move(0, 100)
        self.topFiller.setMinimumSize(1000, 500)
        self.scroll.show()
        self.btn_start.setText("开始")
        self.btn_start.move(250, 30)
        self.btn_start.clicked.connect(self.record)
        self.btn_clear.setText("清空")
        self.btn_clear.move(450, 30)
        self.btn_clear.clicked.connect(self.clearall)
        self.show()

    def clearall(self):
        for i in range(0, len(self.labels)):
            self.labels[i].close()
            self.texts[i].close()
        self.labels.clear()
        self.texts.clear()
        print("清空")

    def setbackgroundcolor(self, r, g, b):
        palette = QtGui.QPalette()
        palette.setColor(self.backgroundRole(), QColor(r, g, b))
        self.setPalette(palette)

    def record(self):
        # print("开始")
        recordVoice(self.voice_path)
        words = postRequest(self.voice_path)
        print(words)
        if (words.__contains__("，")):
            sentences = words.split("，")
            for i in range(0, len(sentences)):
                print(sentences[i])
                data = getPicsDatas(sentences[i], self.image_path)
                print(data)
                self.action(data)
        else:
            data = getPicsDatas(words, self.image_path)
            print(data)
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
            self.texts[i].setFixedSize(1000, 20)
            self.texts[i].move(80, 50 + 200 * i + 150)
            self.topFiller.setMinimumSize(1000, 50 + 200 * (i + 1))
            img = QPixmap(self.image_path + str(i) + '.png')
            self.labels[i].setPixmap(img)
            self.scroll.setWidget(self.topFiller)
            self.labels[i].show()
            self.texts[i].show()
