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

class EventInspector(QObject):
    def __init__(self, parent):
        super(EventInspector, self).__init__(parent)
        self.tbr = self.ShowSearchBoxAtCursor()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Escape:
                print("Killing")
                self.deleteLater()
            elif event.key() == Qt.Key.Key_S:
                # pos = QCursor.pos()
                self.setMouseTracking(True)
                self.tbr.mapToGlobal(event.pos())
    
    def ShowSearchBoxAtCursor(self):
        global wax, sea, tbr
        mw = Gui.getMainWindow()
        tbr = customToolbar(text="mouseMenu")
        import SearchBox

        if mw:
            if sea is None:
                wax = SearchBox.SearchBoxFunction(mw)
            if tbr is None:
                tbr = QToolBar("SearchBar")  # QtGui.QDockWidget()
                # Include FreeCAD in the name so that one can find windows labeled with
                # FreeCAD easily in window managers which allow search through the list of open windows.
                tbr.setObjectName("SearchBar")
                tbr.addAction(wax)
        return tbr
    
class customToolbar(QToolBar):
    keyPressed = Signal(QEvent)
    
    def __init__(self, parent, text):
        super(customToolbar, self).__init__(parent)
        self.keyPressed.connect(self.on_key)
        
    # def keyPressEvent(self, event):
    #     # if event.key() == Qt.Key.Key_Escape:
    #     #     print("Killing")
    #     #     self.deleteLater()
    #     # elif event.key() == Qt.Key.Key_S:
    #     #     # pos = QCursor.pos()
    #     #     self.setMouseTracking(True)
    #     #     self.exec_(self.mapToGlobal(event.pos()))
    #     self.keyPressed.emit(event)
    #     event.accept()
        
    # def on_key(self, event):
    #     print('event received @ myDialog')
    #     if event.key() == Qt.Key.Key_0:
    #         print(0)