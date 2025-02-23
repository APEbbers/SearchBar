import os
import FreeCAD as App
import FreeCADGui as Gui
import StyleMapping

# Define the translation
translate = App.Qt.translate


def loadAllWorkbenches():
    import FreeCADGui as Gui
    from PySide.QtGui import QLabel
    from PySide.QtCore import Qt, SIGNAL, Signal, QObject, QThread, QSize
    from PySide.QtGui import QIcon, QPixmap, QAction, QGuiApplication

    activeWorkbench = Gui.activeWorkbench().name()
    lbl = QLabel(translate("SearchBar", "Loading workbench … (…/…)"))
    lbl.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    # Get the stylesheet from the main window and use it for this form
    lbl.setStyleSheet("background-color: " + StyleMapping.ReturnStyleItem("Background_Color") + ";")

    # # Get the main window from FreeCAD
    # mw = Gui.getMainWindow()
    # # Center the widget
    # cp = QGuiApplication.screenAt(mw.pos()).geometry().center()
    # lbl.move(cp)

    lbl.show()
    lst = Gui.listWorkbenches()
    for i, wb in enumerate(lst):
        msg = translate("SearchBar", "Loading workbench ") + wb + " (" + str(i) + "/" + str(len(lst)) + ")"
        print(msg)
        lbl.setText(msg)
        geo = lbl.geometry()
        geo.setSize(lbl.sizeHint())
        lbl.setGeometry(geo)
        lbl.repaint()
        Gui.updateGui()  # Probably slower with this, because it redraws the entire GUI with all tool buttons changed etc. but allows the label to actually be updated, and it looks nice and gives a quick overview of all the workbenches…
        try:
            Gui.activateWorkbench(wb)
        except Exception:
            pass
    lbl.hide()
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

    serializedItemGroups = Serialize_SearchBar.serialize(gatherTools())
    # Todo: use wb and a specific encoding.
    with open(cachePath(), "w") as cache:
        cache.write(serializedItemGroups)
    # I prefer to systematically deserialize, instead of taking the original version,
    # this avoids possible inconsistencies between the original and the cache and
    # makes sure cache-related bugs are noticed quickly.
    import Serialize_SearchBar

    itemGroups = Serialize_SearchBar.deserialize(serializedItemGroups)
    print("SearchBox: Cache has been written.")
    return itemGroups


def readCacheTools():
    # Todo: use rb and a specific encoding.
    with open(cachePath(), "r") as cache:
        serializedItemGroups = cache.read()
    import Serialize_SearchBar

    itemGroups = Serialize_SearchBar.deserialize(serializedItemGroups)
    print("SearchBox: Tools were loaded from the cache.")
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
    from PySide import QtGui

    print("Refresh cached results")
    fw = QtGui.QApplication.focusWidget()
    if fw is not None:
        fw.clearFocus()
    reply = QtGui.QMessageBox.question(
        None,
        translate("SearchBar", "Load all workbenches?"),
        translate(
            "SearchBar",
            """Load all workbenches? This can cause FreeCAD to become unstable, and this "reload tools" feature contained a bug that crashed freecad systematically, so please make sure you save your work before. It\'s a good idea to restart FreeCAD after this operation.""",
        ),
        QtGui.QMessageBox.Yes,
        QtGui.QMessageBox.No,
    )
    if reply == QtGui.QMessageBox.Yes:
        refreshToolbars()
    else:
        print("cancelled")
