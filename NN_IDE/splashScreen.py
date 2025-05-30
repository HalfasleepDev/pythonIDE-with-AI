# Form implementation generated from reading ui file 'splash_screenNNIDE.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import QSS_Resources_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QtWidgets.QWidget(parent=SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.circularProgressBarBase = QtWidgets.QFrame(parent=self.centralwidget)
        self.circularProgressBarBase.setGeometry(QtCore.QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgress = QtWidgets.QFrame(parent=self.circularProgressBarBase)
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(116, 225, 237, 1));\n"
"}")
        self.circularProgress.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.circularBg = QtWidgets.QFrame(parent=self.circularProgressBarBase)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: rgba(181, 171, 252, 120);\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QtWidgets.QFrame(parent=self.circularProgressBarBase)
        self.container.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.container.setStyleSheet("QFrame{\n"
"    border-radius: 135px;\n"
"    background-color: #7B63FD;\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.container.setObjectName("container")
        self.layoutWidget = QtWidgets.QWidget(parent=self.container)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 194, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTitle = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)
        self.labelPercentage = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(68)
        self.labelPercentage.setFont(font)
        self.labelPercentage.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelPercentage.setObjectName("labelPercentage")
        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)
        self.labelLoadingInfo = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelLoadingInfo.setMinimumSize(QtCore.QSize(0, 20))
        self.labelLoadingInfo.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelLoadingInfo.setFont(font)
        self.labelLoadingInfo.setStyleSheet("QLabel{\n"
"    border-radius: 10px;    \n"
"    background-color: #2D2E2E;\n"
"    color: #FFFFFF;\n"
"    margin-left: 40px;\n"
"    margin-right: 40px;\n"
"}")
        self.labelLoadingInfo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.labelLoadingInfo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelLoadingInfo.setObjectName("labelLoadingInfo")
        self.gridLayout.addWidget(self.labelLoadingInfo, 2, 0, 1, 1)
        self.labelCredits = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet("background-color: none;\n"
"color: #E1E5FC;")
        self.labelCredits.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelCredits.setObjectName("labelCredits")
        self.gridLayout.addWidget(self.labelCredits, 3, 0, 1, 1)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.labelTitle.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-weight:600; color:#74e1ed;\">NN-IDE </span>Prototype</p></body></html>"))
        self.labelPercentage.setText(_translate("SplashScreen", "<p><span style=\" font-size:68pt;\">0</span><span style=\" font-size:58pt; vertical-align:super;\">%</span></p>"))
        self.labelLoadingInfo.setText(_translate("SplashScreen", "loading..."))
        self.labelCredits.setText(_translate("SplashScreen", "Created by HalfAsleepDev"))
