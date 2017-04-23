import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


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
        # self.initStatusBar()

    def initCentral(self): 
        # 保存默认设置
        self.saveWindowSettings('default')
        pass

    def initMenu(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu("File")
        fileMenu.addAction(self.createAction('Quit', self.close))
        helpMenu = menubar.addMenu("Help")
        helpMenu.addAction(self.createAction('About', self.onAbout))

    def createAction(self, actionName, function):
        action = QAction(actionName, self)
        action.triggered.connect(function)
        return action

    def onAbout(self):
        try:
            self.widgetDict['aboutW'].show()
        except KeyError:
            self.widgetDict['aboutW'] = AboutWidget(self)
            self.widgetDict['aboutW'].show()

    def createDock(self, widgetClass, widgetName, widgetArea):
        widget = widgetClass(self.mainEngine, self.eventEngine)
        dock = QtGui.QDockWidget(widgetName)
        dock.setWidget(widget)
        dock.setObjectName(widgetName)
        dock.setFeatures(dock.DockWidgetFloatable | dock.DockWidgetMovable)
        self.addDockWidget(widgetArea, dock)
        return widget, dock

    def saveWindowSettings(self, settingName):
        settings = QSettings('ATSMain', settingName)
        settings.setValue('state', self.saveState())
        settings.setValue('geometry', self.saveGeometry())


class AboutWidget(QDialog):

    def __init__(self, parent=None):
        super(AboutWidget, self).__init__(parent)

        self.initUi()

    def initUi(self):
        self.setWindowTitle("About")

        text = """
            Developed by Programmer, For Traders
            """

        label = QLabel()
        label.setText(text)
        label.setMinimumWidth(500)

        vbox = QVBoxLayout()
        vbox.addWidget(label)

        self.setLayout(vbox)


if __name__ == '__main__':
    import qdarkstyle
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainWindow = ATSMain()
    mainWindow.showMaximized()
    sys.exit(app.exec_())
