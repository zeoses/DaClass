import pandas as pd
from PySide2 import QtCore, QtWidgets, QtGui
import sys



df = pd.read_csv("Data/500.csv", error_bad_lines=False, sep='\t', header=None)

class MyWidget(QtWidgets.QWidget):

    global df
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dictionary EN 2 FA")

        self.edit = QtWidgets.QLineEdit()
        self.edit.returnPressed.connect(self.magic)

        

        self.result = QtWidgets.QPlainTextEdit()
        self.result.setReadOnly(True)
        
        self.button = QtWidgets.QPushButton("Search")
        self.coutLabe = QtWidgets.QLabel()
        self.coutLabe.setStyleSheet("font-size: 12px;")

        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(6)

        self.grid.addWidget(self.edit, 1, 0)
        self.grid.addWidget(self.button, 1, 1)
        
        
        self.grid.addWidget(self.coutLabe, 2, 0)

        self.grid.addWidget(self.result, 3, 0)

        self.button.clicked.connect(self.magic) 

        self.setLayout(self.grid)

   
        

    def magic(self):

        keySearch = self.edit.text()   
        machResult = df[df[0].str.match(keySearch)]
        lenof = str(len(machResult))
        self.coutLabe.setText('Result : ' + lenof)
        if lenof == 0:
            self.result.setPlainText("")
        else:
            self.result.setPlainText(machResult.to_string())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())