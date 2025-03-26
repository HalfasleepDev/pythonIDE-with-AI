
import sys
from MainWindow import Ui_MainWindow
from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MainWindow(Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        index = self.ui.TextToText.currentIndex()
    
        print(self.AutoCompletionLengthConfig())

    def AutoCompletionLengthConfig(self):
        index = self.ui.TextToText.currentIndex()
        return index


    
########################################################################
## END===>
######################################################################## 
