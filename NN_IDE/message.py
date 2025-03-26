from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import QSS_Resources_rc
import os
from datetime import datetime

sendBy = None


class Message(QWidget):
    def __init__(self, message, me_send):
        super().__init__()
        global sendBy
        sendBy = me_send

        self.setMinimumHeight(3)
        self.setup_ui(message)
        self.setFixedHeight(self.layout.sizeHint().height())

        # SET MESSAGE
        self.message.setText(message)
        #self.message.setFixedHeight(int(self.message.document().size().height() + self.message.contentsMargins().top()*5))
        #print(self.setMessageHeight(message))
        print(self.message.width())
        # SET DATE TIME
        dateTime = datetime.now()
        dateTimeFormat = dateTime.strftime("%m/%d/%Y %H:%M")
        self.data_message.setText(str(dateTimeFormat))

    def setup_ui(self, newMessage):
        # LAYOUT
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)

        # FRAME BG
        self.bg = QFrame()
        if sendBy:
            self.bg.setStyleSheet("#bg {background-color: #0e0e0f; border-radius: 10px; margin-left: 3px; } #bg:hover { background-color: #252628; }")
        else:
            self.bg.setStyleSheet("#bg {background-color: #28282b; border-radius: 10px; margin-right: 3px; } #bg:hover { background-color: #252628; }")
        self.bg.setObjectName("bg")

        # FRAME BG
        self.btn = QPushButton()
        self.btn.setMinimumSize(10, 10)
        self.btn.setMaximumSize(10, 10)
        self.btn.setStyleSheet("""
        QPushButton {
            background-color: transparent;
            border-radius: 4px;
            background-repeat: no-repeat;
            position: center;
            image: url(:/icons/Icons/more-horizontal.png);
        }
        QPushButton:hover {
            background-color: rgb(61, 62, 65);
        }
        QPushButton:pressed {
            background-color: rgb(16, 17, 18);
        }        
        """)

        if sendBy:
            self.layout.addWidget(self.bg)
            self.layout.addWidget(self.btn)
        else:
            self.layout.addWidget(self.btn)
            self.layout.addWidget(self.bg)

        # LAYOUT INSIDE
        self.layout_inside = QVBoxLayout(self.bg)
        self.layout.setContentsMargins(3,3,3,3)

        # LABEL MESSAGE 
        self.message = QTextBrowser()
        self.message.setText("message test")
        self.message.setStyleSheet("font: 500 6pt 'Segoe UI'")
        self.message.setTextInteractionFlags(Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)
        #self.message.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff) 
        #self.message.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) 
        #self.message.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.message.document().setTextWidth(285)
        self.message.setFixedHeight(self.setMessageHeight(newMessage))
        #print(int(self.message.document().size().height() + self.message.contentsMargins().top()*2) *10)
        #self.message.setFixedHeight(self.message.document().size().height())
        #self.message.document().documentLayout().documentSizeChanged.connect(self.wrapHeightToContents)

        # LABEL MESSAGE 
        self.data_message = QLabel()
        self.data_message.setText("date")
        self.data_message.setStyleSheet("font: 4pt 'Segoe UI'; color: #4c5154")
        if sendBy:
            self.data_message.setAlignment(Qt.AlignRight)
        else:
            self.data_message.setAlignment(Qt.AlignLeft)

        self.layout_inside.addWidget(self.message)
        self.layout_inside.addWidget(self.data_message)
        
    def setMessageHeight(self, message):
        self.message.setText(message)
        #self.message.document().setTextWidth(200)
        #print(self.message.document().size().height())
        print(int(self.message.document().size().height() + self.message.contentsMargins().top() + self.message.contentsMargins().bottom())-10)
        return int((self.message.document().size().height() + self.message.contentsMargins().top() + self.message.contentsMargins().bottom()) -10)
        #return int(self.message.document().size().height())
 