# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bip44_page.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(538, 370)
        self.coin_list = QtWidgets.QListView(Dialog)
        self.coin_list.setGeometry(QtCore.QRect(10, 30, 121, 251))
        self.coin_list.setObjectName("coin_list")
        self.acc_list = QtWidgets.QListView(Dialog)
        self.acc_list.setGeometry(QtCore.QRect(140, 30, 121, 251))
        self.acc_list.setObjectName("acc_list")
        self.chn_list = QtWidgets.QListView(Dialog)
        self.chn_list.setGeometry(QtCore.QRect(270, 30, 121, 251))
        self.chn_list.setObjectName("chn_list")
        self.add_list = QtWidgets.QListView(Dialog)
        self.add_list.setGeometry(QtCore.QRect(400, 30, 121, 251))
        self.add_list.setObjectName("add_list")
        self.close_btn = KDialogButtonBox(Dialog)
        self.close_btn.setGeometry(QtCore.QRect(425, 330, 91, 27))
        self.close_btn.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.close_btn.setObjectName("close_btn")
        self.coin_add_btn = KPushButton(Dialog)
        self.coin_add_btn.setGeometry(QtCore.QRect(10, 290, 41, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.coin_add_btn.setFont(font)
        self.coin_add_btn.setObjectName("coin_add_btn")
        self.coin_rm_btn = KPushButton(Dialog)
        self.coin_rm_btn.setGeometry(QtCore.QRect(60, 290, 71, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.coin_rm_btn.setFont(font)
        self.coin_rm_btn.setObjectName("coin_rm_btn")
        self.acc_rm_btn = KPushButton(Dialog)
        self.acc_rm_btn.setGeometry(QtCore.QRect(190, 290, 71, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.acc_rm_btn.setFont(font)
        self.acc_rm_btn.setObjectName("acc_rm_btn")
        self.acc_add_btn = KPushButton(Dialog)
        self.acc_add_btn.setGeometry(QtCore.QRect(140, 290, 41, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.acc_add_btn.setFont(font)
        self.acc_add_btn.setObjectName("acc_add_btn")
        self.chn_rm_btn = KPushButton(Dialog)
        self.chn_rm_btn.setGeometry(QtCore.QRect(320, 290, 71, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chn_rm_btn.setFont(font)
        self.chn_rm_btn.setObjectName("chn_rm_btn")
        self.chn_add_btn = KPushButton(Dialog)
        self.chn_add_btn.setGeometry(QtCore.QRect(270, 290, 41, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chn_add_btn.setFont(font)
        self.chn_add_btn.setObjectName("chn_add_btn")
        self.add_rm_btn = KPushButton(Dialog)
        self.add_rm_btn.setGeometry(QtCore.QRect(450, 290, 71, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_rm_btn.setFont(font)
        self.add_rm_btn.setObjectName("add_rm_btn")
        self.add_add_btn = KPushButton(Dialog)
        self.add_add_btn.setGeometry(QtCore.QRect(400, 290, 41, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_add_btn.setFont(font)
        self.add_add_btn.setObjectName("add_add_btn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 66, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 66, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(270, 10, 66, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 10, 66, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.coin_add_btn.setText(_translate("Dialog", "Add"))
        self.coin_rm_btn.setText(_translate("Dialog", "Remove"))
        self.acc_rm_btn.setText(_translate("Dialog", "Remove"))
        self.acc_add_btn.setText(_translate("Dialog", "Add"))
        self.chn_rm_btn.setText(_translate("Dialog", "Remove"))
        self.chn_add_btn.setText(_translate("Dialog", "Add"))
        self.add_rm_btn.setText(_translate("Dialog", "Remove"))
        self.add_add_btn.setText(_translate("Dialog", "Add"))
        self.label.setText(_translate("Dialog", "Coin"))
        self.label_2.setText(_translate("Dialog", "Account"))
        self.label_3.setText(_translate("Dialog", "Chain"))
        self.label_4.setText(_translate("Dialog", "Address"))

from kdialogbuttonbox import KDialogButtonBox
from kpushbutton import KPushButton
