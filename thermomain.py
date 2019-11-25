'''
input value(0.0-1.0) convert heat map and display it.
Require PySide2(Qt for Python)

Author: Takehiro Matsuda
Date: Sep. 13, 2019
'''

import sys
import os

from PySide2.QtCore import (QLineF, QPointF, QRectF, Qt)
from PySide2.QtWidgets import (QApplication, QWidget, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QGraphicsLineItem,
                             QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsPixmapItem)
from PySide2.QtGui import (QIcon, QPixmap, QBrush, QPen, QColor)
from thermography import Ui_Dialog
#from main_window import MainWindow
import numpy as np

#gain = 30
comp_offset_x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
comp_offset_green = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

view = 0
scene = 0


def sigmoid(x, gain=1, offset_x=0):
    return ((np.tanh(((x + offset_x) * gain) / 2) + 1) / 2)


def colorBarRGB(x, offset_x, offset_green, gain):
    x = (x * 2) - 1
    red = sigmoid(x, gain, -1 * offset_x)
    blue = 1 - sigmoid(x, gain, offset_x)
    green = sigmoid(x, gain, offset_green) + (1 - sigmoid(x, gain, -1 * offset_green))
    green = green - 1.0
    return (red * 256, green * 256, blue * 256)


class Test(QWidget):
    def __init__(self):
        # super() でスーパークラスのインスタンスメソッドを呼び出す
        #        super(MainWindow, self).__init__(parent)
        super().__init__()

        self.ui = Ui_Dialog()
        #self.ui = MainWindow()
        self.ui.setupUi(self)
        self.view = self.ui.graphicsView
        self.view.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.scene = QGraphicsScene()

        # アイテムの名前設定
        self.ui.comboBox.addItem("{}".format(comp_offset_x[0]))
        self.ui.comboBox.addItem("{}".format(comp_offset_x[1]))
        self.ui.comboBox.addItem("{}".format(comp_offset_x[2]))
        self.ui.comboBox.addItem("{}".format(comp_offset_x[3]))
        self.ui.comboBox.addItem("{}".format(comp_offset_x[4]))
        self.ui.comboBox.addItem("{}".format(comp_offset_x[5]))
        self.ui.comboBox.addItem("{}".format(comp_offset_x[6]))
        self.ui.comboBox.addItem("{}".format(comp_offset_x[7]))
        self.ui.comboBox.addItem("{}".format(comp_offset_x[8]))
        self.ui.comboBox.addItem("{}".format(comp_offset_x[9]))
        self.ui.comboBox.addItem("{}".format(comp_offset_x[10]))
        self.ui.comboBox.setCurrentIndex(2)

        self.ui.comboBox_2.addItem("{}".format(comp_offset_green[0]))
        self.ui.comboBox_2.addItem("{}".format(comp_offset_green[1]))
        self.ui.comboBox_2.addItem("{}".format(comp_offset_green[2]))
        self.ui.comboBox_2.addItem("{}".format(comp_offset_green[3]))
        self.ui.comboBox_2.addItem("{}".format(comp_offset_green[4]))
        self.ui.comboBox_2.addItem("{}".format(comp_offset_green[5]))
        self.ui.comboBox_2.addItem("{}".format(comp_offset_green[6]))
        self.ui.comboBox_2.addItem("{}".format(comp_offset_green[7]))
        self.ui.comboBox_2.addItem("{}".format(comp_offset_green[8]))
        self.ui.comboBox_2.addItem("{}".format(comp_offset_green[9]))
        self.ui.comboBox_2.addItem("{}".format(comp_offset_green[10]))
        self.ui.comboBox_2.setCurrentIndex(6)

        self.ui.lineEdit.setText('10.0')

        self.ui.pushButton.clicked.connect(lambda: self.buttonClicked("Hello world"))

    def buttonClicked(self, str):
        print("{} {} {}".format(str, self.ui.comboBox.currentIndex(), self.ui.comboBox_2.currentIndex()))

        offset_x = comp_offset_x[self.ui.comboBox.currentIndex()]
        offset_green = comp_offset_green[self.ui.comboBox_2.currentIndex()]
        gain = float(self.ui.lineEdit.text())

        self.data = [colorBarRGB(x * 0.001, offset_x, offset_green, gain) for x in range(1000)]

        for i in range(1000):
            # QPenの設定
            pen = QPen(QColor(self.data[i][0], self.data[i][1], self.data[i][2]), 1, Qt.SolidLine, Qt.RoundCap,
                       Qt.RoundJoin)
            self.scene.addLine(i, 0, i, 80, pen)

        self.view.setScene(self.scene)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickToColor(event)

    def clickToColor(self, event):
        self.px = event.pos().x()
        self.py = event.pos().y()
        #print('px:{px}, py:{py}'.format(px=self.px, py=self.py))
        #print(type(self.px))

        view_geo = self.view.geometry()
        #print('view_geo{}'.format(view_geo))
        self.cp_x = self.px - view_geo.left()
        self.cp_y = self.py - view_geo.top()
        print('cp_x:{cp_x}, cp_y:{cp_y}'.format(cp_x=self.cp_x, cp_y=self.cp_y))

        #print('data size:{}'.format(len(self.data)))
        #view_margin = self.view.alignment()
        #print('view_margin:{}'.format(view_margin))

        selectLine = self.view.itemAt(self.cp_x, self.cp_y)
        if not selectLine is None:
            select_color = selectLine.pen().color()
            r = select_color.red()
            g = select_color.green()
            b = select_color.blue()
            input_value = self.cp_x / 1000

            self.ui.label_R.setText(str(r))
            self.ui.label_G.setText(str(g))
            self.ui.label_B.setText(str(b))
            self.ui.label_input.setText(str(input_value))

            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())