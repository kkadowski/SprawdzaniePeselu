# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pesel.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

class Ui_MainWindow(object):
    
    
    
    def setupUi(self, MainWindow):
        self.wagi = [1,3,7,9,1,3,7,9,1,3]
        self.dni = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 365)
        MainWindow.setMinimumSize(QtCore.QSize(450, 280))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 454, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Srawdzanie numeru PESEL"))
        self.pushButton.setText(_translate("MainWindow", "Sprwadź Pesel"))
        self.pushButton_2.setText(_translate("MainWindow", "Zakończ"))
        self.pushButton.clicked.connect(self.sprawdzanie)

    def sprawdzanie(self):
        pesel = self.lineEdit.text() 
        if len(pesel)!= 11:
            self.listWidget.addItem("Błędna długość Peselu!")
        else:
            self.listWidget.clear()
            
            suma = 0
            for p in range(len(pesel)-1):
                suma += int(pesel[p]) * self.wagi[p]
            
            m = 10-(suma % 10)
            
            if (m) == int(pesel[10]):
                self.listWidget.addItem("Pesel poprawny.")
                p_year = pesel[:2]
                p_month = pesel[2:4]
                p_day = pesel[4:6]
                
                if pesel[2] in ['8', '9']:
                    year = '18' + p_year
                elif pesel[2] in ['0','1']:
                    year = '19' + p_year
                elif pesel[2] in ['2','3']:
                    year = '20' + p_year
                elif pesel[2] in ['4','5']:
                    year = '21' + p_year
                elif pesel[2] in ['6','7']:
                    year = '22' + p_year
                
                if int(pesel[9])%2 == 0:
                    k_m = "kobieta"
                else:
                    k_m = "mężczyzna"
                
                if int(pesel[2]) not in [0, 1]:
                    if int(pesel[2]) in [8, 2, 4, 6]:
                        a_m = '0'+ pesel[3]
                    elif int(pesel[2]) in [9, 3, 5, 7]:
                        a_m = '1'+ pesel[3]
                    data = datetime(year = int(year), month=int(a_m), day=int(p_day))
                    a_month = data.toordinal() % 7
                else:
                    data = datetime(year = int(year), month=int(p_month), day=int(p_day))
                    a_month = data.toordinal() % 7
            
                dt = self.dni[a_month-1]
                
                
                
                self.listWidget.addItem("Płeć: " + k_m)
                self.listWidget.addItem(f"Data urodzenia: {year}-{p_month}-{p_day}")
                self.listWidget.addItem(f"Dzień tygodnia daty urodzenia: {dt}")
            
            else:
                self.listWidget.addItem("Pesel niepoprawny.")
            
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

