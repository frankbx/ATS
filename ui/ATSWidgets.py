from collections import OrderedDict
from eventEngine import *

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class BasicTable(QTableWidget):
    signal = pyqtSignal(type(Event()))

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


class PChangeCell(QTableWidgetItem):
    """Display change percent"""

    def __init__(self, text=None):
        super(PChangeCell, self).__init__()
        # self.mainEngine = mainEngine
        self.data = None
        if text is not None:
            self.setContent(text)

    def setContent(self, text):
        if text >= 0:
            self.setForeground(QColor('red'))
        elif text < 0:
            self.setForeground(QColor('green'))
        self.setText(text)


if __name__ == '__main__':
    import sys

    # from PyQt5.QtWidgets import *

    app = QApplication(sys.argv)

    t = BasicTable()
    t.show()
    sys.exit(app.exec_())
