import tools.mysql as MySQLConnect
from ui.login import *
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation,pyqtSignal
from PyQt5.QtGui import QMouseEvent, QCursor
from PyQt5.QtWidgets import *
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem,QTableView
from PyQt5.uic import loadUi
from src.pyqtgraph_pyqt import MainWindow

class ExcelReader(QMainWindow):
    signal=pyqtSignal(str)
    def __init__(self):
        super(ExcelReader, self).__init__()
        loadUi("ui/ReadExcel.ui", self)  # Load the UI file
        self.file_path = ""  # To store the file path
        self.df = pd.DataFrame()  # To store the Excel data
        self.flag2=0
        self.table=QTableWidget()
        self.browse_btn.clicked.connect(self.browse_file)
        self.read_btn.clicked.connect(self.read_excel)

    def browse_file(self):
        """
        Open a file dialog to browse Excel files.
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Files (*.*)")
        if file_name:
            self.file_path = file_name
            self.file_path_line_edit.setText(self.file_path)
    def read_excel(self):
        """
        Read the Excel file using Pandas and display the data in the table widget.
        """
        if not self.file_path:
            QMessageBox.critical(self, "Error", "Please select an  file to read.")
            return
        try:
            try:
                self.df = pd.read_excel(self.file_path)
            except:
                self.df=pd.read_csv(self.file_path)

            self.table_widget.setRowCount(self.df.shape[0])
            self.table_widget.setColumnCount(self.df.shape[1])
            self.table_widget.setHorizontalHeaderLabels(self.df.columns)
            for i in range(self.df.shape[0]):
                for j in range(self.df.shape[1]):
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))

            self.signal.emit(self.file_path)
            print("读取完成")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while reading  file.\n\n{e}")

class TabDemo(QTabWidget):
    def __init__(self, parent=None):
        super(TabDemo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.selectcol=[]
        self.msg=""
        self.data=pd.DataFrame()
        self.table1=QTableWidget()
        self.tableWidget = QTableWidget()
        self.tableWidget1 = QTableWidget()
        self.tableWidget1.doubleClicked.connect(self.double_value)
        self.tableWidget1.horizontalHeader().sectionClicked.connect(self.headleHeaderClicked)

        self.read1=ExcelReader()
        self.read1.signal.connect(self.getdata)
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.tab1UI()

        self.setWindowTitle("数据分析")
        self.resize(1000,700)
        self.move(500,0)
    def getdata(self,msg):
        self.msg=msg
        self.tab2UI()
        self.tab3UI()

    def headleHeaderClicked(self, columnIndex):
        item = self.tableWidget1.horizontalHeaderItem(columnIndex)
        if item:
            #print("表头索引", columnIndex)
            print("表头内容", item.text())
            self.selectcol.append(item.text())

    def double_value(self):
        for i in self.tableWidget1.selectedItems():
            print(i.row(), i.column(), i.text())
    def tab1UI(self):
        conLayout1 = QHBoxLayout()
        conLayout1.addWidget(self.read1)
        self.tab1.setLayout(conLayout1)
        print("tab1")
    def tab2UI(self):

        print("文件路径",self.msg)
        conLayout = QHBoxLayout()
        try:
            self.data = pd.read_csv(self.msg)
        except:
            self.data=pd.read_excel(self.msg)
        print("表格规格",self.data.shape)

        self.tableWidget1.setRowCount(self.data.shape[0])
        self.tableWidget1.setColumnCount(self.data.shape[1])
        self.tableWidget1.setHorizontalHeaderLabels(list(self.data.columns))
        conLayout.addWidget(self.tableWidget1)
        self.list1 = []
        self.count = 0
        for index, row in self.data.iterrows():
            for j in row:
                self.list1.append(j)
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                newItem = QTableWidgetItem(str(self.list1[self.count]))
                self.tableWidget1.setItem(i, j, newItem)
                # print(self.list1[self.count])
                # self.tableWidget.setItem(i, j, int(self.list1[self.count]))
                self.count += 1
        # Qt.DescendingOrder 降序
        # Qt.AscendingOrder 升序
        self.tableWidget.sortItems(2, Qt.DescendingOrder)
        # self.setLayout(conLayout)
        self.tab2.setLayout(conLayout)
        print("tab2")

    def tab3UI(self):
        #print(self.selectcol)
        try:
            self.data = pd.read_csv(self.msg)
        except:
            self.data=pd.read_excel(self.msg)

        conLayout3 = QHBoxLayout()
        win1=MainWindow()
        win1.data3=self.data
        win1.col=self.selectcol
        conLayout3.addWidget(win1)
        self.tab3.setLayout(conLayout3)




        print("tab3")

class LoginWindows(QMainWindow, Ui_MainWindow):
    mc = MySQLConnect.MysqlConnect()
    flag=0
    def __init__(self, parent=None):
        super(LoginWindows, self).__init__(parent)

        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.close_pushButton.clicked.connect(self.close)
        self.hidden_pushButton.clicked.connect(self.showMinimized)
        self.login_pushButton.clicked.connect(self.onLoginButtonClick)
        self.signUp_pushButton.clicked.connect(self.onSignUpButtonClick)

    # 窗口拖动
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    # 提示框
    def showMsgBox(self, msg):
        TipBox = QMessageBox(self.widget)
        TipBox.setText(msg)
        TipBox.setWindowFlags(
            TipBox.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowStaysOnTopHint)
        # TipBox.setStandardButtons(QMessageBox.NoButton)
        TipBox.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        TipBox.show()
        # 创建动画
        animation = QPropertyAnimation(TipBox, b"windowOpacity", self)
        animation.setStartValue(0.5)
        animation.setEndValue(1)
        animation.setDuration(500)

        # 启动动画
        animation.start()

        QTimer.singleShot(800, TipBox.close)
        pass

    # 登录按钮逻辑
    def onLoginButtonClick(self):
        userNum = self.user_lineEdit.text()
        userPassword=self.password_lineEdit.text()
        if (userNum!='') & (userPassword!=''):
           res = self.mc.selectOneByOne('user','user_num',userNum)
           print(res)
           if len(res) > 0:
               if res[0][1] == userPassword:
                   self.showMsgBox("登录成功")
                   self.close()
                   self.flag=1
                   self.tab = TabDemo()
                   self.tab.show()
                   # 后续操作...

               else:
                   self.showMsgBox("账号或密码错误")
           else:
               self.showMsgBox("无此账号")
        else:
            self.showMsgBox("请输入信息")
        #pass

    # 注册按钮逻辑
    def onSignUpButtonClick(self):
        userNum = self.user_lineEdit.text()
        userPassword = self.password_lineEdit.text()
        if (userNum != '') & (userPassword != ''):
            try:
                res = self.mc.insertUser(userNum,userPassword)
                if res:
                    self.showMsgBox("注册成功")
                else:
                    self.showMsgBox("注册失败!错误!")
            except Exception as e:
                if e.args[0] == 1062:
                    self.showMsgBox("注册失败,账号已存在")
                print("insertSQL:",e)
        else:
            self.showMsgBox("请输入信息")
        pass
    def getflag(self):
        return self.flag
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = LoginWindows()
    mywin.show()
    sys.exit(app.exec_())


