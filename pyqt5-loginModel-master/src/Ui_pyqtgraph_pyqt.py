# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\zw_own\PyQt\Python3\testPyQt5_7\my_pyqt_book\pyqtgraph_pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pyqtgraph2 = GraphicsLayoutWidget(self.centralwidget)
        self.pyqtgraph2.setGeometry(QtCore.QRect(10, 50, 700, 500))
        self.pyqtgraph2.setObjectName("pyqtgraph2")
        self.pushButtontab31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtontab31.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButtontab31.setObjectName("pushButton_1")
        self.pushButtontab32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtontab32.setGeometry(QtCore.QRect(100, 0, 75, 23))
        self.pushButtontab32.setObjectName("pushButton_2")
        self.pushButtontab33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtontab33.setGeometry(QtCore.QRect(200, 0, 75, 23))
        self.pushButtontab33.setObjectName("pushButton_3")
        self.pushButtontab34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtontab34.setGeometry(QtCore.QRect(300, 0, 75, 23))
        self.pushButtontab34.setObjectName("pushButton_4")
        self.pushButtontab35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtontab35.setGeometry(QtCore.QRect(400, 0, 75, 23))
        self.pushButtontab35.setObjectName("pushButton_5")
        self.pushButtontab36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtontab36.setGeometry(QtCore.QRect(500, 0, 75, 23))
        self.pushButtontab36.setObjectName("pushButton_6")
        self.linetext=QtWidgets.QLineEdit(self.centralwidget)
        self.linetext.setGeometry(QtCore.QRect(0, 30, 750, 23))
        self.linetext.setObjectName("colname")
        self.linetext1 = QtWidgets.QLineEdit(self.centralwidget)
        self.linetext1.setGeometry(QtCore.QRect(0, 550, 750, 23))
        self.linetext1.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0,1000,23))
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

        self.pushButtontab32.setText(_translate("MainWindow", "垂直绘图"))
        self.pushButtontab31.setText(_translate("MainWindow", "初始化"))
        self.pushButtontab33.setText(_translate("MainWindow", "相关性分析"))
        self.pushButtontab34.setText(_translate("MainWindow", "删除参数"))

from pyqtgraph import GraphicsLayoutWidget
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

'''