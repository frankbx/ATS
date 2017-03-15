from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from collections import OrderedDict


class BasicTable(QTableWidget):
    signal = QtCore.pyqtSignal(type(Event()))
    def __init__(self, dataEngine=None, eventEngine=None, parent=None):
        super(BasicTable, self).__init__(parent)
        self.dataEngine = dataEngine
        self.eventEngine = eventEngine

        self.headerDict = OrderedDict()
        self.headerList = []

        self.dataDict = {}
        self.dataKey = ''

        self.eventType = ''

        self.saveData = False
        self.sorting = False
