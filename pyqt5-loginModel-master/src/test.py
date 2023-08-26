import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt5.uic import loadUi


class ExcelReader(QMainWindow):
    def __init__(self):
        super(ExcelReader, self).__init__()
        loadUi("ReadExcel.ui", self)  # Load the UI file
        self.file_path = ""  # To store the file path
        self.df = pd.DataFrame()  # To store the Excel data
        self.browse_btn.clicked.connect(self.browse_file)
        self.read_btn.clicked.connect(self.read_excel)

    def browse_file(self):
        """
        Open a file dialog to browse Excel files.
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", " Files (*.*)")
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
            self.df = pd.read_excel(self.file_path)
            self.table_widget.setRowCount(self.df.shape[0])
            self.table_widget.setColumnCount(self.df.shape[1])
            self.table_widget.setHorizontalHeaderLabels(self.df.columns)
            for i in range(self.df.shape[0]):
                for j in range(self.df.shape[1]):
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while reading  file.\n\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExcelReader()
    window.show()
    sys.exit(app.exec_())

