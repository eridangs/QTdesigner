# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditNum1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNum1.setGeometry(QtCore.QRect(290, 130, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEditNum1.setFont(font)
        self.lineEditNum1.setObjectName("lineEditNum1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 230, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEditNum2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNum2.setGeometry(QtCore.QRect(290, 220, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEditNum2.setFont(font)
        self.lineEditNum2.setObjectName("lineEditNum2")
        self.pushButtonCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCalcular.setGeometry(QtCore.QRect(190, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCalcular.setFont(font)
        self.pushButtonCalcular.setObjectName("pushButtonCalcular")
        self.labelResultado = QtWidgets.QLabel(self.centralwidget)
        self.labelResultado.setGeometry(QtCore.QRect(90, 420, 361, 171))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(15)
        self.labelResultado.setFont(font)
        self.labelResultado.setText("")
        self.labelResultado.setWordWrap(True)
        self.labelResultado.setObjectName("labelResultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "EX7: Calculadora"))
        self.label_2.setText(_translate("MainWindow", "Primeiro numero:"))
        self.label_3.setText(_translate("MainWindow", "Primeiro numero:"))
        self.pushButtonCalcular.setText(_translate("MainWindow", "CALCULAR"))
