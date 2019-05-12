import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


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
    items = ["Twitter", "VK", "Facebook", "Instagram", "Otzovik"]

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
        self.resourceInput.move(170, 500)
        self.resourceInput.resize(440, 70)
        self.resourceInput.setFrame(False)
        self.resourceInput.setFont(self.font)

        self.arrowButton = PicButton(QPixmap("images/downArrow.png"), self)
        self.arrowButton.move(628, 515)
        self.arrowButton.clicked.connect(self.downArrowClick)

        self.goButton = PicButton(QPixmap('images/go.png'), self)
        self.goButton.move(330, 730)
        self.goButton.resize(180, 180)
        # goButton.clicked.connect(QCoreApplication.instance().quit)
        self.goButton.clicked.connect(self.on_click)

        self.wrongData = QLabel(self)
        self.wrongData.setPixmap(QPixmap("images/wrong.png"))
        self.wrongData.move(240, 650)

        oImage = QImage("images/back.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)

        rightSquare = QLabel(self)
        rightSquare.setPixmap(QPixmap("images/rightSquare.png"))
        rightSquare.move(840, 0)

        self.setWindowIcon(QIcon('images/kaka.jpg'))

        self.resize(1980, 1000)
        self.center()

        self.setWindowTitle('Супер прилога')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_click(self):
        key = self.keywordInput.text()
        source = self.resourceInput.text()

        # self.wrongData = QLabel()
        # self.wrongData.setPixmap(QPixmap("wrong.png"))
        # self.wrongData.move(240, 752)

        checkSource = True
        if len(key.strip(" ")) == 0 or len(source) == 0:
            checkSource = False

        if not checkSource:
            self.wrongData.show()
            print("aaa")
        else:
            self.wrongData.close()


        print(key, source)

    def downArrowClick(self):

        self.goButton.hide()

        self.resourceMenu = QLabel(self)
        self.resourceMenu.setPixmap(QPixmap("images/resourceMenuBig.png"))
        self.resourceMenu.move(120, 490)
        self.resourceMenu.show()

        self.menuChoice = QLineEdit(self)
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
        self.menuChoice.setText("images/Twitter")
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
