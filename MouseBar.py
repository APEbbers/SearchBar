from tkinter import Menubutton
from turtle import isvisible
import FreeCAD as App
import FreeCADGui as Gui
from PySide6.QtWidgets import QToolBar, QMenu, QHBoxLayout, QWidget, QWidgetAction
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
        mw = Gui.getMainWindow()
        
        if event.type() == QEvent.Type.KeyPress:
            menu = QMenu("test", parent=mw)            
            if event.key() == Qt.Key.Key_S:
                pos = QCursor.pos()
                action = ToolBarAction(mw)
                menu.addAction(action)
                action.setEnabled(True)
                menu.exec_(menu.mapToGlobal(pos))
                return True
        return False

class ToolBarAction(QWidgetAction):
    import SearchBox
    mw = Gui.getMainWindow()
    action: QWidgetAction = SearchBox.SearchBoxFunction(mw)
        
    toolbar = QToolBar()
    toolbar.setObjectName("mouseMenu")
    toolbar.addAction(action)
    
    def __init__(self, parent):
        super(ToolBarAction, self).__init__(parent)
        
        layout = QHBoxLayout()
        self.widget = QWidget()
        layout.addWidget(self.toolbar)
        self.widget.setLayout(layout)

        self.setDefaultWidget(self.widget)
        return
    