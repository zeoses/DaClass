import pandas as pd
from PySide2 import QtCore, QtWidgets, QtGui
import sys
import Student
import pandas as pd


global lstStudent
lstStudent = list()

class parent(QtWidgets.QWidget):


    def init_ui(self, windoName):
        self.center()
        self.setWindowTitle(windoName)
        
        

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


class NewStdWindow(parent):

    def __init__(self, id=0):
        super().__init__()
        self.Base_UI()
        self.ID = id

    def Base_UI(self):
        self.init_ui("New Insert Studet")
        self.lblID = QtWidgets.QLabel()
        self.lblID.setText('ID : ' )
        self.lblID.setStyleSheet("font-size: 12px;")

        self.ledID = QtWidgets.QSpinBox()
        self.ledID.setValue(len(lstStudent) +1)
        self.ledID.setReadOnly(True)
        
        

        self.lblName = QtWidgets.QLabel()
        self.lblName.setText('Name : ' )
        self.lblName.setStyleSheet("font-size: 12px;")

        self.ledName = QtWidgets.QLineEdit()
        
        self.lblFamily = QtWidgets.QLabel()
        self.lblFamily.setText('Family : ' )
        self.lblFamily.setStyleSheet("font-size: 12px;")

        self.ledFamily = QtWidgets.QLineEdit()

        self.lblGrad = QtWidgets.QLabel()
        self.lblGrad.setText('Grad : ' )
        self.lblGrad.setStyleSheet("font-size: 12px;")

        self.ledGrad = QtWidgets.QLineEdit()

        #self.grbScore = QGroupBox('Score of Course : ')

        self.lblMath = QtWidgets.QLabel()
        self.lblMath.setText('Math : ' )
        self.lblMath.setStyleSheet("font-size: 12px;")

        self.ledMath = QtWidgets.QDoubleSpinBox()
        self.ledMath.setMaximum(20)
        self.ledMath.setMinimum(0)

        self.lblScince = QtWidgets.QLabel()
        self.lblScince.setText('Scince : ' )
        self.lblScince.setStyleSheet("font-size: 12px;")

        self.ledScince = QtWidgets.QDoubleSpinBox()
        self.ledScince.setMaximum(20)
        self.ledScince.setMinimum(0)


        self.lblAlghebra = QtWidgets.QLabel()
        self.lblAlghebra.setText('Algebra : ' )
        self.lblAlghebra.setStyleSheet("font-size: 12px;")

        self.ledAlghebra = QtWidgets.QDoubleSpinBox()
        self.ledAlghebra.setMaximum(20)
        self.ledAlghebra.setMinimum(0)

        self.lblComputer = QtWidgets.QLabel()
        self.lblComputer.setText('Computer : ' )
        self.lblComputer.setStyleSheet("font-size: 12px;") 

        self.ledComputer = QtWidgets.QDoubleSpinBox()
        self.ledComputer.setMaximum(20)
        self.ledComputer.setMinimum(0)

        self.grdScore = QtWidgets.QGridLayout()
        self.grdScore.setSpacing(4)

        self.grdStd = QtWidgets.QGridLayout()
        self.grdStd.setSpacing(5)

        self.grdScore.addWidget(self.lblMath, 1, 0)
        self.grdScore.addWidget(self.ledMath, 1, 1)
        
        self.grdScore.addWidget(self.lblScince, 2, 0)
        self.grdScore.addWidget(self.ledScince, 2, 1)

        self.grdScore.addWidget(self.lblAlghebra, 3, 0)
        self.grdScore.addWidget(self.ledAlghebra, 3, 1)

        self.grdScore.addWidget(self.lblComputer, 4, 0)
        self.grdScore.addWidget(self.ledComputer, 4, 1)

        self.grdbtn = QtWidgets.QGridLayout()
        self.grdbtn.setSpacing(1)


        self.btnSave = QtWidgets.QPushButton("Save")
        self.btnSave.clicked.connect(self.SaveStd)

        self.btnCancel = QtWidgets.QPushButton("Cancel")
        self.btnCancel.clicked.connect(self.Cancel)

        self.grdbtn.addWidget(self.btnSave, 1, 0)
        self.grdbtn.addWidget(self.btnCancel, 1, 1)




        #self.grbScore.setLayout(self.grbScore)
        
        self.grdStd.addWidget(self.lblID, 0, 0)
        self.grdStd.addWidget(self.ledID, 0, 1)

        self.grdStd.addWidget(self.lblName, 1, 0)
        self.grdStd.addWidget(self.ledName, 1, 1)
        
        self.grdStd.addWidget(self.lblFamily, 2, 0)
        self.grdStd.addWidget(self.ledFamily, 2, 1)

        self.grdStd.addWidget(self.lblGrad, 3, 0)
        self.grdStd.addWidget(self.ledGrad, 3, 1)

        self.grdStd.addLayout(self.grdScore, 4, 1)

        self.grdStd.addLayout(self.grdbtn, 5, 2)



        self.setLayout(self.grdStd)

        if id!= 0:
            pass


    def SaveStd(self):

        #id = self.ledID.text()
        name = self.ledName.text() 
        family = self.ledFamily.text()
        grade = self.ledGrad.text()

        math = float(self.ledMath.text())
        algebra = float(self.ledAlghebra.text())
        scince = float(self.ledScince.text())
        computer = float(self.ledComputer.text())
        std = Student.Student(name, family, grade, math, algebra, scince,computer)
        
        
        # reply = QtGui.QMessageBox.ok .question(self, 'Save Message',
        #     "New student succussfuly insert.", QtGui.QMessageBox.Yes | 
        #     QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        # if reply == QtGui.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()   

        lstStudent.append(std)
        

        self.close()

    def Cancel(self):
        self.close()
        
class EditWindow(parent):
    global df
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List of Student")

        self.edit = QtWidgets.QLineEdit()
        self.edit.returnPressed.connect(self.magic)

        

        self.result = QtWidgets.QPlainTextEdit()
        self.result.setReadOnly(True)
        
        self.button = QtWidgets.QPushButton("Edit")

        self.lblId = QtWidgets.QLabel('ID : ')
        self.lblId.setStyleSheet("font-size: 12px;")

        self.grid2 = QtWidgets.QGridLayout()
        self.grid2.setSpacing(1)

        self.grid2.addWidget(self.lblId, 1,0)
        self.grid2.addWidget(self.edit, 1,1)

        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(6)

        self.grid.addLayout(self.grid2, 1, 0)
        self.grid.addWidget(self.button, 1, 1)
        
        
        

        self.grid.addWidget(self.result, 2, 0)

        self.button.clicked.connect(self.magic) 

        self.setLayout(self.grid)

        dictoFstudent = [vars(a) for a in lst]
        df = pd.DataFrame(lstStudent)
        self.result.setPlainText(df.to_string())
    def magic(self):
        ID = self.edit.text()

        if len(lstStudent)>= ID:
            self.newStd = NewStdWindow(ID)
            self.newStd.setFixedSize(600, 300)
            self.newStd.show()


class MainWindow(parent):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui("Main Window")
        self.show()

        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(4)
        # self.grid.setAlignment(QtCore.Qt.AlignCenter)
        self.grid.setHorizontalSpacing(30)
        self.grid.setVerticalSpacing(30)


        self.btnNew = QtWidgets.QPushButton("  New Student")
        self.btnNew.setIcon(QtGui.QPixmap('media/student.png'))
        self.btnNew.setIconSize(QtCore.QSize(120, 120))
        self.btnNew.clicked.connect(self.OpenNewStd)


        self.btnViewStd = QtWidgets.QPushButton("  Viwe/Edit Student")
        self.btnViewStd.setIcon(QtGui.QPixmap('media/class.png'))
        self.btnViewStd.setIconSize(QtCore.QSize(120, 120))
        self.btnViewStd.clicked.connect(self.EditViewStd)

        self.btnInsertCourseScore = QtWidgets.QPushButton("  Export Data")
        self.btnInsertCourseScore.setIcon(QtGui.QPixmap('media/study.png'))
        self.btnInsertCourseScore.setIconSize(QtCore.QSize(120, 120))

        self.btnRepo = QtWidgets.QPushButton("  Report")
        self.btnRepo.setIcon(QtGui.QPixmap('media/maths.png'))
        self.btnRepo.setIconSize(QtCore.QSize(120, 120))

        self.grid.addWidget(self.btnNew, 1, 0)
        self.grid.addWidget(self.btnViewStd, 1, 1)
        self.grid.addWidget(self.btnInsertCourseScore, 2, 1)
        self.grid.addWidget(self.btnRepo, 2, 0)
        self.setLayout(self.grid)

        


    def OpenNewStd(self):
        #self.hide()
        self.newStd = NewStdWindow()
        self.newStd.setFixedSize(600, 300)
        self.newStd.show()

    def EditViewStd(self):
        self.editStd = EditWindow()
        self.editStd.setFixedSize(600, 300)
        self.editStd.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MainWindow()
    

    sys.exit(app.exec_())