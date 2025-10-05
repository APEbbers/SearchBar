import os
import FreeCAD as App
import FreeCADGui as Gui
import StyleMapping_SearchBar

import FreeCADGui as Gui
from PySide.QtWidgets import QLabel, QProgressBar, QApplication
from PySide.QtCore import Qt, SIGNAL, Signal, QObject, QThread, QSize
from PySide.QtGui import QIcon, QPixmap, QAction, QGuiApplication

# Define the translation
translate = App.Qt.translate

# Define a QProgressBar as a counter dialog
progressBar = QProgressBar(minimum=0, value=0)
progressBar.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowStaysOnTopHint)
progressBar.setMinimumSize(300, 20)

# Get the stylesheet from the main window and use it for this form
progressBar.setStyleSheet("background-color: " + StyleMapping_SearchBar.ReturnStyleItem("Background_Color") + ";")

def loadAllWorkbenches():
    import FreeCADGui as Gui
    from PySide.QtWidgets import QLabel, QProgressBar, QApplication
    from PySide.QtCore import Qt, SIGNAL, Signal, QObject, QThread, QSize
    from PySide.QtGui import QIcon, QPixmap, QAction, QGuiApplication

    activeWorkbench = Gui.activeWorkbench().name()

    # # Define a QProgressBar as a counter dialog
    # progressBar = QProgressBar(minimum=0, value=0)
    # progressBar.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowStaysOnTopHint)
    # progressBar.setMinimumSize(300, 20)

    # # Get the stylesheet from the main window and use it for this form
    # progressBar.setStyleSheet("background-color: " + StyleMapping_SearchBar.ReturnStyleItem("Background_Color") + ";")

    # # Get the main window from FreeCAD
    # mw = Gui.getMainWindow()
    # # Center the widget
    # cp = QGuiApplication.screenAt(mw.pos()).geometry().center()
    # lbl.move(cp)

    progressBar.show()
    lst = Gui.listWorkbenches()
    progressBar.setMaximum(len(lst)+1)
    for i, wb in enumerate(lst):
        msg = translate("SearchBar", "Loading workbench ") + wb + " (" + str(i + 1) + "/" + str(len(lst)) + ")"
        print(msg)
        progressBar.setFormat(msg)
        progressBar.setValue(i)
        Gui.updateGui()  # Probably slower with this, because it redraws the entire GUI with all tool buttons changed etc. but allows the label to actually be updated, and it looks nice and gives a quick overview of all the workbenches…
        try:
            Gui.activateWorkbench(wb)
        except Exception:
            pass
    # progressBar.close()
    Gui.activateWorkbench(activeWorkbench)
    return


def cachePath():
    return os.path.join(App.getUserAppDataDir(), "Cache_SearchBarMod")


def gatherTools():
    itemGroups = []
    import SearchResults

    for providerName, provider in SearchResults.resultProvidersCached.items():
        itemGroups = itemGroups + provider()
    return itemGroups


def writeCacheTools():
    import Serialize_SearchBar
    msg = translate("SearchBar", "Writing to cache ")
    print(msg)
    progressBar.setFormat(msg)
    progressBar.setValue(progressBar.value()+1)
    serializedItemGroups = Serialize_SearchBar.serialize(gatherTools())
    # Todo: use wb and a specific encoding.
    with open(cachePath(), "w") as cache:
        cache.write(serializedItemGroups)
    # I prefer to systematically deserialize, instead of taking the original version,
    # this avoids possible inconsistencies between the original and the cache and
    # makes sure cache-related bugs are noticed quickly.
    import Serialize_SearchBar

    itemGroups = Serialize_SearchBar.deserialize(serializedItemGroups)
    progressBar.setValue(progressBar.value()+1)
    print("SearchBox: Data file is created.")
    progressBar.close()
    return itemGroups


def readCacheTools():
    # Todo: use rb and a specific encoding.
    with open(cachePath(), "r") as cache:
        serializedItemGroups = cache.read()
    import Serialize_SearchBar

    itemGroups = Serialize_SearchBar.deserialize(serializedItemGroups)
    print("SearchBox: Tools are loaded.")
    return itemGroups


def refreshToolbars(doLoadAllWorkbenches=True):
    if doLoadAllWorkbenches:
        loadAllWorkbenches()
        return writeCacheTools()
    else:
        try:
            return readCacheTools()
        except:
            return writeCacheTools()


def refreshToolsAction():
    from PySide.QtWidgets import QApplication, QMessageBox
    from PySide.QtCore import Qt

    print("Refresh data file")
    msgBox = QMessageBox()
    msgBox.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    # Get the main window from FreeCAD
    mw = Gui.getMainWindow()
    reply = msgBox.question(
        mw,
        translate("SearchBar", "Load all workbenches?"),
        translate(
            "SearchBar",
            """Load all workbenches? This can cause FreeCAD to become unstable. Please make sure you save your work first.\nIt is a advised to restart FreeCAD after this operation.""",
        ),
        QMessageBox.Yes,
        QMessageBox.No,
    )
    if reply == QMessageBox.Yes:
        refreshToolbars()
    else:
        print("cancelled")
