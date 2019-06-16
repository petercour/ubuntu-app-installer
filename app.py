# ubuntu app installer demo (apt-get)
# https://pythonbasics.org/pyqt/

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
import sys
import os
 
class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('gui.ui', self)
        self.pushButtonInstall.clicked.connect(self.onClick)
        
    def onClick(self):
        if len(self.lineEditName.text()) < 1:
            QMessageBox.critical(self, "Install", "Install")
        else:
            os.system("sudo apt-get install " + self.lineEditName.text())
            
app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
