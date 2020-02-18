import pandas as pd
from PySide2 import QtCore, QtWidgets, QtGui
import sys
import Student
import pandas as pd
import os


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

    
    def __init__(self, ID=0):
        super().__init__()
        self.ID = int(ID) - 1
        self.Base_UI()
        
        

    def Base_UI(self):
        if self.ID ==-1:
            self.init_ui("New Insert Studet")
        else:
            self.init_ui("Edit Studet")

        self.lblID = QtWidgets.QLabel()
        self.lblID.setText('ID : ' )
        self.lblID.setStyleSheet("font-size: 12px;")

        self.ledID = QtWidgets.QSpinBox()
        if self.ID == - 1:
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

        if self.ID != -1:
            self.ledID.setValue(int(lstStudent[self.ID].id))
            self.ledName.setText(lstStudent[self.ID].name)
            self.ledFamily.setText(lstStudent[self.ID].family)
            self.ledGrad.setText(lstStudent[self.ID].grade)

            self.ledAlghebra.setValue(lstStudent[self.ID].alghebra)
            self.ledComputer.setValue(lstStudent[self.ID].computer)
            self.ledMath.setValue(lstStudent[self.ID].math)
            self.ledScince.setValue(lstStudent[self.ID].scince)


    def SaveStd(self):

        if self.ID == -1 :
            id = int(self.ledID.text())
            name = self.ledName.text() 
            family = self.ledFamily.text()
            grade = self.ledGrad.text()

            math = float(self.ledMath.text())
            algebra = float(self.ledAlghebra.text())
            scince = float(self.ledScince.text())
            computer = float(self.ledComputer.text())
            std = Student.Student(id, name, family, grade, math, algebra, scince,computer)
            
            
            # reply = QtGui.QMessageBox.ok .question(self, 'Save Message',
            #     "New student succussfuly insert.", QtGui.QMessageBox.Yes | 
            #     QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            # if reply == QtGui.QMessageBox.Yes:
            #     event.accept()
            # else:
            #     event.ignore()   

            lstStudent.append(std)

        else :
            lstStudent[self.ID].name = self.ledName.text()
            lstStudent[self.ID].family = self.ledFamily.text()
            lstStudent[self.ID].grade = self.ledGrad.text()

            lstStudent[self.ID].alghebra = self.ledAlghebra.text()
            lstStudent[self.ID].computer = self.ledComputer.text()
            lstStudent[self.ID].scince = self.ledScince.text()
            lstStudent[self.ID].math = self.ledMath.text()
            
        

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

        dictoFstudent = [list(vars(a).values()) for a in lstStudent]
        
        df = pd.DataFrame(dictoFstudent, index= None)
        self.result.setPlainText(str(df.to_numpy()))


    def magic(self):
        try :
            ID = self.edit.text()

            if len(lstStudent)>= int(ID):
                self.newStd = NewStdWindow(ID)
                self.newStd.setFixedSize(600, 300)
                self.newStd.center()
                self.newStd.show()

            else :
                mb = QtWidgets.QMessageBox()
                #mb.setIcon(mb.Icon.Error)
                mb.setText("{0}".format('Not exist this ID'))
                mb.setWindowTitle("Error")
                mb.exec_() 
        except :
            mb = QtWidgets.QMessageBox()
            #mb.setIcon(mb.Icon.Error)
            mb.setText("{0}".format('ID is a number '))
            mb.setWindowTitle("Error")
            mb.exec_() 

class ReportWindow(parent):

    def __init__(self):
        super().__init__()

        dictoFstudent = [list(vars(a).values()) for a in lstStudent]
        df = pd.DataFrame(dictoFstudent)
        # print(df)
        studentCont = len(lstStudent)
        print(df.head(10))
        self.lblMath = QtWidgets.QLabel('Math ')
        self.lblMath.setStyleSheet("font-size: 14px; ")

        self.lblMaxMath = QtWidgets.QLabel('Min : '+ str(df.min()[4]))
        self.lblMaxMath.setStyleSheet("font-size: 12px; ")

        self.lblMinMath = QtWidgets.QLabel('Max : '+ str(df.max()[4]))
        self.lblMinMath.setStyleSheet("font-size: 12px; ")

        self.lblAveMath = QtWidgets.QLabel('Average : '+ str(df.mean()[4]))
        self.lblAveMath.setStyleSheet("font-size: 12px; ")

        self.grdMath = QtWidgets.QGridLayout()
        self.grdMath.setSpacing(4)


        self.grdMath.addWidget(self.lblMath, 1, 0)
        self.grdMath.addWidget(self.lblMaxMath, 2, 0)
        self.grdMath.addWidget(self.lblMinMath, 3, 0)
        self.grdMath.addWidget(self.lblAveMath, 4, 0)
        self.grdMath.setMargin(20)

        self.lblAl = QtWidgets.QLabel('Algebra  ')
        self.lblAl.setStyleSheet("font-size: 14px; ")

        self.lblMaxAl = QtWidgets.QLabel('Min : ' + str(df.min()[6]))
        self.lblMaxAl.setStyleSheet("font-size: 12px; " )

        self.lblMinAl  = QtWidgets.QLabel('Max : '+ str(df.max()[6]))
        self.lblMinAl .setStyleSheet("font-size: 12px; ")

        self.lblAveAl = QtWidgets.QLabel('Average :'+ str(df.mean()[6]))
        self.lblAveAl.setStyleSheet("font-size: 12px; ")

        self.grdAl = QtWidgets.QGridLayout()
        self.grdAl.setSpacing(4)


        self.grdAl.addWidget(self.lblAl, 1, 0)
        self.grdAl.addWidget(self.lblMaxAl, 2, 0)
        self.grdAl.addWidget(self.lblMinAl, 3, 0)
        self.grdAl.addWidget(self.lblAveAl, 4, 0)
        self.grdAl.setMargin(20)

        self.lblSci = QtWidgets.QLabel('Science')
        self.lblSci.setStyleSheet("font-size: 14px; ")

        self.lblMaxSci = QtWidgets.QLabel('Min : '+ str(df.min()[5]))
        self.lblMaxSci.setStyleSheet("font-size: 12px; ")

        self.lblMinSci  = QtWidgets.QLabel('Max : '+ str(df.max()[5]))
        self.lblMinSci .setStyleSheet("font-size: 12px; ")

        self.lblAveSci = QtWidgets.QLabel('Average :'+ str(df.mean()[5]))
        self.lblAveSci.setStyleSheet("font-size: 12px; ")

        self.grdSci = QtWidgets.QGridLayout()
        self.grdSci.setSpacing(4)


        self.grdSci.addWidget(self.lblSci, 1, 0)
        self.grdSci.addWidget(self.lblMaxSci, 2, 0)
        self.grdSci.addWidget(self.lblMinSci, 3, 0)
        self.grdSci.addWidget(self.lblAveSci, 4, 0)
        self.grdSci.setMargin(20)

        self.lblCmp = QtWidgets.QLabel('Computer  ')
        self.lblCmp.setStyleSheet("font-size: 14px; ")

        self.lblMaxCmp = QtWidgets.QLabel('Min : '+ str(df.min()[7]))
        self.lblMaxCmp.setStyleSheet("font-size: 12px; ")

        self.lblMinCmp  = QtWidgets.QLabel('Max : '+ str(df.max()[7]))
        self.lblMinCmp .setStyleSheet("font-size: 12px; ")

        self.lblAveCmp = QtWidgets.QLabel('Average :'+ str(df.mean()[7]))
        self.lblAveCmp.setStyleSheet("font-size: 12px; ")

        self.grdCmp = QtWidgets.QGridLayout()
        self.grdCmp.setSpacing(4)


        self.grdCmp.addWidget(self.lblCmp, 1, 0)
        self.grdCmp.addWidget(self.lblMaxCmp, 2, 0)
        self.grdCmp.addWidget(self.lblMinCmp, 3, 0)
        self.grdCmp.addWidget(self.lblAveCmp, 4, 0)
        self.grdCmp.setMargin(20)


        self.grdBase = QtWidgets.QGridLayout()
        self.grdBase.setSpacing(3)

        self.grdBase.addLayout(self.grdMath, 1, 0)
        self.grdBase.addLayout(self.grdAl, 1, 1)
        self.grdBase.addLayout(self.grdSci, 2, 0)
        self.grdBase.addLayout(self.grdCmp, 2, 1)

        self.setLayout(self.grdBase)



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

        self.btnExport = QtWidgets.QPushButton("  Export Data")
        self.btnExport.setIcon(QtGui.QPixmap('media/study.png'))
        self.btnExport.setIconSize(QtCore.QSize(120, 120))
        self.btnExport.clicked.connect(self.ExportWindow)


        self.btnRepo = QtWidgets.QPushButton("  Report")
        self.btnRepo.setIcon(QtGui.QPixmap('media/maths.png'))
        self.btnRepo.setIconSize(QtCore.QSize(120, 120))
        self.btnRepo.clicked.connect(self.RepotWindoCourse)

        self.grid.addWidget(self.btnNew, 1, 0)
        self.grid.addWidget(self.btnViewStd, 1, 1)
        self.grid.addWidget(self.btnExport, 2, 1)
        self.grid.addWidget(self.btnRepo, 2, 0)
        self.setLayout(self.grid)

        


    def OpenNewStd(self):
        #self.hide()
        self.newStd = NewStdWindow()
        self.newStd.setFixedSize(600, 300)
        self.newStd.center()
        self.newStd.show()

    def EditViewStd(self):
        self.editStd = EditWindow()
        self.editStd.setFixedSize(600, 300)
        self.editStd.center()
        self.editStd.show()

    def RepotWindoCourse(self):
        if len(lstStudent)>0:
            self.repoWindow = ReportWindow()
            self.repoWindow.setFixedSize(300, 300)
            self.repoWindow.center()
            self.repoWindow.show()
        else:
            mb = QtWidgets.QMessageBox()
            #mb.setIcon(mb.Icon.Error)
            mb.setText("{0}".format('First Insert a Student'))
            mb.setWindowTitle("Error")
            mb.exec_() 
    
    def ExportWindow(self):
        # self.exportWindow = ExportWindow()
        # self.exportWindow.setFixedSize(200, 200)
        # self.exportWindow.center()
        # self.exportWindow.show()
        
        fname = QtWidgets.QFileDialog.getSaveFileName(caption='Export File', options=QtWidgets.QFileDialog.DontUseNativeDialog, filter="csv file (*.csv)")
        dictoFstudent = [list(vars(a).values()) for a in lstStudent]
        df = pd.DataFrame(dictoFstudent)
        if not os.path.isfile(fname[0]):
            f = open(fname[0]+'.csv', 'x')
            f.write(df.to_csv())
            f.close()
        else:
            f = open(fname[0], 'w')
            f.write(df.to_csv())
            f.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MainWindow()
    

    sys.exit(app.exec_())