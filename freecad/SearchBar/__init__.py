import FreeCAD as App
import FreeCADGui as Gui

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
    from PySide.QtWidgets import QToolBar
    from PySide.QtGui import QShortcut, QKeySequence

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
        tbr.show()
        return


addToolSearchBox()
Gui.getMainWindow().workbenchActivated.connect(addToolSearchBox)
