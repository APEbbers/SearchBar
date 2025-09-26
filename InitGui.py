import FreeCAD as App
import FreeCADGui as Gui
from PySide.QtWidgets import QMainWindow, QToolBar, QMenu, QWidget, QWidgetAction, QDialog, QHBoxLayout
from PySide.QtGui import QShortcut, QKeySequence, QCursor
from PySide.QtCore import Qt, Signal, QEvent, QObject
import os
import Parameters_SearchBar

# Avoid garbage collection by storing the action in a global variable
wax = None
sea = None
tbr = None

ChangeDialogLoaded = False

# Define the translation
translate = App.Qt.translate

PrefLoaded = False
Gui.addIconPath(Parameters_SearchBar.ICON_LOCATION)
Gui.addResourcePath(Parameters_SearchBar.ICON_LOCATION)
PreferenceUI = os.path.join(Parameters_SearchBar.UI_LOCATION, "PreferencesUI_SearchBar.ui")
Gui.addPreferencePage(PreferenceUI, "SearchBar")


def QT_TRANSLATE_NOOP(context, text):
    return text

class SearchBar(Gui.Workbench):
    # This is needed to avoid crashes
    def GetClassName(self):
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"

    def addToolSearchBox():
        global wax, sea, tbr, ChangeDialogLoaded
        mw: QMainWindow = Gui.getMainWindow()
        cp = mw.centralWidget()
        vp: QWidget = cp.viewport()
        import SearchBox
        import MouseBar
        import LoadChangeDialog_SearchBar
        from MouseBar import EventInspector_SB
        from PySide.QtWidgets import QToolBar
        import Parameters_SearchBar
        
        # Reset the DoNotShowAgain parameter if wanted
        if Parameters_SearchBar.Settings.GetBoolSetting("ShowChangeDialog") is True:
            Parameters_SearchBar.Settings.SetStringSetting("DoNotShowAgain", " ")
            Parameters_SearchBar.DO_NOT_SHOW_AGAIN = " "
            
        if mw:
            if ChangeDialogLoaded is False:
                # Load the what changed dialog
                LoadChangeDialog_SearchBar.main()
            ChangeDialogLoaded = True
            
            # If the mousebar is enabled in preferences, enable it.
            if Parameters_SearchBar.Settings.GetBoolSetting("EnableMouseBar", True) is True:
                # Activate the searchBar at the pointer module
                MouseBar.SearchBar_Pointer()
                
                mw.installEventFilter(EventInspector_SB(mw))
                mw.centralWidget().installEventFilter(EventInspector_SB(mw))
                vp.installEventFilter(EventInspector_SB(mw))
                for child in vp.children():
                    child.installEventFilter(EventInspector_SB(mw))
            
            # if the toolbars are enabled in preferences, load them
            if Parameters_SearchBar.Settings.GetBoolSetting("EnableToolbars", True) is True:          
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

SearchBar.addToolSearchBox()
Gui.getMainWindow().workbenchActivated.connect(SearchBar.addToolSearchBox)



