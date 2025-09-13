import FreeCAD as App
import FreeCADGui as Gui
import Parameters_SearchBar
from PySide.QtWidgets import QMainWindow, QToolBar, QMenu, QHBoxLayout, QWidget, QWidgetAction, QDialog, QVBoxLayout
from PySide.QtGui import QShortcut, QKeySequence, QCursor, QWindow,  QKeySequence
from PySide.QtCore import Qt, Signal, QEvent, QObject
import SearchBoxLight
import os
import StyleMapping_SearchBar

# Avoid garbage collection by storing the action in a global variable
wax = None
sea = None
tbr = None

# Define the translation
translate = App.Qt.translate

# Create the command
class SearchBar_Pointer:
    def GetResources(self):
        return {
            "Pixmap": os.path.join(Parameters_SearchBar.ICON_LOCATION, "Tango-System-search.svg"),  # the name of a svg file available in the resources
            "Accel": "S",
            "MenuText": "Pointer command",
            "ToolTip": "SearchBar pointer command",
        }

    def Activated(self):
        # Get the main window
        mw: QMainWindow = Gui.getMainWindow()
        # get the toolbar if it already exists
        toolbar = mw.findChild(QToolBar, "SearchBarAtMouse")
        # Get the cursor position
        pos = QCursor.pos()
        
        # If there is no toolbar, create and show it at the cursor
        if toolbar is None:
            toolbar = QToolBar("SearchBarAtMouse", mw)   
            toolbar.setFloatable(True)
            toolbar.setAllowedAreas(Qt.ToolBarArea.NoToolBarArea)
            toolbar.setOrientation(Qt.Orientation.Horizontal)
            toolbar.setWindowFlags(Qt.WindowType.FramelessWindowHint)
            action = ToolBarAction(mw)
            action = ToolBarAction(mw)
            toolbar.addAction(action)

            # Get the style from the main window and use it for this form
            palette = mw.palette()
            toolbar.setPalette(palette)
            Style = mw.style()
            toolbar.setStyle(Style)
            
            toolbar.move(pos.x()+10, pos.y()-10)
            toolbar.adjustSize()
            toolbar.show()
            return
        # If there is already a toolbar, show it at the cursor or hide it
        if toolbar is not None:
            if toolbar.isVisible() is False:
                toolbar.parent().parent().move(pos.x()+10, pos.y()-10)
                toolbar.parent().parent().show()
            else:
                toolbar.parent().parent().close()
            return
        return 

# Add the command
Gui.addCommand("SearchBar", SearchBar_Pointer())

# Create the toolbar action
class ToolBarAction(QWidgetAction):     
    toolbar = QToolBar()
        
    def __init__(self, parent):
        super(ToolBarAction, self).__init__(parent)

        # Define a new searchbar widget
        sea = SearchBoxLight.SearchBoxLight(
            getItemGroups=lambda: __import__("GetItemGroups").getItemGroups(),
            getToolTip=lambda groupId, setParent: __import__("GetItemGroups").getToolTip(groupId, setParent),
            getItemDelegate=lambda: __import__("IndentedItemDelegate").IndentedItemDelegate(),
        )
        sea.resultSelected.connect(
            lambda index, groupId: __import__("GetItemGroups").onResultSelected(index, groupId)
        )
        
        
        toolbar = QToolBar()
        toolbar.setObjectName("SearchBarAtMouse")
        toolbar.addWidget(sea)
        self.toolbar = toolbar
        
        layout = QHBoxLayout()
        self.widget = QWidget()
        layout.addWidget(self.toolbar)
        self.widget.setLayout(layout)

        self.setDefaultWidget(self.widget)
        return

# Create an event filter to install and detect the shortcut key
class EventInspector(QObject):
    
    def __init__(self, parent):
        super(EventInspector, self).__init__(parent)

    def eventFilter(self, obj, event):
        # Get the main window and the toolbar
        mw: QMainWindow = Gui.getMainWindow()
        toolbar = mw.findChild(QToolBar, "SearchBarAtMouse")
        
        # Get the shortcut key
        ShortcutKey = "S"
        CustomShortCuts = App.ParamGet(
                "User parameter:BaseApp/Preferences/Shortcut"
            )
        if "SearchBar" in CustomShortCuts.GetStrings():
            ShortcutKey = CustomShortCuts.GetString("SearchBar")
        # Get a modifier key if there is one
        modifier = None
        key = QKeySequence(ShortcutKey)
        if len(ShortcutKey.split("+")) > 1:
            if ShortcutKey.split("+")[0].lower() == "alt":
                modifier = Qt.KeyboardModifier.AltModifier
            if ShortcutKey.split("+")[0].lower() == "ctrl":
                modifier = Qt.KeyboardModifier.ControlModifier
            if ShortcutKey.split("+")[0].lower() == "shift":
                modifier = Qt.KeyboardModifier.ShiftModifier
            key = QKeySequence(ShortcutKey.split("+")[1])
        
        # If there is a key press event, continue
        if event.type() == QEvent.Type.KeyPress:
            # check if there is a modifier key that matches the modifier key in the shortcut
            if modifier is not None:
                if event.modifiers() and modifier:
                    if event.key() == key:
                        Gui.runCommand("SearchBar")
                        return True
            # If there is only one key, continue here
            else:
                if event.key() == key:
                    Gui.runCommand("SearchBar")
                    return True
        # If there is a mouse click, check if the toolbar is under the cursor
        # If not, close it
        if (
            event.type() == QEvent.Type.MouseButtonRelease 
            or event.type() == QEvent.Type.GraphicsSceneMouseRelease
            or (event.type() == QEvent.Type.KeyPress and event.key() == Qt.Key.Key_Escape) 
            ):
            try:
                if toolbar.underMouse() is False:
                    toolbar.parent().parent().close()
            except Exception:
                pass
            return True
        return False
    
   