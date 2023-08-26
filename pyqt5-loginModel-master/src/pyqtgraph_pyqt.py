# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import pandas as pd
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication,QVBoxLayout
import pyqtgraph as pg
from src.Ui_pyqtgraph_pyqt import Ui_MainWindow
import matplotlib.pyplot as plt
#from Ui_pyqtgraph_pyqt import Ui_MainWindow
import numpy as np
import pandas as pd
import seaborn as sns
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation,pyqtSignal
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.data3=pd.DataFrame()
        self.col=[]
        pg.setConfigOption('background', '#f0f0f0')  # 设置背景为灰色
        pg.setConfigOption('foreground', 'd')  # 设置前景（包括坐标轴，线条，文本等等）为黑色。
        pg.setConfigOptions(antialias=True) # 使曲线看起来更光滑，而不是锯齿状
        # pg.setConfigOption('antialias',True) # 等价于上一句，所不同之处在于setconfigOptions可以传递多个参数进行多个设置，而setConfigOption一次只能接受一个参数进行一个设置。
        self.setupUi(self)
    @pyqtSlot()
    def on_pushButton_1_clicked(self):
        print("初始化tab3")
        self.linetext.setText(";".join(self.col))
        print(self.col)
        #print(self.data3)
        #self.pyqtgraph1.clear() # 清空里面的内容，否则会发生重复绘图的结果
        '''第一种绘图方式'''
        #self.pyqtgraph1.addPlot(title="绘图单条线", y=np.random.normal(size=100), pen=pg.mkPen(color='b', width=2))
        '''第二种绘图方式'''
        '''
        plt2 = self.pyqtgraph1.addPlot(title='绘制多条线')

        plt2.plot(np.random.normal(size=150), pen=pg.mkPen(color='r', width=2), name="Red curve") # pg.mkPen的使用方法，设置线条颜色为红色，宽度为2。
        plt2.plot(np.random.normal(size=110) + 5, pen=(0, 255, 0), name="Green curve")
        plt2.plot(np.random.normal(size=120) + 10, pen=(0, 0, 255), name="Blue curve")
        '''

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        '''如果没有进行第一次绘图，就开始绘图，然后做绘图标记，否则就什么都不做'''
        try:
            self.first_plot_flag # 检测是否进行过第一次绘图。
        except:





            print(self.col)


            #self.pyqtgraph2.nextRow()
            self.pyqtgraph2.clear()
            p4 = self.pyqtgraph2.addPlot(title="可视化分析")
            x = self.data3[self.col[0]]
            y = self.data3[self.col[1]]
            p4.plot(x, y)
            p4.showGrid(x=True, y=True) # 显示网格

            self.first_plot_flag = True # 第一次绘图后进行标记

    @pyqtSlot()
    def on_pushButton_3_clicked(self):

        sns.heatmap(self.data3.corr(), vmax=1, cmap="RdYlGn", annot=True)
        plt.show()

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        try:
            self.col.pop()
        except:
            print("参数列表已空")
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
