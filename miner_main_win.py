import sys
import scraper
from PyQt4 import QtGui, uic
from PyQt4.QtCore import SIGNAL

qtCreatorFile = "miner_main_win.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.searchButtonClicked)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.searchButtonClicked)
        
    def searchButtonClicked(self):
        site = self.lineEdit.text()
        source = scraper.findTheLinks(site)
        self.textEdit.setText(source)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
    
