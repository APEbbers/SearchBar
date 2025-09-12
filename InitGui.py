import FreeCAD as App
import FreeCADGui as Gui
from PySide.QtWidgets import QMainWindow, QToolBar, QMenu, QWidget, QDialog
from PySide.QtGui import QShortcut, QKeySequence, QCursor
from PySide.QtCore import Qt, Signal, QEvent, QObject

import MouseBar
import LoadChangeDialog

# Avoid garbage collection by storing the action in a global variable
wax = None
sea = None
tbr = None

ChangeDialogLoaded = False

# Define the translation
translate = App.Qt.translate


def QT_TRANSLATE_NOOP(context, text):
    return text

def addToolSearchBox():
    global wax, sea, tbr, ChangeDialogLoaded
    mw: QMainWindow = Gui.getMainWindow()
    cp = mw.centralWidget()
    vp: QWidget = cp.viewport()
    import SearchBox
    import MouseBar
    import LoadChangeDialog
    from MouseBar import EventInspector
    from PySide.QtWidgets import QToolBar
        
    if mw:
        if ChangeDialogLoaded is False:
            # Load the what changed dialog
            LoadChangeDialog.main()
        ChangeDialogLoaded = True
        
        # Activate the searchBar at the pointer module
        MouseBar.SearchBar_Pointer()
        
        mw.installEventFilter(EventInspector(mw))
        mw.centralWidget().installEventFilter(EventInspector(mw))
        vp.installEventFilter(EventInspector(mw))
        for child in vp.children():
            child.installEventFilter(EventInspector(mw))
        
        if sea is None:
            wax = SearchBox.SearchBoxFunction(mw)
        if tbr is None:
            tbr = QToolBar("SearchBar")  # QtGui.QDockWidget()
            # Include FreeCAD in the name so that one can find windows labeled with
            # FreeCAD easily in window managers which allow search through the list of open windows.
            tbr.setObjectName("SearchBar")
            tbr.addAction(wax)
        mw.addToolBar(tbr)
        tbr.show()
        return   

addToolSearchBox()
Gui.getMainWindow().workbenchActivated.connect(addToolSearchBox)



