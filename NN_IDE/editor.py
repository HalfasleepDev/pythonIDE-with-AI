import sys
from PyQt6 import QtGui, QtWidgets
from PyQt6.Qsci import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import keyword
import pkgutil
from lexer import PyCustomLexer
from autoCompleterJedi import AutoCompleter
#TODO:from autoCompleterAI import
from pathlib import Path
from PyQt6.Qsci import QsciAPIs
sys.path.insert(0, '/Users/eloig/Dropbox/Projects/PythonIDE_Project/Enviro_NN_IDE/PytorchStuff')
from generateCode import codeCompletion, commentGeneration, autoDoc
import re
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import MainWindow

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

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)

class Editor(QsciScintilla):
    CIRCLE_MARKER_NUM = 0

    def getAiCompleteIndex(self, index):
        self.aiCompleteIndex = index



    def getAiCommentGenIndex(self, index):
        self.aiCommentGenIndex = index

    
    def getAiAutoDocIndex(self, index):
        self.aiAutoDocIndex = index
    

    def __init__(self, mainWindow, parent=None, path: Path = None, is_python_file=True):
        super(Editor, self).__init__(parent)

        self.mainWindow: MainWindow = mainWindow
        self._currentFileChanged = False
        self.firstLaunch = True

        self.path = path
        self.fullPath = self.path.absolute()
        self.isPythonFile = is_python_file

        self.aiCompleteEvent = False
        self.aiIndex = 0
        self.aiLine = 0
        self.threadpool = QThreadPool()
        self.codeComment= ""

        self.cursorPositionChanged.connect(self._cursorPositionChanged)
        self.marginClicked.connect(self._marginClicked)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.generateContextMenu)
        self.textChanged.connect(self._textChanged)
        
        

        #encoding
        self.setUtf8(True)
        # Font
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        #brace matching
        self.setBraceMatching(QsciScintilla.BraceMatch.SloppyBraceMatch)

        #indentation
        self.setIndentationGuides(True)
        self.setTabWidth(4)
        self.setIndentationsUseTabs(False)
        self.setAutoIndent(True)

        #autoComplete
        self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)
        self.setAutoCompletionThreshold(1) # auto complete will show after one character
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionUseSingle(QsciScintilla.AutoCompletionUseSingle.AcusNever)


        #Caret
        self.setCaretForegroundColor(QColor("#f9f9f8")) #TODO Change color
        self.setCaretLineVisible(True)
        self.setCaretWidth(2)
        self.setCaretLineBackgroundColor(QColor("#3e8f9a")) #TODO Change color

        #Eol
        self.setEolMode(QsciScintilla.EolMode.EolWindows)
        self.setEolVisibility(False)

        if self.isPythonFile:
            #lexer for syntax highlighting
            self.pyLexer = PyCustomLexer(self)
            self.pyLexer.setDefaultFont(self.font)

            self.__api = QsciAPIs(self.pyLexer)

            self.autoCompleter = AutoCompleter(self.fullPath, self.__api)
            self.autoCompleter.finished.connect(self.loadedAutoComplete)

            self.setLexer(self.pyLexer)
            print(self.text(10), "here")
            print(self.autoCompleter.line)
        else:
            self.setPaper(QColor('#282c34')) #TODO: change color
            self.setColor(QColor('#abb2bf')) #TODO: change color

        # line numbers
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.setMarginWidth(0, "000")
        self.setMarginsForegroundColor(QColor("#ff888888")) #TODO Change color
        self.setMarginsBackgroundColor(QColor("#282c34")) #TODO Change color
        self.setMarginsFont(self.font)
        self.setMarginSensitivity(1, True)
        self.markerDefine(QsciScintilla.MarkerSymbol.LeftRectangle  ,self.CIRCLE_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor('#8680A6'),self.CIRCLE_MARKER_NUM)

        # key press
        #self.keyPressEvent = self.handleEditorPress
    @property
    def currentFileChanged(self):
        return self._currentFileChanged

    @currentFileChanged.setter
    def currentFileChanged(self, value: bool):
        currIndex = self.mainWindow.ui.tabWidget.currentIndex()
        if value:
            self.mainWindow.ui.tabWidget.setTabText(currIndex, "*"+self.path.name)
        else:
            if self.mainWindow.ui.tabWidget.tabText(currIndex).startswith("*"):
                self.mainWindow.ui.tabWidget.setTabText(
                    currIndex,
                    self.mainWindow.ui.tabWidget.tabText(currIndex)[1:]
                )
        self._currentFileChanged = value

    def toggleComment(self, text: str):
        lines = text.split("\n")
        toggled_lines = []
        for line in lines:
            if line.startswith('#'):
                toggled_lines.append(line[1:].lstrip())
            else:
                toggled_lines.append("# " + line)
        
        return '\n'.join(toggled_lines)

    def keyPressEvent(self, e: QKeyEvent) -> None:

        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_Space:
            if self.isPythonFile:
                pos = self.getCursorPosition()
                self.autoCompleter.get_completions(pos[0]+1, pos[1], self.text())
                self.autoCompleteFromAPIs()
                return
            
        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_X:
            if not self.hasSelectedText():
                line, index = self.getCursorPosition()
                self.setSelection(line, 0, line, self.lineLength(line))
                self.cut()
                return
        
        if e.modifiers() == Qt.ControlModifier and e.text() == "/":
            if self.hasSelectedText():
                start, srow, end, erow = self.getSelection()
                self.setSelection(start, 0, end, self.lineLength(end)-1)
                self.replaceSelectedText(self.toggleComment(self.selectedText()))
                self.setSelection(start, srow, end, erow)
            else:
                line, _ = self.getCursorPosition()
                self.setSelection(line, 0, line, self.lineLength(line)-1) 
                self.replaceSelectedText(self.toggleComment(self.selectedText()))
                self.setSelection(-1, -1, -1, -1)

            return
        
        if e.modifiers() == Qt.KeyboardModifier.ControlModifier and e.key() == Qt.Key.Key_PageDown:
            if self.isPythonFile:
                line, index = self.getCursorPosition()
                docText = self.text(line)
                print(docText[:index]) #str needed for prompt
                print(line+1) #current line
                print(index) #current index
                prompt = docText[:index]
                print(prompt)
                try:
                    self.aiCompleteIndex
                except AttributeError: 
                    texts = codeCompletion(docText[:index], 0)
                else:
                    texts = codeCompletion(docText[:index], self.aiCompleteIndex)
                self.insertAt(texts.replace(prompt, '\n'), line, index)
                self.setReadOnly(False)

        return super().keyPressEvent(e)
        
    def _cursorPositionChanged(self, line: int, index: int) -> None: 
        if self.isPythonFile:
            self.autoCompleter.get_completions(line+1, index, self.text())
            

    def _marginClicked(self, margin: int, line: int) -> None: 
        
        if self.isPythonFile:
            docText = self.text(line)
            if docText.startswith(("#", "'''")) and docText != "#":
                self.markerAdd(line, self.CIRCLE_MARKER_NUM)
                self.margintext = docText
                self.marginline = line
                worker = Worker(self.genCom)
                self.threadpool.start(worker)
            
    def loadedAutoComplete(self):
        pass

    '''           if self.markersAtLine(line) != 0:
                    self.markerDelete(line, self.CIRCLE_MARKER_NUM)
                else:'''

    def genCom(self):
        docText =  self.margintext
        line = self.marginline
        try: 
            self.aiCommentGenIndex
        except AttributeError: 
            texts = commentGeneration(docText, 0)
        else:
            texts = commentGeneration(docText, self.aiCommentGenIndex)
        print(line)
        self.insertAt('\n'+ texts.replace(docText, '\n'), line+1, 0)
        self.markerDelete(line, self.CIRCLE_MARKER_NUM)

    def genAutoDoc(self):
        #line, index = self.getCursorPosition()
        if self.hasSelectedText():
            lineFrom, indexFrom, lineTo, indexTo = self.getSelection()
            text = self.selectedText()
            try: 
                self.aiAutoDocIndex
            except AttributeError:
                texts = autoDoc(text, 0)
            else:
                texts = autoDoc(text, self.aiAutoDocIndex)
            self.insertAt(texts, lineFrom+1, 0)
    
    def generateContextMenu(self, location):
        self.conMenu = self.createStandardContextMenu()
        self.conMenu.addSeparator()
        self.createAutoDoc = QAction("Generate Docstring")
        self.conMenu.addAction(self.createAutoDoc)

        self.conMenu.popup(self.mapToGlobal(location))
        self.createAutoDoc.triggered.connect(self.startAiAutoDoc)
    
    def startAiAutoDoc(self):
        if self.isPythonFile:
            worker = Worker(self.genAutoDoc)
            self.threadpool.start(worker)
    
    def _textChanged(self):
        if not self.currentFileChanged and not self.firstLaunch:
            self.currentFileChanged = True

        if self.firstLaunch:
            self.firstLaunch = False