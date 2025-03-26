import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *


class CustomMainWindow(QMainWindow):
    def __init__(self):
        super(CustomMainWindow, self).__init__()

        # Window setup
        # --------------

        # 1. Define the geometry of the main window
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle("QScintilla Test")

        # 2. Create frame and layout
        self.__frm = QFrame(self)
        self.__frm.setStyleSheet("QWidget { background-color: #ffeaeaea }")
        self.__lyt = QVBoxLayout()
        self.__frm.setLayout(self.__lyt)
        self.setCentralWidget(self.__frm)
        self.__myFont = QFont()
        self.__myFont.setPointSize(14)

        # 3. Place a button
        self.__btn = QPushButton("Qsci")
        self.__btn.setFixedWidth(50)
        self.__btn.setFixedHeight(50)
        self.__btn.clicked.connect(self.__btn_action)
        self.__btn.setFont(self.__myFont)
        self.__lyt.addWidget(self.__btn)

        # QScintilla editor setup
        # ------------------------

        # ! Make instance of QsciScintilla class!
        self.__editor = QsciScintilla()
        self.__editor.setText("Hello\n")
        self.__editor.append("world")
        self.__editor.setLexer(None)
        self.__editor.setUtf8(True)  # Set encoding to UTF-8
        self.__editor.setFont(self.__myFont)  # Will be overridden by lexer!

        # ! Add editor to layout !
        self.__lyt.addWidget(self.__editor)

        self.show()



    def __btn_action(self):
        print("Hello World!")

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_PageDown:
            print("ok")




 #End Class 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = CustomMainWindow()

    sys.exit(app.exec_())

'''class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.TerminalProcess = QProcess(self)
        self.TerminalOutput = QTextBrowser(self)
        self.TerminalInput = QLineEdit(self)
        #self.run_command_button = QPushButton("Run Command", self)
        self.LineEditIndication = ""

        layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input)
        input_layout.addWidget(self.run_command_button)
        layout.addLayout(input_layout)
        layout.addWidget(self.output)
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.TerminalProcess.readyReadStandardOutput.connect(self.TerminalReadOutput)
        self.TerminalRunCommandButton.clicked.connect(self.run_command) #change to return
        self.TerminalProcess.start("cmd.exe")

    def TerminalReadOutput(self):
        stream = QTextStream(self.TerminalProcess)
        self.TerminalOutput.append(stream.readAll())
        #put last line in lineEdit
        self.lineEditIndication = self.TerminalOutput.toPlainText()
        self.TerminalInput.setPlaceholderText(self.indication.splitlines()[-1])
        

    def runTerminalCommand(self):
        command = self.input.text() + "\n"
        self.process.write(command.encode())
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())'''