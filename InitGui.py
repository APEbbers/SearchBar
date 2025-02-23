import FreeCAD as App
import FreeCADGui as Gui

from PySide6.QtWidgets import QWidgetAction, QToolBar, QMainWindow, QWidget, QDialog
from PySide6.QtGui import QCursor, QShortcut, QKeySequence, QAction
from PySide6.QtCore import Qt

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


def SearchBoxFunction():
    import SearchBoxLight

    global wax, sea, tbr
    mw = Gui.getMainWindow()

    if mw:
        if sea is None:
            sea = SearchBoxLight.SearchBoxLight(
                getItemGroups=lambda: __import__("GetItemGroups").getItemGroups(),
                getToolTip=lambda groupId, setParent: __import__("GetItemGroups").getToolTip(groupId, setParent),
                getItemDelegate=lambda: __import__("IndentedItemDelegate").IndentedItemDelegate(),
            )
            sea.resultSelected.connect(
                lambda index, groupId: __import__("GetItemGroups").onResultSelected(index, groupId)
            )

        if wax is None:
            wax = QWidgetAction(None)
            wax.setWhatsThis(
                translate(
                    "SearchBar",
                    "Use this search bar to find tools, document objects, preferences and more",
                )
            )

        sea.setWhatsThis(
            translate(
                "SearchBar",
                "Use this search bar to find tools, document objects, preferences and more",
            )
        )
        wax.setDefaultWidget(sea)
    return wax


addToolSearchBox()
Gui.getMainWindow().workbenchActivated.connect(addToolSearchBox)
