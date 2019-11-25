# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thermography.ui',
# licensing of 'thermography.ui' applies.
#
# Created: Fri Sep 13 16:16:40 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!
'''
Sample Code from
https://tomosoft.jp/design/?p=11549
'''

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QDoubleValidator
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 360)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(20, 40, 1020, 130))
        self.graphicsView.setObjectName("graphicsView")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(210, 240, 201, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(460, 240, 201, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(710, 240, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setValidator(QDoubleValidator())
        self.lineEdit.setGeometry(QtCore.QRect(50, 238, 113, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 200, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(460, 200, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 200, 80, 21))
        self.label_3.setObjectName("label_3")

        self.label_R_title = QtWidgets.QLabel(Dialog)
        self.label_R_title.setGeometry(QtCore.QRect(60, 320, 20, 21))
        self.label_R_title.setObjectName("label_R_title")
        self.label_R = QtWidgets.QLabel(Dialog)
        self.label_R.setGeometry(QtCore.QRect(80, 320, 40, 21))
        self.label_R.setObjectName("label_R")

        self.label_G_title = QtWidgets.QLabel(Dialog)
        self.label_G_title.setGeometry(QtCore.QRect(140, 320, 20, 21))
        self.label_G_title.setObjectName("label_G_title")
        self.label_G = QtWidgets.QLabel(Dialog)
        self.label_G.setGeometry(QtCore.QRect(160, 320, 40, 21))
        self.label_G.setObjectName("label_G")

        self.label_B_title = QtWidgets.QLabel(Dialog)
        self.label_B_title.setGeometry(QtCore.QRect(220, 320, 20, 21))
        self.label_B_title.setObjectName("label_B_title")
        self.label_B = QtWidgets.QLabel(Dialog)
        self.label_B.setGeometry(QtCore.QRect(240, 320, 40, 21))
        self.label_B.setObjectName("label_B")

        self.label_input_title = QtWidgets.QLabel(Dialog)
        self.label_input_title.setGeometry(QtCore.QRect(300, 320, 60, 21))
        self.label_input_title.setObjectName("label_input_title")
        self.label_input = QtWidgets.QLabel(Dialog)
        self.label_input.setGeometry(QtCore.QRect(400, 320, 40, 21))
        self.label_input.setObjectName("label_input")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "設定", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "offset input", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "offset green", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "gain", None, -1))

        self.label_R_title.setText(QtWidgets.QApplication.translate("Dialog", "R", None, -1))
        self.label_G_title.setText(QtWidgets.QApplication.translate("Dialog", "G", None, -1))
        self.label_B_title.setText(QtWidgets.QApplication.translate("Dialog", "B", None, -1))
        self.label_input_title.setText(QtWidgets.QApplication.translate("Dialog", "input", None, -1))