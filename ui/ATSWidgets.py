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

        # Header Dict uses Header Label as keys, Cell Type as values
        self.headerDict = OrderedDict()
        self.headerList = []

        self.dataDict = {}
        self.dataKey = ''

        self.eventType = ''

        self.saveData = False
        self.sorting = False

    def setHeaderDict(self, headerDict):
        self.headerDict = headerDict
        self.headerList = headerDict.keys()

    def setEventType(self, eventType):
        self.eventType = eventType

    def initTable(self):
        """初始化表格"""
        # 设置表格的列数
        col = len(self.headerDict)
        self.setColumnCount(col)

        # 设置列表头
        labels = self.headerList
        self.setHorizontalHeaderLabels(labels)

        # 关闭左边的垂直表头
        self.verticalHeader().setVisible(False)

        # 设为不可编辑
        self.setEditTriggers(self.NoEditTriggers)

        # 设为行交替颜色
        self.setAlternatingRowColors(True)

        # 设置允许排序
        self.setSortingEnabled(self.sorting)


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
    t.setHeaderDict({'Code':[1,2,3,4,5,6],'Name':[1,2,3,4,5,6]})
    t.initTable()
    t.show()
    sys.exit(app.exec_())
