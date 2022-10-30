from concurrent.futures import thread
import threading
from qt import *
import sys
from main import *
from threading import *




def Start_clicked ():
    
    thread1=Thread(target=myprogStart("asdad",1))
    thread1.start()

def Cancel_clicked():
    sys.exit(app.exec_())

app = QtWidgets.QApplication(sys.argv)
whatsDirect = QtWidgets.QDialog()
ui = Ui_whatsDirect()
ui.setupUi(whatsDirect)
ui.StartButton.clicked.connect(Start_clicked)
ui.CancelButton.clicked.connect(Cancel_clicked)
whatsDirect.show()

sys.exit(app.exec_())