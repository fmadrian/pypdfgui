# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Main(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_merge = QtWidgets.QPushButton(Dialog)
        self.btn_merge.setObjectName("btn_merge")
        self.verticalLayout.addWidget(self.btn_merge)
        self.btn_split = QtWidgets.QPushButton(Dialog)
        self.btn_split.setObjectName("btn_split")
        self.verticalLayout.addWidget(self.btn_split)
        self.btn_about = QtWidgets.QPushButton(Dialog)
        self.btn_about.setObjectName("btn_about")
        self.verticalLayout.addWidget(self.btn_about)
        self.btn_exit = QtWidgets.QPushButton(Dialog)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_merge.setText(_translate("Dialog", "Merge"))
        self.btn_split.setText(_translate("Dialog", "Split"))
        self.btn_about.setText(_translate("Dialog", "About"))
        self.btn_exit.setText(_translate("Dialog", "Exit"))
