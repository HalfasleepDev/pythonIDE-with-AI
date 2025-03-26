from PyQt5 import QtCore, QtGui, QtWidgets


def create_pixmap(point, radius=64):
    rect = QtCore.QRect(QtCore.QPoint(), 2 * radius * QtCore.QSize(1, 1))
    pixmap = QtGui.QPixmap(rect.size())
    rect.adjust(1, 1, -1, -1)
    pixmap.fill(QtCore.Qt.transparent)
    painter = QtGui.QPainter(pixmap)
    painter.setRenderHints(
        QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing
    )
    pen = painter.pen()
    painter.setPen(QtCore.Qt.NoPen)

    gradient = QtGui.QLinearGradient()
    gradient.setColorAt(1, QtGui.QColor("#FD6684"))
    gradient.setColorAt(0, QtGui.QColor("#E0253F"))
    gradient.setStart(0, rect.height())
    gradient.setFinalStop(0, 0)

    painter.setBrush(QtGui.QBrush(gradient))
    painter.drawEllipse(rect)
    painter.setPen(pen)
    painter.drawText(rect, QtCore.Qt.AlignCenter, str(point))
    painter.end()
    return pixmap


class NotificationButton(QtWidgets.QWidget):
    scoreChanged = QtCore.pyqtSignal(int)

    def __init__(self, score=0, icon=QtGui.QIcon(), radius=12, parent=None):
        super(NotificationButton, self).__init__(parent)

        self.m_score = score
        self.m_radius = radius

        self.setContentsMargins(0, self.m_radius, self.m_radius, 0)
        self.m_button = QtWidgets.QToolButton(clicked=self.clear)
        self.m_button.setContentsMargins(0, 0, 0, 0)
        self.m_button.setIcon(icon)
        self.m_button.setIconSize(QtCore.QSize(18, 18))
        lay = QtWidgets.QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.m_button)
        self.m_label = QtWidgets.QLabel(self)
        self.m_label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.m_label.raise_()
        self.setSizePolicy(self.m_button.sizePolicy())
        self.update_notification()

    @QtCore.pyqtProperty(int, notify=scoreChanged)
    def score(self):
        return self.m_score

    @score.setter
    def score(self, score):
        if self.m_score != score:
            self.m_score = score
            self.update_notification()
            self.scoreChanged.emit(score)

    @QtCore.pyqtSlot()
    def clear(self):
        self.score = 0

    @QtCore.pyqtProperty(int)
    def radius(self):
        return self.m_radius

    @radius.setter
    def radius(self, radius):
        self.m_radius = radius
        self.update_notification()

    def update_notification(self):
        self.setContentsMargins(0, self.m_radius, self.m_radius, 0)
        self.m_label.setPixmap(create_pixmap(self.m_score, self.m_radius))
        self.m_label.adjustSize()

    def resizeEvent(self, event):
        self.m_label.move(self.width() - self.m_label.width(), 0)
        super(NotificationButton, self).resizeEvent(event)


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.m_item_le = QtWidgets.QLineEdit("Stack Overflow")
        add_button = QtWidgets.QPushButton("Add", clicked=self.add_item)
        self.m_notification_button = NotificationButton(
            icon=QtGui.QIcon("image.png")
        )
        self.m_list_widget = QtWidgets.QListWidget()

        vlay = QtWidgets.QVBoxLayout(self)
        hlay = QtWidgets.QHBoxLayout()
        hlay.addWidget(self.m_item_le)
        hlay.addWidget(add_button)
        vlay.addLayout(hlay)
        vlay.addWidget(
            self.m_notification_button, alignment=QtCore.Qt.AlignRight
        )
        vlay.addWidget(self.m_list_widget)

    @QtCore.pyqtSlot()
    def add_item(self):
        text = self.m_item_le.text()
        self.m_list_widget.addItem(
            "%s: %s" % (self.m_list_widget.count(), text)
        )
        self.m_notification_button.score += 1
        self.m_list_widget.scrollToBottom()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())