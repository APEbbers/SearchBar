import FreeCAD as App
import FreeCADGui as Gui
from PySide6.QtWidgets import QToolBar, QMenu
from PySide6.QtGui import QShortcut, QKeySequence, QCursor
from PySide6.QtCore import Qt, Signal, QEvent, QObject

# Avoid garbage collection by storing the action in a global variable
wax = None
sea = None
tbr = None

# Define the translation
translate = App.Qt.translate


def QT_TRANSLATE_NOOP(context, text):
    return text


def addToolSearchBox():
    global wax, sea, tbr
    mw = Gui.getMainWindow()
    import SearchBox
    from EventFilters import EventInspector
    from PySide6.QtWidgets import QToolBar
    
    if mw:
        if sea is None:
            wax = SearchBox.SearchBoxFunction(mw)
        if tbr is None:
            tbr = QToolBar("SearchBar")  # QtGui.QDockWidget()
            # Include FreeCAD in the name so that one can find windows labeled with
            # FreeCAD easily in window managers which allow search through the list of open windows.
            tbr.setObjectName("SearchBar")
            tbr.addAction(wax)
        mw.addToolBar(tbr)
        mw.installEventFilter(EventInspector(mw))
        tbr.show()
        return
    
# def ShowSearchBoxAtCursor():
#     global wax, sea, tbr
#     mw = Gui.getMainWindow()
#     tbr = customToolbar("mouseMenu")
#     import SearchBox

#     if mw:
#         if sea is None:
#             wax = SearchBox.SearchBoxFunction(mw)
#         if tbr is None:
#             tbr = QToolBar("SearchBar")  # QtGui.QDockWidget()
#             # Include FreeCAD in the name so that one can find windows labeled with
#             # FreeCAD easily in window managers which allow search through the list of open windows.
#             tbr.setObjectName("SearchBar")
#             tbr.addAction(wax)
#         return
    

addToolSearchBox()
# ShowSearchBoxAtCursor()
Gui.getMainWindow().workbenchActivated.connect(addToolSearchBox)

