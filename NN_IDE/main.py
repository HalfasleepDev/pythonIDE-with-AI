########################################################################
## NN_IDE
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
from PySide6 import QtWidgets as qtw
########################################################################
# IMPORT GUI FILE
from ui_interface import Ui_MainWindow

########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################



########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        #self = QMainWindow class
        #self.ui = Ui_MainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        loadJsonStyle(self, self.ui)

        # Use this to specify your json file(s) path/name
        # loadJsonStyle(self, self.ui, jsonFiles = {
        #     "mystyle.json", "style.json"
        #     }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()

        # Expand centerMenuContainer
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu() & self.ui.minimizedMenuContainer.collapseMenu())
        self.ui.searchBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu() & self.ui.minimizedMenuContainer.collapseMenu())
        self.ui.fileBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu() & self.ui.minimizedMenuContainer.collapseMenu())
        self.ui.aiBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu() & self.ui.minimizedMenuContainer.collapseMenu())
            
        # Minimize centerMenuContainer
        self.ui.minCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu() & self.ui.minimizedMenuContainer.expandMenu())
        self.ui.maxCenterMenuBtn.clicked.connect(lambda: self.ui.minimizedMenuContainer.collapseMenu() & self.ui.centerMenuContainer.expandMenu())

        # Expand rightMenuContainer
        self.ui.actionOpen_Terminal.triggered.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.actionOpen_Monitor.triggered.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        # Minimize rightMenuContainer
        self.ui.minRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu() & self.ui.minRightMenuContainer.expandMenu())
        self.ui.maxRightMenuBtn.clicked.connect(lambda: self.ui.minRightMenuContainer.collapseMenu() & self.ui.rightMenuContainer.expandMenu())
        # Close rightMenuContainer
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())
        self.ui.closeMinRightMenuBtn.clicked.connect(lambda: self.ui.minRightMenuContainer.collapseMenu())

        # Open Editor Page
        self.ui.actionOpen_Editor.triggered.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.page_16))

        # View options page
        self.ui.viewOptionsBox.currentIndexChanged.connect(self.indexChanged)

        # Close all right menu
        self.ui.homeBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu() & self.ui.minimizedMenuContainer.collapseMenu())

    # Changing the View Options
    def indexChanged(self, index):
        match index:
            case 0:
                self.ui.terminalPages.setCurrentWidget(self.ui.page_11)
                self.ui.minTerminalPages.setCurrentWidget(self.ui.page_10)
            case 1:
                self.ui.terminalPages.setCurrentWidget(self.ui.page_12)
                self.ui.minTerminalPages.setCurrentWidget(self.ui.page_14)
            case 2:
                self.ui.terminalPages.setCurrentWidget(self.ui.page_13)
                self.ui.minTerminalPages.setCurrentWidget(self.ui.page_9)
            case _:
                self.ui.terminalPages.setCurrentWidget(self.ui.page_11)
                self.ui.minTerminalPages.setCurrentWidget(self.ui.page_10)

    def checkButtonGroup(self):
        btn = self.sender()
        group = btn.group
        groupBtns = getattr(self, "group_btns_"+str(group))
        active = getattr(self, "group_active_"+str(group))
        notActive = getattr(self, "group_not_active_"+str(group))

        for x in groupBtns:
            if not x == btn:
                x.setStyleSheet(notActive)
                x.active = False

        btn.setStyleSheet(active)
        btn.active = True
########################################################################
## EXECUTE APP
########################################################################

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

########################################################################
## END===>
########################################################################  
