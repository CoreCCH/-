###
# Main file connect function and layout

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTabWidget, QApplication, QWidget
import manual
import sys
import Ui
import qdarkstyle
import flag

Flag = flag.Flag()

class Main(QTabWidget, Ui.Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent) # 調用父類把子類對象轉為父類對象
        # 調用介面
        self.setupUi(self)
        self.addTab(Page_Testing(),"Testing")
        self.addTab(Page_Manual(),"Manual")

class Page_Testing(QWidget, Ui.Page_Testing):
    def __init__(self, parent=None):
        super(Page_Testing, self).__init__(parent) # 調用父類把子類對象轉為父類對象
        self.setupUi(self)
        
class Page_Manual(QWidget, Ui.Page_Manual):
    def __init__(self, parent=None):
        super(Page_Manual, self).__init__(parent) # 調用父類把子類對象轉為父類對象
        self.setupUi(self)
        self.flag = Flag  
        self.Connecting()
    def Connecting(self):
        self.btnConveyerForward.clicked.connect(lambda: manual.ClickConveyerForward(self).action())
        self.btnConveyerBackward.clicked.connect(lambda: manual.ClickConveyerBackward(self).action())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainFrame = Main()
    mainFrame.showFullScreen()
    sys.exit(app.exec_())