from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
import pyqtgraph as pg


class ATSMain(QMainWindow):
    def __init__(self, eventEngine=None, dataEngine=None):
        super(ATSMain, self).__init__()
        self.widgetDict = {}
        self.initUi()
        self.eventEngine = eventEngine
        self.dataEngine = dataEngine

    def initUi(self):
        self.setWindowTitle("Auto Trading System")
        self.initCentral()
        self.initMenu()
        self.initStatusBar()

    def initCentral(self):
        """初始化中心区域"""
        # widgetMarketM, dockMarketM = self.createDock(MarketMonitor, u'行情', QtCore.Qt.RightDockWidgetArea)
        # widgetLogM, dockLogM = self.createDock(LogMonitor, u'日志', QtCore.Qt.BottomDockWidgetArea)
        # widgetErrorM, dockErrorM = self.createDock(ErrorMonitor, u'错误', QtCore.Qt.BottomDockWidgetArea)
        # widgetTradeM, dockTradeM = self.createDock(TradeMonitor, u'成交', QtCore.Qt.BottomDockWidgetArea)
        # widgetOrderM, dockOrderM = self.createDock(OrderMonitor, u'委托', QtCore.Qt.RightDockWidgetArea)
        # widgetPositionM, dockPositionM = self.createDock(PositionMonitor, u'持仓', QtCore.Qt.BottomDockWidgetArea)
        # widgetAccountM, dockAccountM = self.createDock(AccountMonitor, u'资金', QtCore.Qt.BottomDockWidgetArea)
        # widgetTradingW, dockTradingW = self.createDock(TradingWidget, u'交易', QtCore.Qt.LeftDockWidgetArea)
        #
        # self.tabifyDockWidget(dockTradeM, dockErrorM)
        # self.tabifyDockWidget(dockTradeM, dockLogM)
        # self.tabifyDockWidget(dockPositionM, dockAccountM)
        #
        # dockTradeM.raise_()
        # dockPositionM.raise_()
        #
        # # 连接组件之间的信号
        # widgetPositionM.itemDoubleClicked.connect(widgetTradingW.closePosition)

        # 保存默认设置
        self.saveWindowSettings('default')

    def createDock(self, widgetClass, widgetName, widgetArea):
        """创建停靠组件"""
        widget = widgetClass(self.mainEngine, self.eventEngine)
        dock = QtGui.QDockWidget(widgetName)
        dock.setWidget(widget)
        dock.setObjectName(widgetName)
        dock.setFeatures(dock.DockWidgetFloatable | dock.DockWidgetMovable)
        self.addDockWidget(widgetArea, dock)
        return widget, dock

if __name__ == '__main__':
    pass
