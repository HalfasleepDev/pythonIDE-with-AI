from PyQt6 import QtGui, QtWidgets
from PyQt6.Qsci import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import keyword
import pkgutil
from lexer import PyCustomLexer

class Editor(QsciScintilla):
    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)

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

        #lexer for syntax highlighting
        self.pyLexer = PyCustomLexer(self)
        self.pyLexer.setDefaultFont(self.font)

        # API goes here
        self.api = QsciAPIs(self.pyLexer)
        for key in keyword.kwlist + dir(__builtins__):
            self.api.add(key)

        for _, name, _ in pkgutil.iter_modules():
            self.api.add(name)

        #Testing only
        self.api.add("addition(a: int, b: int)")

        self.api.prepare()

        self.setLexer(self.pyLexer)

        # line numbers
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.setMarginWidth(0, "000")
        self.setMarginsForegroundColor(QColor("#ff888888")) #TODO Change color
        self.setMarginsBackgroundColor(QColor("#282c34")) #TODO Change color
        self.setMarginsFont(self.font)

        # key press
        #self.keyPressEvent = self.handleEditorPress
    
    def keyPressEvent(self, e: QKeyEvent) -> None:
        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_Space:
            self.autoCompleteFromAll()
        else:
            return super().keyPressEvent(e)