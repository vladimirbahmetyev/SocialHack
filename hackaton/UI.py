import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from orgSysCounter import calcOrgRait, frontend

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math


class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.font = QFont()
        self.font.setPointSize(20)
        self.font.setFamily("Calibri")
        self.font.setBold(True)

        logo = QLabel(self)
        logo.setPixmap(QPixmap('images/logo.png'))
        logo.move(70, 70)

        keyword = QLabel(self)
        keyword.setPixmap(QPixmap("images/keyword.png"))
        keyword.move(165, 220)

        keywordPic = QLabel(self)
        keywordPic.setPixmap(QPixmap("images/line.png"))
        keywordPic.move(120, 290)

        self.keywordInput = QLineEdit(self)
        self.keywordInput.setStyleSheet("QLineEdit {color:rgba(96, 2, 62, 1)}")
        self.keywordInput.move(170, 300)
        self.keywordInput.resize(500, 70)
        self.keywordInput.setFrame(False)
        self.keywordInput.setFont(self.font)

        resource = QLabel(self)
        resource.setPixmap(QPixmap("images/resource.png"))
        resource.move(165, 420)

        resourcePic = QLabel(self)
        resourcePic.setPixmap(QPixmap("images/line.png"))
        resourcePic.move(120, 490)

        self.resourceInput = QLineEdit(self)
        self.resourceInput.setStyleSheet("QLineEdit {color:rgba(96, 2, 62, 1)}")
        self.resourceInput.move(170, 500)
        self.resourceInput.resize(440, 70)
        self.resourceInput.setFrame(False)
        self.resourceInput.setFont(self.font)

        self.arrowButton = PicButton(QPixmap("images/downArrow.png"), self)
        self.arrowButton.move(628, 515)
        self.arrowButton.clicked.connect(self.downArrowClick)

        self.goButton = PicButton(QPixmap('images/go.png'), self)
        self.goButton.move(330, 730)
        # self.goButton.resize(180, 180)
        self.goButton.clicked.connect(self.on_click)


        self.goClicked = PicButton(QPixmap("images/goClicked.png"), self)
        self.goClicked.move(330, 730)
        self.goClicked.hide()

        # self.wrongData = QLabel(self)
        # self.wrongData.setPixmap(QPixmap("images/wrong.png"))
        # self.wrongData.move(240, 650)

        oImage = QImage("images/back.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)

        self.rightSquare = QLabel(self)
        self.rightSquare.setPixmap(QPixmap("images/rightSquare.png"))
        self.rightSquare.move(840, 0)

        self.doneSquare = QLabel(self)
        self.doneSquare.setPixmap(QPixmap("images/stats.png"))
        self.doneSquare.move(840, 0)
        self.doneSquare.hide()

        # self.totalSpam = QLineEdit(self)
        # self.totalSpam.setReadOnly(True)
        # self.totalSpam.setFrame(False)
        # self.totalSpam.setFont(self.font)

        self.setWindowIcon(QIcon('images/minilogo.png'))

        self.resize(1980, 1000)
        self.center()

        self.setWindowTitle('StatFinder')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_click(self):
        self.goButton.hide()
        self.goClicked.show()

        self._status_update_timer = QTimer(self)
        self._status_update_timer.setSingleShot(False)
        self._status_update_timer.timeout.connect(self.changeItem)
        self._status_update_timer.start(100)


        key = self.keywordInput.text()
        source = self.resourceInput.text()

        checkSource = True
        if len(key.strip(" ")) == 0 or len(source) == 0:
            checkSource = False

        if not checkSource:
            # self.wrongData.show()
            print("aaa")
        else:
            # self.wrongData.close()
            if source.lower() == "twitter":
                rating, uW, tL = calcOrgRait("https://twitter.com/search?q=", key)  # uW -- список весов юзеров
                                                                                    # tL -- список тональностей комментариев
                print(rating)                                                       # rating -- рейтинг поискового запроса
                plt.hist(tL)
                plt.savefig("graph.png")
                plt.show()
                self.graph = QLabel(self)
                self.graph.setPixmap(QPixmap("graph.png"))
                # self.graph.resize(530, 400)
                self.graph.move(1090, 100)
                self.graph.show()

                # sup = []
                # n = len(uW)
                # for i in range(n):
                #     count = 0
                #     for j in range(n):
                #         if uW[j] >= i / n and uW[j] < (i + 1) / n:
                #             count += 1
                #     sup.append(count)
                # x = np.arange(0, 1, 1 / n)
                # plt.plot(x, sup)
                # plt.show()

                spam = 0
                for w in uW:
                    if w < 0.15:
                        spam += 1
                spamers = spam / len(uW)

                self.totalSpam = QLineEdit(self)
                self.totalSpam.setStyleSheet("QLineEdit {color:rgba(96, 2, 62, 1)}")
                self.totalSpam.setReadOnly(True)
                self.totalSpam.setFrame(False)
                self.totalSpam.setFont(self.font)
                self.totalSpam.setText(str(round(spamers)))
                self.totalSpam.move(1525, 595)
                self.totalSpam.show()

            self.rightSquare.hide()
            self.doneSquare.show()

        # print(key, source)

    def changeItem(self):
        self.goClicked.hide()
        self.goButton.show()

    def downArrowClick(self):

        self.goButton.hide()

        self.resourceMenu = QLabel(self)
        self.resourceMenu.setPixmap(QPixmap("images/resourceMenuBig.png"))
        self.resourceMenu.move(120, 490)
        self.resourceMenu.show()

        self.menuChoice = QLineEdit(self)
        self.menuChoice.setStyleSheet("QLineEdit {color:rgba(96, 2, 62, 1)}")
        self.menuChoice.setText(self.resourceInput.text())
        self.menuChoice.setReadOnly(True)
        self.menuChoice.move(170, 500)
        self.menuChoice.resize(440, 70)
        self.menuChoice.setFrame(False)
        self.menuChoice.setFont(self.font)
        self.menuChoice.show()

        self.twitter = PicButton(QPixmap("images/twitter.png"), self)
        self.twitter.move(270, 590)
        self.twitter.show()
        self.twitter.clicked.connect(self.twitterClicked)

        self.vkButton = PicButton(QPixmap("images/vk.png"), self)
        self.vkButton.move(270, 660)
        self.vkButton.show()
        self.vkButton.clicked.connect(self.vkClicked)

        self.fbButton = PicButton(QPixmap("images/facebook.png"), self)
        self.fbButton.move(270, 730)
        self.fbButton.show()
        self.fbButton.clicked.connect(self.fbClicked)

        self.instButton = PicButton(QPixmap("images/instagram.png"), self)
        self.instButton.move(270, 800)
        self.instButton.show()
        self.instButton.clicked.connect(self.instClicked)

        self.upButton = PicButton(QPixmap("images/upArrow.png"), self)
        self.upButton.move(628, 515)
        self.upButton.show()
        self.upButton.clicked.connect(self.upButtonClick)

    def twitterClicked(self):
        self.menuChoice.setText("Twitter")
        self.upButtonClick()

    def vkClicked(self):
        self.menuChoice.setText("VK")
        self.upButtonClick()

    def fbClicked(self):
        self.menuChoice.setText("Facebook")
        self.upButtonClick()

    def instClicked(self):
        self.menuChoice.setText("Instagram")
        self.upButtonClick()

    def onActivated(self, text):
        self.resourceInput.setText(text)
        self.menuChoice.setText(text)

    def upButtonClick(self):
        self.resourceMenu.close()
        self.upButton.hide()
        self.goButton.show()
        self.resourceInput.setText(self.menuChoice.text())
        self.twitter.hide()
        self.vkButton.hide()
        self.fbButton.hide()
        self.instButton.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
