########################################################################
## NN_IDE
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
#from PyQt5 import QtWidgets as qtw
from PyQt6 import QtWidgets, uic
#from PySide6.Qsci import *
from PyQt6.Qsci import *
from PyQt6.QtCore import *
#from PyQt6.QtGui import *
from PyQt6.QtWidgets import QFileDialog
import traceback
from pathlib import Path
from editor import Editor
from editorMsg import Editor as EditorMsg
from fuzzySearcher import SearchItem, SearchWorker
from message import Message
from fileManager import FileManager
sys.path.insert(0, '/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff')
from chat import getResponse
import psutil
import GPUtil

########################################################################
# IMPORT GUI FILE
#from ui_interface import Ui_MainWindow
from MainWindow import Ui_MainWindow
from splashScreen import Ui_SplashScreen
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
from Custom_Widgets.RoundProgressBar import *
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################
counter = 0
jumper = 10

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        #self.fn(*self.args, **self.kwargs)
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.currentFile = None
        self.setUpMemu()
        
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

        self.threadpool = QThreadPool()

        self.setUpStatusBar()

        self.ui.mainPages.setCurrentWidget(self.ui.page_15)
        #For terminal
        self.terminalProcess = QProcess(self)
        self.lineEditIndication = ""
        
        # Expand centerMenuContainer
        self.ui.settingsBtn.clicked.connect(self.expandOrCollapseLeft)
        self.ui.searchBtn.clicked.connect(self.expandOrCollapseLeft)
        self.ui.fileBtn.clicked.connect(self.expandOrCollapseLeft)
        self.ui.aiBtn.clicked.connect(self.expandOrCollapseLeft)
            
        # Minimize centerMenuContainer
        self.ui.minCenterMenuBtn.clicked.connect(self.minMenuLeft)
        self.ui.maxCenterMenuBtn.clicked.connect(self.maxMenuLeft)

        #lable change centerMenuContainer
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuLabels.setCurrentWidget(self.ui.page_21))
        self.ui.searchBtn.clicked.connect(lambda: self.ui.centerMenuLabels.setCurrentWidget(self.ui.page_19))
        self.ui.fileBtn.clicked.connect(lambda: self.ui.centerMenuLabels.setCurrentWidget(self.ui.page_18))
        self.ui.aiBtn.clicked.connect(lambda: self.ui.centerMenuLabels.setCurrentWidget(self.ui.page_20))

        # Expand rightMenuContainer
        self.ui.actionOpen_Terminal.triggered.connect(self.openRightMenu)
        self.ui.actionOpen_Monitor.triggered.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        # Minimize rightMenuContainer
        self.ui.minRightMenuBtn.clicked.connect(self.minMenuRight)
        # Maximize rightMenuContainer
        self.ui.maxRightMenuBtn.clicked.connect(self.maxMenuRight)
        # Close rightMenuContainer
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())
        self.ui.closeMinRightMenuBtn.clicked.connect(lambda: self.ui.minRightMenuContainer.collapseMenu())

        # Open Editor Page
        self.ui.actionOpen_Editor.triggered.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.page_16))

        # View options page
        self.ui.viewOptionsBox.currentIndexChanged.connect(self.indexChanged)

        # Close all right menu
        self.ui.homeBtn.clicked.connect(self.closeAllRightMenu)

        #Close performance monitoring
        #self.ui.openPerformanceMonitorBtn.setCheckable(True)
        self.ui.openPerformanceMonitorBtn.clicked.connect(self.openPerfMon)


        #Tree view
        self.fileManager = FileManager(
            tabView = self.ui.tabWidget,
            setNewTab=self.setNewTab,
            MainWindow=self
        )
        self.treeViewTimer = QTimer()
        self.treeViewTimer.timeout.connect(self.treeViewClicked)
        self.ui.verticalLayout_11.addWidget(self.fileManager)
        self.treeViewTimer.start()
       
        '''self.model = QFileSystemModel()
        self.model.setRootPath(os.getcwd())
        # Filesystem Filters
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)
        #Tree view
        self.treeView = self.ui.treeView
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(os.getcwd()))
        self.ui.treeView.setSelectionMode(QTreeView.SingleSelection)
        self.ui.treeView.setSelectionBehavior(QTreeView.SelectRows)
        self.ui.treeView.setEditTriggers(QTreeView.NoEditTriggers)
        #Context menu
        self.ui.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeView.customContextMenuRequested.connect(self.treeViewContextMenu)
        self.ui.treeView.clicked.connect(self.treeViewClicked)
        #hidding
        self.ui.treeView.setHeaderHidden(True)
        self.ui.treeView.setColumnHidden(1, True)
        self.ui.treeView.setColumnHidden(2, True)
        self.ui.treeView.setColumnHidden(3, True)'''

        #TabWidget
        self.ui.tabWidget.setContentsMargins(0, 0, 0, 0)
        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.setMovable(True)
        self.ui.tabWidget.setDocumentMode(True)
    

        #editorTestWidget
        #self.editor1 = QsciScintilla()
        #self.editor1.setText("Hello\n")
        #self.editor1.append("world")
        #self.editor1.setLexer(None)
        #self.editor1.setUtf8(True)  # Set encoding to UTF-8
        #self.__editor.setFont(self.__myFont)  # Will be overridden by lexer!
        #self.ui.tabWidget.set
        self.font = QtGui.QFont()
        self.font.setPointSize(10)

        self.ui.tabWidget.tabCloseRequested.connect(self.closeTab)

        self.searchWorker = SearchWorker()
        self.searchWorker.finished.connect(self.searchFinished)

        self.ui.lineEdit.textChanged.connect(
            lambda text: self.searchWorker.update(
            text,
            self.model.rootDirectory().absolutePath(),
            self.ui.checkBox.isChecked()
            )
        )

        ################################################################
        # AI Assistant calling
        ################################################################
        # Enter/return
        self.ui.lineEdit_2.keyReleaseEvent = self.enterReturnRelease
        #self.ui.sendBtn.clicked.connect(self.sendMessage)

        # example messages
        self.messages = [
            f"Hi, how are you?",
            f"Hello, how are you today?",
            f"Do you know if it is going to rain today?",
            f"How is your day?",
            f"Do you remember that you owe me $100? Humm..."
        ]
        self.sentence = ''
        self.codeText = ''
        #self.sendByAi()
        #AiChat(self.sentence)
        #print(self.sentence)

        self.messageEditor = self.getEditorMsg() #change 
        self.messageEditor.font.setPointSize(10)
        self.ui.verticalLayout_48.addWidget(self.messageEditor)
        self.ui.addBtn.clicked.connect(lambda: self.ui.centerMenuPages.setCurrentWidget(self.ui.page_22))
        self.ui.backBtn.clicked.connect(lambda: self.ui.centerMenuPages.setCurrentWidget(self.ui.page_2))
        self.ui.sendBtn.clicked.connect(self.printCodeText)
        self.plusNorm = QtGui.QIcon()
        self.plusNotif = QtGui.QIcon()
        self.plusNotif.addPixmap(QtGui.QPixmap(":/icons/Icons/plus_notif.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.plusNorm.addPixmap(QtGui.QPixmap(":/icons/Icons/plus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        
        ################################################################
        #Terminal calling
        ################################################################
        self.ui.terminalInput.keyReleaseEvent = self.enterReturnReleaseTerminal

        self.terminalProcess.readyReadStandardOutput.connect(self.TerminalReadOutput)
        #self.terminalRunCommandButton.clicked.connect(self.run_command) #change to return
        self.terminalProcess.start("cmd.exe")

        ################################################################
        #AI assistant setting min menu
        ################################################################ 
        '''self.ui.TextToText.setEditable(True) # Auto Completion Length config
        self.ui.CodeToCode.setEditable(True) # Auto Doc Length config
        self.ui.Summerize.setEditable(True) # Code Generation Length
        tTTLineEdit = self.ui.TextToText.lineEdit()
        cTCLineEdit = self.ui.CodeToCode.lineEdit()
        summerizeLineEdit = self.ui.Summerize.lineEdit()
        comboFont = QtGui.QFont()
        comboFont.setPointSize(6)
        tTTLineEdit.setFont(comboFont)
        cTCLineEdit.setFont(comboFont)
        summerizeLineEdit.setFont(comboFont)
        tTTLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cTCLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        summerizeLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tTTLineEdit.setReadOnly(True)
        cTCLineEdit.setReadOnly(True)
        summerizeLineEdit.setReadOnly(True)'''

        self.ui.CodeToCode.currentIndexChanged.connect(self.getAiADIndex)
        self.ui.Summerize.currentIndexChanged.connect(self.getAiComGenIndex)
        self.ui.TextToText.currentIndexChanged.connect(self.getAICompIndex)
    
        self.perfTimer = QTimer()
        self.perfTimer.timeout.connect(self.updateCPUPercent)
        self.perfTimer.timeout.connect(self.updateRAMPercent)
        self.perfTimer.timeout.connect(self.updateGPUPercent)
        self.perfTimer.start(1000)

        self.ui.cpuProgress.rpb_setBarStyle('Hybrid1')
        self.ui.ramProgress.rpb_setBarStyle('Hybrid1')
        self.ui.gpuProgress.rpb_setBarStyle('Hybrid1')
        self.ui.memProgress.rpb_setBarStyle('Hybrid1')

    def updateCPUPercent(self):
        cpuPercent = psutil.cpu_percent() * psutil.cpu_count()
        cpuPercentTxt = f"CPU: {cpuPercent:.2f}%"
        self.ui.label_16.setText(cpuPercentTxt)
        self.ui.cpuProgress.rpb_setValue(cpuPercent)
        

    def updateRAMPercent(self):
        ramPercent = psutil.virtual_memory().percent
        ramPercentTxt = f"RAM: {ramPercent:.2f}%"
        self.ui.label_17.setText(ramPercentTxt)
        self.ui.ramProgress.rpb_setValue(ramPercent)
        

    def updateGPUPercent(self):
        GPUs = GPUtil.getGPUs()
        for GPU in GPUs:
            self.ui.gpuProgress.rpb_setValue(int(GPU.load*100))
            self.ui.memProgress.rpb_setValue(int(GPU.memoryUtil*100))

    def setUpStatusBar(self):
        stat = QStatusBar(self)
        stat.setStyleSheet("background-color: #2D2E2E;")
        stat.showMessage("Ready", 3000)
        self.setStatusBar(stat)


    def getAICompIndex(self, index):
        print(index)
        Editor.getAiCompleteIndex(Editor, index)

    def getAiComGenIndex(self, index):
        print(index)
        Editor.getAiCommentGenIndex(Editor, index)
    
    def getAiADIndex(self, index):
        print(index)
        Editor.getAiAutoDocIndex(Editor, index)

    ################################################################
    #Open rightmenu and optimize for performance
    ################################################################
    def openRightMenu(self):
        self.ui.rightMenuContainer.expandMenu()
        #self.terminalProcess.start("cmd.exe")
        #TODO: start and exit for "cmd.exe"
        #TODO: debug and output
    ################################################################
    #Terminal functions
    ################################################################
    def enterReturnReleaseTerminal(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.runTerminalCommand()
            self.ui.terminalInput.setText("")

    def TerminalReadOutput(self):
        stream = QTextStream(self.terminalProcess)
        self.ui.terminalBrowser.append(stream.readAll())
        #put last line in lineEdit
        self.lineEditIndication = self.ui.terminalBrowser.toPlainText()
        self.ui.terminalInput.setPlaceholderText(self.lineEditIndication.splitlines()[-1])

    def runTerminalCommand(self):
        command = self.ui.terminalInput.text() + "\n"
        self.terminalProcess.write(command.encode())
        self.ui.terminalInput.setText("")

    ################################################################
    #Open performance monitor
    ################################################################
    def openPerfMon(self):
        if self.ui.openPerformanceMonitorBtn.isChecked():
            self.ui.widget_2.float = True
            self.ui.widget_2.floatPosition = "bottom-left"
            self.ui.widget_2.expandMenu()
            
        else:
            self.ui.widget_2.collapseMenu()

    ################################################################
    #AI Messages
    ################################################################     
    def printCodeText(self):
        if self.messageEditor.text() != "":
            self.codeText = self.messageEditor.text()
            self.ui.centerMenuPages.setCurrentWidget(self.ui.page_2)
            self.ui.addBtn.setIcon(self.plusNotif)
    
    def enterReturnRelease(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.sentence = self.ui.lineEdit_2.text()
            self.ui.addBtn.setIcon(self.plusNorm)
            self.sendMessage()
            

    def sendMessage(self):
         if self.ui.lineEdit_2.text() != "":
            self.message = Message(self.ui.lineEdit_2.text(), True)
            self.ui.verticalLayout_46.addWidget(self.message, Qt.AlignCenter, Qt.AlignBottom)
            self.ui.lineEdit_2.setText("")

            # SCROLL TO END            
            QTimer.singleShot(10, lambda: self.ui.frame_12.setFixedHeight(self.ui.verticalLayout_46.sizeHint().height()))
            QTimer.singleShot(15, lambda: self.scrollToEnd())

            # SEND USER MESSAGE
            QTimer.singleShot(1000, lambda: self.sendByAiOptim())

    def sendByAi(self):
        self.message = getResponse(self.sentence, self.codeText)
        return self.message

    def sendByAiCreate(self, msg):
        self.message = Message(msg, False)
        self.ui.verticalLayout_46.addWidget(self.message, Qt.AlignCenter, Qt.AlignBottom)
        self.ui.lineEdit_2.setText("")
        self.codeText = ""

        # SCROLL TO END            
        QTimer.singleShot(20, lambda: self.ui.frame_12.setFixedHeight(self.ui.verticalLayout_46.sizeHint().height()))#10 to 20
        QTimer.singleShot(25, lambda: self.scrollToEnd())#changes form 15 to 25

    def sendByAiOptim(self):
        worker = Worker(self.sendByAi)
        worker.signals.result.connect(self.sendByAiCreate)
        worker.signals.finished.connect(self.aiDoneNotif)
        self.threadpool.start(worker)

    def aiDoneNotif(self):
        if self.ui.centerMenuLabels.currentWidget() != self.ui.page_20:
            print("ai done") #TODO: add icons for ai
        

    def scrollToEnd(self):
         # SCROLL TO END
        self.scroll_bar = self.ui.chatMessages.verticalScrollBar()
        self.scroll_bar.setValue(self.scroll_bar.maximum())

    ################################################################
    #search and closing tabs
    ################################################################
    def searchFinished(self, items):
        self.ui.listWidget_2.clear()
        for i in items:
            self.ui.listWidget_2.addItem(i)

    def searchListViewClicked(self, item: SearchItem):
        self.setNewTab(Path(item.fullPath))
        editor: Editor = self.ui.tabWidget.currentWidget()
        editor.setCursorPosition(item.lineno, item.end)
        editor.setFocus()

    def showDialog(self, title, msg) -> int:
            dialog = QMessageBox(self)
            dialog.setFont(self.font)
            dialog.font().setPointSize(14)
            dialog.setWindowTitle(title)
            dialog.setWindowIcon(QIcon(":/icons/Icons/window_close.png"))
            dialog.setText(msg)
            dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dialog.setDefaultButton(QMessageBox.No)
            dialog.setIcon(QMessageBox.Warning)
            return dialog.exec_()

    def closeTab(self, index):
        editor: Editor = self.ui.tabWidget.currentWidget()
        if editor.currentFileChanged:
            dialog = self.showDialog(
                "Close", f"Do you want to save the changes made to {self.currentFile.name}?",
            )
            if dialog == QMessageBox.Yes:
                self.saveFile
            
        self.ui.tabWidget.removeTab(index)
    
    ################################################################
    # Closing and collapsing Menus
    ################################################################
    def expandOrCollapseLeft(self):
        if self.ui.minimizedMenuContainer.expanded == True:
            self.ui.minimizedMenuContainer.collapseMenu()
            self.ui.centerMenuContainer.expandMenu()
        else:
            self.ui.centerMenuContainer.expandMenu()
    
    def minMenuLeft(self):
        self.ui.centerMenuContainer.collapseMenu()
        self.ui.minimizedMenuContainer.expandMenu()

    def maxMenuLeft(self):
        self.ui.minimizedMenuContainer.collapseMenu()
        self.ui.centerMenuContainer.expandMenu()
    
    def minMenuRight(self):
        self.ui.rightMenuContainer.collapseMenu()
        self.ui.minRightMenuContainer.expandMenu()

    def maxMenuRight(self):
        self.ui.minRightMenuContainer.collapseMenu()
        self.ui.rightMenuContainer.expandMenu()

    def closeAllRightMenu(self):
        self.ui.centerMenuContainer.collapseMenu()
        self.ui.minimizedMenuContainer.collapseMenu()
        self.ui.mainPages.setCurrentWidget(self.ui.page_15)
    
    ################################################################
    # TreeView
    ################################################################
    def treeViewContextMenu(self, pos):
        ...
    
    def treeViewClicked(self):
         if self.fileManager.isTrue:
            self.ui.mainPages.setCurrentWidget(self.ui.page_16)
            self.fileManager.isTrue = False

    ################################################################
    # Changing the View Options for min and max pages
    ################################################################
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

    ################################################################
    #MenuBar Actions
    ################################################################
    def setUpMemu(self):
        #FileMenu
        # new file
        self.ui.actionNew_File.setShortcut("Ctrl+N")
        self.ui.actionNew_File.triggered.connect(self.newFile)
        self.ui.actionNew_File.triggered.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.page_16))
        # new folder
        #self.ui.actionNew_Folder.setShortcut()
        self.ui.actionNew_Folder.triggered.connect(self.newFolder)
        # new text file
        #self.ui.actionNew_Text_File.setShortcut()
        self.ui.actionNew_Text_File.triggered.connect(self.newTextFile)
        # new project
        #self.ui.actionNew_Project.setShortcut()
        self.ui.actionNew_Project.triggered.connect(self.newProject)
        # open file
        self.ui.actionOpen_File.setShortcut("Ctrl+O")
        self.ui.actionOpen_File.triggered.connect(self.openFile)
        # open folder
        self.ui.actionOpen_Folder.setShortcut("Ctrl+K")
        self.ui.actionOpen_Folder.triggered.connect(self.openFolder)
        # open recent
        #self.ui.
        #self.ui.
        # save
        self.ui.actionSave.setShortcut("Ctrl+S")
        self.ui.actionSave.triggered.connect(self.saveFile)
        # save as
        self.ui.actionSave_As.setShortcut("Ctrl+Shift+S")
        self.ui.actionSave_As.triggered.connect(self.saveAs)

        # edit Menu
        # copy
        self.ui.actionCopy.setShortcut("Ctrl+C")
        self.ui.actionCopy.triggered.connect(self.copy)
        # window menu
        #Ai Actions
        

    '''def contextMenuEvent(self, event):
        self.aiActionsMenu.exec(event.globalPos())'''

    def newFile(self):
        self.setNewTab(Path("untitled"), is_new_file=True)

    def newFolder(self):
        ...

    def newTextFile(self):
        ...

    def newProject(self):
        ...

    def openFile(self):
        #ops = QFileDialog.options() #Idk how tf this works :(
        #ops |= QFileDialog.DontUseNativeDialog
        #ops = QFileDialog.Option
        newFile, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", )
        if newFile =='':
            self.statusBar().showMessage("Cancelled", 2000)
            return
        f = Path(newFile)
        self.setNewTab(f)

    def openFolder(self):
        
        #ops = QFileDialog.options()
        #ops |= QFileDialog.DontUseNativeDialog
        ops = QFileDialog.ShowDirsOnly

        newFolder = QFileDialog.getExistingDirectory(self, "Pick A Folder", "", options=ops)
        if newFolder:
            self.model.setRootPath(newFolder)
            self.ui.treeView.setRootIndex(self.model.index(newFolder))
            self.statusBar().showMessage(f"Opened {newFolder}", 2000)
        
    def saveFile(self):
        if self.currentFile is None and self.ui.tabWidget.count() > 0:
            self.saveAs()
        editor = self.ui.tabWidget.currentWidget()
        self.currentFile.write_text(editor.text())
        self.statusBar().showMessage(f"Saved {self.currentFile.name}", 2000)
        editor.currentFileChanged = False


    def saveAs(self):
        editor = self.ui.tabWidget.currentWidget()
        if editor is None:
            return
        
        filePath = QFileDialog.getSaveFileName(self, "Save As", os.getcwd())[0]
        if filePath == '':
            self.statusBar().showMessage("Cancelled", 2000)
        path = Path(filePath)
        path.write_text(editor.text())
        self.ui.tabWidget.setTabText(self.ui.tabWidget.currentIndex(), path.name)
        self.statusBar().showMessage(f"Saved {path.name}", 2000)
        self.currentFile = path
        editor.currentFileChanged = False

    def copy(self):
        editor = self.ui.tabWidget.currentWidget()
        if editor is not None:
            editor.copy()

    ################################################################
    #Setting up editor
    ################################################################
    def getEditorMsg(self) -> QsciScintilla:
        editor = EditorMsg()
        return editor
    
    def getEditor(self, path: Path = None, is_python_file=True) -> QsciScintilla:
        editor = Editor(self, path = path, is_python_file = is_python_file)
        return editor

    def isBinary(self, path):
        with open(path, 'rb') as f:
            return b'\0' in f.read(1024)


    def setNewTab(self, path: Path, is_new_file=False):
        if not is_new_file and self.isBinary(path):
            self.ui.statusBar().showMessage("Cannot Open Binary File", 2000)
            return
        if path.is_dir():
            return 
        
        editor = self.getEditor(path, path.suffix in {".py", ".pyc", ".pyw"})  
        if is_new_file:
            self.ui.tabWidget.addTab(editor, "untitled")
            self.statusBar().showMessage("Opened untitled")
            self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.count() - 1)
            self.currentFile = None
            return

        #Check if file is already opened
        for i in range(self.ui.tabWidget.count()):
            if self.ui.tabWidget.tabText(i) == path.name or self.ui.tabWidget.tabText(i) == "*"+path.name:
                self.ui.tabWidget.setCurrentIndex(i)
                self.currentFile = path
                return print("1")
       
        #Create new tab
        self.ui.tabWidget.addTab(editor, path.name)
        editor.setText(path.read_text(encoding='utf-8'))
        editor.setText(path.read_text())
        #self.ui.setWindowTitle(path.name)
        self.currentFile = path
        self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.count() - 1)
        self.statusBar().showMessage(f"Opened {path.name}", 2000)


class SplashScreen(QtWidgets.QMainWindow, Ui_SplashScreen):
    def __init__(self, *args, obj=None, **kwargs):
        super(SplashScreen, self).__init__(*args, **kwargs)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # Remove title bar
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground) # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(20)
        

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        ## ==> END ##

    ## DEF TO LOANDING
    ########################################################################
    def progress (self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))
        
        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 1

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()
            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 0.5

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(116, 225, 237, 1));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)
########################################################################
## EXECUTE APP
########################################################################


if __name__ == "__main__":
    app = QApplication([])
    ########################################################################
    ## 
    ########################################################################
    window = SplashScreen()
    app.processEvents()
    window.show()
    sys.exit(app.exec())
    
########################################################################
## END===>
########################################################################  

