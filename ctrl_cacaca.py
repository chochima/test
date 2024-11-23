from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
import sys
from cacaca import Ui_Dialog
app = QApplication(sys.argv)
widget = QWidget()
self_movie = QMovie()
ui = Ui_Dialog()
ui.setupUi(widget)

tmp = ""
def click(A):
    global tmp
    tmp = tmp+A
    ui.label.setText(tmp)

def click_0():
    click("0")
def click_1():
    click("1")
def click_2():
    click("2")
def click_3():
    click("3")
def click_4():
    click("4")
def click_5():
    click("5")
def click_6():
    click("6")
def click_7():
    click("7")
def click_8():
    click("8")
def click_9():
    click("9")


def nono():
    a = ui.lineEdit_01.text()
    b = ui.lineEdit_2.text()
    msgBox = QMessageBox()

    if int(b) == 0:
        msgBox.setInformativeText("no")
    else:
        c = int(a)/int(b)
        msgBox.setInformativeText(str(int(c)))
    msgBox.exec_()


def click_pic(event):
    if event.button() == 1:
       usagiBox = QMessageBox()
       usagiBox.setInformativeText("咿↗呀↗哈↘")
    elif event.button() ==2:
       usagiBox = QMessageBox()
       usagiBox.setInformativeText("蛤↗")
    usagiBox.exec_()

ui.label_usagi.mouseReleaseEvent = click_pic

ui.pushButton_div.clicked.connect(nono)
ui.pushButton_0.clicked.connect(click_0)
ui.pushButton_1.clicked.connect(click_1)
ui.pushButton_2.clicked.connect(click_2)
ui.pushButton_3.clicked.connect(click_3)
ui.pushButton_4.clicked.connect(click_4)
ui.pushButton_5.clicked.connect(click_5)
ui.pushButton_6.clicked.connect(click_6)
ui.pushButton_7.clicked.connect(click_7)
ui.pushButton_8.clicked.connect(click_8)
ui.pushButton_9.clicked.connect(click_9)

self_movie.movie = QMovie("usagi_gif.gif")
ui.label_usagi.setMovie(self_movie.movie)
self_movie.movie.start()
widget.show()
app.exec_()

