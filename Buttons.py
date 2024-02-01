# This Python file uses the following encoding: utf-8
from PyQt6 import QtCore
from PyQt6 import QtWidgets

class Buttons(QtWidgets.QPushButton):
    def __init__(self, name, text, size=44, parent=None):
        super().__init__(text, parent)
        self.setObjectName(name)
        self.setMinimumSize(size, size)
