import sys
import traceback
from SagarUI import Ui_FinalUI 
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import Jeeva
import os

class MainThread (QThread):

        def __init__(self):
            super(MainThread,self).__init__()
        
        def run (self):
            Jeeva.task_Gui()

startExe = MainThread()

class Gui_start(QMainWindow):


        def __init__(self):

            super().__init__()
            self. gui=Ui_FinalUI()
            self.gui.setupUi(self)

            self.gui.start_push.clicked.connect(self.startTask)
            self.gui.Exit_push.clicked.connect(self.close)
            
        def startTask(self):
            self.gui.label1 = QtGui.QMovie("C://Users//Pradeep Mishra//output//Jeeva_materials//jeeva.png")
            self.gui.siri_label.setMovie(self.gui.label1)
            self.gui.label1.start()
            startExe.start() 
            
            self.gui.label2 = QtGui.QMovie("C://Users//Pradeep Mishra//output//Jeeva_materials//middle.gif")
            self.gui.recognition_label.setMovie(self.gui.label2)
            self.gui.label2.start()
            startExe.start() 

            timer = QTimer(self)
            timer.timeout.connect(self.showTimeLive)
            timer.start(999)
            startExe.start()
        
        def showTimeLive (self):
            t_ime = QTime.currentTime()
            time_ = t_ime.toString()
            d_ate = QDate.currentDate()
            date_ = d_ate.toString()
            label_time="Time:\n"+ time_
            label_date="Date:\n"+ date_
    
            

            self.gui.Time_text.setText(label_time)
            self.gui.Date_text.setText(label_date)


import sys
GuiApp = QApplication(sys.argv)
JeevaUI=Gui_start()
os. system('cls')
JeevaUI.show()
try:
    sys.exit(GuiApp.exec_())
except Exception as error:
    traceback.print_exc()


        