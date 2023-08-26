# -*- coding: utf-8 -*- 
'''
    【简介】
	PyQT5中表格头为自适应模式例子
  
  
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication , QTableWidgetItem, QHeaderView)
from PyQt5 import  *

class Table(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.tableWidget.doubleClicked.connect(self.double_value)
		self.tableWidget.horizontalHeader().sectionClicked.connect(self.headleHeaderClicked)
	def headleHeaderClicked(self,columnIndex):
		item=self.tableWidget.horizontalHeaderItem(columnIndex)
		if item:
			print("表头索引",columnIndex)
			print("表头内容",item.text())

	def double_value(self):
		for i in self.tableWidget.selectedItems():
			print(i.row(),i.column(),i.text())

	def initUI(self):
		self.setWindowTitle("QTableWidget demo")
		self.resize(500,300);
		conLayout = QHBoxLayout()
		self.tableWidget= QTableWidget()
		self.tableWidget.setRowCount(4)
		self.tableWidget.setColumnCount(3)
		conLayout.addWidget(self.tableWidget)
		self.list1=['姓名','性别','体重(kg)']
		self.tableWidget.setHorizontalHeaderLabels(self.list1)
		#tableWidget.setVerticalHeaderLabels(['行1','行2','行3','行4' ])        
		self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
				 
		newItem = QTableWidgetItem("张三")  
		self.tableWidget.setItem(0, 0, newItem)
		  
		newItem = QTableWidgetItem("男")  
		self.tableWidget.setItem(0, 1, newItem)
		  
		newItem = QTableWidgetItem("160")  
		self.tableWidget.setItem(0, 2, newItem)

		self.setLayout(conLayout)
		newItem = QTableWidgetItem("李四")
		self.tableWidget.setItem(1, 0, newItem)
		#print(self.tableWidget.currentColumn())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Table()  
	example.show()   
	sys.exit(app.exec_())
