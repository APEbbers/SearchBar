from tkinter import Menubutton
from turtle import isvisible
import FreeCAD as App
import FreeCADGui as Gui
from PySide6.QtWidgets import QMainWindow, QToolBar, QMenu, QHBoxLayout, QWidget, QWidgetAction
from PySide6.QtGui import QShortcut, QKeySequence, QCursor
from PySide6.QtCore import Qt, Signal, QEvent, QObject
# Avoid garbage collection by storing the action in a global variable
wax = None
sea = None
tbr = None

# Define the translation
translate = App.Qt.translate

class EventInspector(QObject):
    
    def __init__(self, parent):
        super(EventInspector, self).__init__(parent)

    def eventFilter(self, obj, event):
        mw: QMainWindow = Gui.getMainWindow()
        toolbar = mw.findChild(QToolBar, "SearchBarAtMouse")
        
        if event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_S:
                toolbar = QToolBar("SearchBarAtMouse", mw)   
                toolbar.setFloatable(True)
                toolbar.setAllowedAreas(Qt.ToolBarArea.NoToolBarArea)
                toolbar.setOrientation(Qt.Orientation.Horizontal)
                toolbar.setWindowFlags(Qt.WindowType.FramelessWindowHint)
                action = ToolBarAction(mw)
                toolbar.addAction(action)

                pos = QCursor.pos()
                toolbar.move(pos.x()+10, pos.y()-10)
                toolbar.adjustSize()
                toolbar.show()
                return True
        if event.type() == QEvent.Type.MouseButtonPress:
            try:
                toolbar = mw.findChild(QToolBar, "SearchBarAtMouse")
                if toolbar.underMouse() is False:
                    toolbar.parent().parent().close()
            except Exception as e:
                print(e)
                pass
            return True
        return False

class ToolBarAction(QWidgetAction):
    import SearchBox
    mw = Gui.getMainWindow()
    action: QWidgetAction = SearchBox.SearchBoxFunction(mw)
        
    toolbar = QToolBar()
    toolbar.setObjectName("SearchBarAtMouse")
    toolbar.addAction(action)
    
    def __init__(self, parent):
        super(ToolBarAction, self).__init__(parent)
        
        layout = QHBoxLayout()
        self.widget = QWidget()
        layout.addWidget(self.toolbar)
        self.widget.setLayout(layout)

        self.setDefaultWidget(self.widget)
        return
    