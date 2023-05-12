# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacevlVZNL.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)
import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 546)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #5B5C5C;\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color: #2D2E2E;\n"
"	border-radius: 12px;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"}\n"
"#widget, #frame, #frame_4, #frame_5{\n"
"	background-color: #606390;\n"
"	border-radius:12px\n"
"}\n"
"#minimizedMenuSubContainer{\n"
"	background-color: #606390;\n"
"	border-radius:12px\n"
"}\n"
"#rightMenuSubContainer{\n"
"	background-color: #606390;\n"
"	border-radius:12px\n"
"}\n"
"#terminalPages{\n"
"	background-color: #2d2e2e;\n"
"	border-radius:12px\n"
"}\n"
"#minRightMenuSubContainer{\n"
"	background-color: #606390;\n"
"	border-radius:12px\n"
"}\n"
"QMenuBar{\n"
"	background-color: #2D2E2E;\n"
"}\n"
"QMenuBar::item:selected {\n"
"	background: #606390;\n"
"	border-radius: 4px;\n"
"}\n"
"QMenu{\n"
""
                        "	 background-color: #2D2E2E;\n"
"     margin: 2px; /* some spacing around the menu */\n"
"}\n"
"QMenu::item {\n"
"    padding: 2px 25px 2px 20px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"QMenu::item:selected {\n"
"	background: #494454;\n"
"	border-radius: 4px;\n"
"}\n"
"QMenu::separator{\n"
"	border: 1px transparent;\n"
"	height: 1px;\n"
"    background: white;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"")
        self.actionNew_File = QAction(MainWindow)
        self.actionNew_File.setObjectName(u"actionNew_File")
        self.actionNew_Folder = QAction(MainWindow)
        self.actionNew_Folder.setObjectName(u"actionNew_Folder")
        self.actionNew_Text_File = QAction(MainWindow)
        self.actionNew_Text_File.setObjectName(u"actionNew_Text_File")
        self.actionNew_Project = QAction(MainWindow)
        self.actionNew_Project.setObjectName(u"actionNew_Project")
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionOpen_Folder = QAction(MainWindow)
        self.actionOpen_Folder.setObjectName(u"actionOpen_Folder")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.action_File_Here = QAction(MainWindow)
        self.action_File_Here.setObjectName(u"action_File_Here")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionUndo.setVisible(True)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionOpen_Terminal = QAction(MainWindow)
        self.actionOpen_Terminal.setObjectName(u"actionOpen_Terminal")
        self.actionOpen_Editor = QAction(MainWindow)
        self.actionOpen_Editor.setObjectName(u"actionOpen_Editor")
        self.actionOpen_Monitor = QAction(MainWindow)
        self.actionOpen_Monitor.setObjectName(u"actionOpen_Monitor")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setMinimumSize(QSize(50, 0))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(0, 0))
        self.homeBtn.setStyleSheet(u"background-color: #baacfd;")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.homeBtn)

        self.fileBtn = QPushButton(self.frame_2)
        self.fileBtn.setObjectName(u"fileBtn")
        self.fileBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fileBtn.setIcon(icon1)
        self.fileBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.fileBtn)

        self.searchBtn = QPushButton(self.frame_2)
        self.searchBtn.setObjectName(u"searchBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon2)
        self.searchBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.searchBtn)

        self.aiBtn = QPushButton(self.frame_2)
        self.aiBtn.setObjectName(u"aiBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/codesandbox.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aiBtn.setIcon(icon3)
        self.aiBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.aiBtn)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 5)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setLayoutDirection(Qt.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.settingsBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.minimizedMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.minimizedMenuContainer.setObjectName(u"minimizedMenuContainer")
        self.minimizedMenuContainer.setMinimumSize(QSize(50, 0))
        self.verticalLayout_12 = QVBoxLayout(self.minimizedMenuContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 3, 0, 3)
        self.minimizedMenuSubContainer = QWidget(self.minimizedMenuContainer)
        self.minimizedMenuSubContainer.setObjectName(u"minimizedMenuSubContainer")
        self.minimizedMenuSubContainer.setMinimumSize(QSize(50, 0))
        self.verticalLayout_14 = QVBoxLayout(self.minimizedMenuSubContainer)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.minimizedMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.maxCenterMenuBtn = QPushButton(self.frame_4)
        self.maxCenterMenuBtn.setObjectName(u"maxCenterMenuBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/chevron-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxCenterMenuBtn.setIcon(icon5)
        self.maxCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.maxCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.minCenterMenuPages = QCustomStackedWidget(self.minimizedMenuSubContainer)
        self.minCenterMenuPages.setObjectName(u"minCenterMenuPages")
        self.minCenterMenuPages.setMinimumSize(QSize(0, 0))
        self.minCenterMenuPages.setMaximumSize(QSize(50, 16777215))
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_15 = QVBoxLayout(self.page_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(True)
        self.label_5.setMargin(10)
        self.label_5.setIndent(0)

        self.verticalLayout_15.addWidget(self.label_5)

        self.minCenterMenuPages.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_13 = QVBoxLayout(self.page_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_6 = QLabel(self.page_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(10)

        self.verticalLayout_13.addWidget(self.label_6)

        self.minCenterMenuPages.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_16 = QVBoxLayout(self.page_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_7 = QLabel(self.page_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setTextFormat(Qt.PlainText)
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(10)

        self.verticalLayout_16.addWidget(self.label_7)

        self.minCenterMenuPages.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_17 = QVBoxLayout(self.page_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_8 = QLabel(self.page_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setWordWrap(True)
        self.label_8.setMargin(10)

        self.verticalLayout_17.addWidget(self.label_8)

        self.minCenterMenuPages.addWidget(self.page_8)

        self.verticalLayout_14.addWidget(self.minCenterMenuPages)


        self.verticalLayout_12.addWidget(self.minimizedMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.minimizedMenuContainer)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 3, 0, 3)
        self.widget = QWidget(self.centerMenuContainer)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minCenterMenuBtn = QPushButton(self.frame)
        self.minCenterMenuBtn.setObjectName(u"minCenterMenuBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/chevron-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minCenterMenuBtn.setIcon(icon6)
        self.minCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.minCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.widget)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(13)
        self.label.setFont(font1)

        self.verticalLayout_7.addWidget(self.label)

        self.centerMenuPages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_2)

        self.centerMenuPages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_10 = QVBoxLayout(self.page_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_11 = QVBoxLayout(self.page_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.page_4)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.centerMenuContainer, 0, Qt.AlignRight)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setMinimumSize(QSize(572, 524))
        self.horizontalLayout_4 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 3, 0, 3)
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_30 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 3, 0, 3)
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.verticalLayout_31 = QVBoxLayout(self.page_15)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_13 = QLabel(self.page_15)
        self.label_13.setObjectName(u"label_13")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_13.setFont(font2)

        self.verticalLayout_31.addWidget(self.label_13)

        self.mainPages.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.verticalLayout_33 = QVBoxLayout(self.page_16)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_19 = QLabel(self.page_16)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.verticalLayout_33.addWidget(self.label_19)

        self.mainPages.addWidget(self.page_16)
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.verticalLayout_34 = QVBoxLayout(self.page_17)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_20 = QLabel(self.page_17)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)

        self.verticalLayout_34.addWidget(self.label_20)

        self.mainPages.addWidget(self.page_17)

        self.verticalLayout_30.addWidget(self.mainPages)


        self.horizontalLayout_4.addWidget(self.mainContentsContainer)

        self.minRightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.minRightMenuContainer.setObjectName(u"minRightMenuContainer")
        self.minRightMenuContainer.setEnabled(True)
        sizePolicy.setHeightForWidth(self.minRightMenuContainer.sizePolicy().hasHeightForWidth())
        self.minRightMenuContainer.setSizePolicy(sizePolicy)
        self.minRightMenuContainer.setMinimumSize(QSize(0, 0))
        self.minRightMenuContainer.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_24 = QVBoxLayout(self.minRightMenuContainer)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.minRightMenuSubContainer = QWidget(self.minRightMenuContainer)
        self.minRightMenuSubContainer.setObjectName(u"minRightMenuSubContainer")
        self.minRightMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_25 = QVBoxLayout(self.minRightMenuSubContainer)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.minRightMenuSubContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_6)
        self.verticalLayout_26.setSpacing(10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.maxRightMenuBtn = QPushButton(self.frame_6)
        self.maxRightMenuBtn.setObjectName(u"maxRightMenuBtn")
        self.maxRightMenuBtn.setIcon(icon6)
        self.maxRightMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.maxRightMenuBtn)

        self.closeMinRightMenuBtn = QPushButton(self.frame_6)
        self.closeMinRightMenuBtn.setObjectName(u"closeMinRightMenuBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeMinRightMenuBtn.setIcon(icon7)
        self.closeMinRightMenuBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_26.addWidget(self.closeMinRightMenuBtn)

        self.openPerformanceMonitorMinBtn = QPushButton(self.frame_6)
        self.openPerformanceMonitorMinBtn.setObjectName(u"openPerformanceMonitorMinBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/activity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openPerformanceMonitorMinBtn.setIcon(icon8)
        self.openPerformanceMonitorMinBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.openPerformanceMonitorMinBtn)

        self.minTerminalPages = QCustomStackedWidget(self.frame_6)
        self.minTerminalPages.setObjectName(u"minTerminalPages")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_29 = QVBoxLayout(self.page_9)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_18 = QLabel(self.page_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(24, 24))
        self.label_18.setMaximumSize(QSize(15, 14))
        self.label_18.setPixmap(QPixmap(u":/icons/Icons/life-buoy.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setWordWrap(True)
        self.label_18.setIndent(0)

        self.verticalLayout_29.addWidget(self.label_18, 0, Qt.AlignLeft|Qt.AlignTop)

        self.minTerminalPages.addWidget(self.page_9)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.verticalLayout_32 = QVBoxLayout(self.page_14)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_21 = QLabel(self.page_14)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(24, 24))
        self.label_21.setMaximumSize(QSize(15, 14))
        self.label_21.setPixmap(QPixmap(u":/icons/Icons/corner-up-right.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.label_21, 0, Qt.AlignTop)

        self.minTerminalPages.addWidget(self.page_14)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_27 = QVBoxLayout(self.page_10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_14 = QLabel(self.page_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(24, 24))
        self.label_14.setMaximumSize(QSize(15, 14))
        self.label_14.setPixmap(QPixmap(u":/icons/Icons/terminal.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.label_14, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.minTerminalPages.addWidget(self.page_10)

        self.verticalLayout_26.addWidget(self.minTerminalPages, 0, Qt.AlignLeft)


        self.verticalLayout_25.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.minRightMenuSubContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 200))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.label_17)

        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.label_15)


        self.verticalLayout_25.addWidget(self.frame_7)


        self.verticalLayout_24.addWidget(self.minRightMenuSubContainer)


        self.horizontalLayout_4.addWidget(self.minRightMenuContainer, 0, Qt.AlignRight)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QSize(203, 518))
        self.verticalLayout_18 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 3, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_19 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.rightMenuSubContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.viewOptionsBox = QComboBox(self.frame_5)
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/terminal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.viewOptionsBox.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/corner-up-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.viewOptionsBox.addItem(icon10, "")
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/life-buoy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.viewOptionsBox.addItem(icon11, "")
        self.viewOptionsBox.setObjectName(u"viewOptionsBox")
        self.viewOptionsBox.setStyleSheet(u"#viewOptionsBox::on {\n"
"	border: 1px solid #baacfd;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"#viewOptionsBox QListView {\n"
"	background-color: #2D2E2E;\n"
"	\n"
"}\n"
"#viewOptionsBox QListView:item:hover {\n"
"	background-color: #494454;\n"
"	border-radius: 4px;\n"
"	\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.viewOptionsBox, 0, Qt.AlignRight)

        self.openPerformanceMonitorBtn = QPushButton(self.frame_5)
        self.openPerformanceMonitorBtn.setObjectName(u"openPerformanceMonitorBtn")
        self.openPerformanceMonitorBtn.setIcon(icon8)
        self.openPerformanceMonitorBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.openPerformanceMonitorBtn, 0, Qt.AlignRight)

        self.closeRightMenuBtn = QPushButton(self.frame_5)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)

        self.minRightMenuBtn = QPushButton(self.frame_5)
        self.minRightMenuBtn.setObjectName(u"minRightMenuBtn")
        self.minRightMenuBtn.setIcon(icon5)
        self.minRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.minRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_5)

        self.terminalPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.terminalPages.setObjectName(u"terminalPages")
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_20 = QVBoxLayout(self.page_11)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_10 = QLabel(self.page_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_20.addWidget(self.label_10)

        self.terminalPages.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_21 = QVBoxLayout(self.page_12)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_11 = QLabel(self.page_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_21.addWidget(self.label_11)

        self.terminalPages.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.verticalLayout_22 = QVBoxLayout(self.page_13)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_12 = QLabel(self.page_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_22.addWidget(self.label_12)

        self.terminalPages.addWidget(self.page_13)

        self.verticalLayout_19.addWidget(self.terminalPages)

        self.widget_2 = QWidget(self.rightMenuSubContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_23 = QVBoxLayout(self.widget_2)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 200))
        self.label_9.setFont(font1)

        self.verticalLayout_23.addWidget(self.label_9)


        self.verticalLayout_19.addWidget(self.widget_2)


        self.verticalLayout_18.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_4.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 900, 22))
        self.menuBar.setAcceptDrops(True)
        self.menuBar.setAutoFillBackground(False)
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOpen_Recent = QMenu(self.menuFile)
        self.menuOpen_Recent.setObjectName(u"menuOpen_Recent")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuWindow = QMenu(self.menuBar)
        self.menuWindow.setObjectName(u"menuWindow")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuWindow.menuAction())
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionNew_Folder)
        self.menuFile.addAction(self.actionNew_Text_File)
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.menuOpen_Recent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuOpen_Recent.addAction(self.action_File_Here)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuWindow.addAction(self.actionOpen_Terminal)
        self.menuWindow.addAction(self.actionOpen_Editor)
        self.menuWindow.addAction(self.actionOpen_Monitor)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(1)
        self.minTerminalPages.setCurrentIndex(0)
        self.terminalPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew_File.setText(QCoreApplication.translate("MainWindow", u"New File...", None))
        self.actionNew_Folder.setText(QCoreApplication.translate("MainWindow", u"New Folder...", None))
        self.actionNew_Text_File.setText(QCoreApplication.translate("MainWindow", u"New Text File...", None))
        self.actionNew_Project.setText(QCoreApplication.translate("MainWindow", u"New Project...", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File...", None))
        self.actionOpen_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder...", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        self.action_File_Here.setText(QCoreApplication.translate("MainWindow", u"[File Here]", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionOpen_Terminal.setText(QCoreApplication.translate("MainWindow", u"Open Terminal", None))
        self.actionOpen_Editor.setText(QCoreApplication.translate("MainWindow", u"Open Editor", None))
        self.actionOpen_Monitor.setText(QCoreApplication.translate("MainWindow", u"Open Monitor", None))
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.fileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"File Explorer", None))
#endif // QT_CONFIG(tooltip)
        self.fileBtn.setText("")
#if QT_CONFIG(tooltip)
        self.searchBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Search", None))
#endif // QT_CONFIG(tooltip)
        self.searchBtn.setText("")
#if QT_CONFIG(tooltip)
        self.aiBtn.setToolTip(QCoreApplication.translate("MainWindow", u"AI Assistant", None))
#endif // QT_CONFIG(tooltip)
        self.aiBtn.setText("")
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maxCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maxCenterMenuBtn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"S e t t i n g s - M i n", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"A I - A s s i s t a n t - M i n", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"S e a r c h - M i n", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"F i  l e - E x p l o r e r - M i n", None))
#if QT_CONFIG(tooltip)
        self.minCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minCenterMenuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"AI Assistant", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"File Explorer", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Text Editor", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"More Settings", None))
#if QT_CONFIG(tooltip)
        self.maxRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maxRightMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeMinRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeMinRightMenuBtn.setText("")
        self.openPerformanceMonitorMinBtn.setText("")
        self.label_18.setText("")
        self.label_21.setText("")
        self.label_14.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"CPU: 15%", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"RAM: 33%", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"GPU: 21%", None))
        self.viewOptionsBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.viewOptionsBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Output", None))
        self.viewOptionsBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Debug", None))

#if QT_CONFIG(tooltip)
        self.openPerformanceMonitorBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Performance monitor", None))
#endif // QT_CONFIG(tooltip)
        self.openPerformanceMonitorBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minRightMenuBtn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Performance monitor", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOpen_Recent.setTitle(QCoreApplication.translate("MainWindow", u"Open Recent", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
    # retranslateUi

