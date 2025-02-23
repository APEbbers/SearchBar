import FreeCAD as App
import FreeCADGui as Gui

from PySide.QtWidgets import QWidgetAction, QToolBar, QMainWindow, QWidget, QDialog
from PySide.QtGui import QCursor, QShortcut, QKeySequence, QAction
from PySide.QtCore import Qt

# Avoid garbage collection by storing the action in a global variable
wax = None
sea = None
tbr = None

# Define the translation
translate = App.Qt.translate


def QT_TRANSLATE_NOOP(context, text):
    return text


# class SearchBox:
mw = Gui.getMainWindow()


def addToolSearchBox():
    global wax, sea, tbr
    mw = Gui.getMainWindow()
    import SearchBox
    from PySide.QtWidgets import QToolBar

    if mw:
        if sea is None:
            wax = SearchBox.SearchBoxFunction()
        if tbr is None:
            tbr = QToolBar("SearchBar")  # QtGui.QDockWidget()
            # Include FreeCAD in the name so that one can find windows labeled with
            # FreeCAD easily in window managers which allow search through the list of open windows.
            tbr.setObjectName("SearchBar")
            tbr.addAction(wax)
        mw.addToolBar(tbr)
        tbr.show()

        # self.shortcut = QShortcut(QKeySequence("Alt+R"), self)
        # self.shortcut.activated.connect(self.AddPointerBox)
        # self.AddPointerBox()
        print("shortcut toggled")
    return


def AddPointerBox():
    import SearchBox

    print("shortcut toggled")

    Dialog = QDialog()
    cursor = QCursor()
    cursorPosition = cursor.pos()

    Dialog.geometry().setX(cursorPosition.x())
    Dialog.geometry().setY(cursorPosition.y())

    Action = SearchBox.SearchBoxFunction()
    Dialog.addAction(Action)

    Dialog.show()
    return


addToolSearchBox()
Gui.getMainWindow().workbenchActivated.connect(addToolSearchBox)
