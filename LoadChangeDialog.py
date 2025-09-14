import FreeCAD as App
import FreeCADGui as Gui
import os
import sys


from PySide.QtGui import QIcon, QPixmap, QAction, QGuiApplication, QTextDocument, QScreen
from PySide.QtWidgets import QCheckBox, QMainWindow, QTextEdit
from PySide.QtCore import QSize, Qt, QObject, SIGNAL

import StandardFunctions_SearchBar as StandardFunctions
import Parameters_SearchBar
import StyleMapping_SearchBar

# Get the resources
pathIcons = Parameters_SearchBar.ICON_LOCATION
pathUI = Parameters_SearchBar.UI_LOCATION
pathImages = Parameters_SearchBar.IMAGE_LOCATION
sys.path.append(pathIcons)
sys.path.append(pathUI)
sys.path.append(pathImages)

# import graphical created Ui. (With QtDesigner or QtCreator)
import ui_ChangeDialog as ui_ChangeDialog

# Define the translation
translate = App.Qt.translate

class LoadDialog(ui_ChangeDialog.Ui_Form, QObject):
    
    # The text for the changelog (markdown)
    text = ("# New in SearchBar version 1.6.0:  \n"
        + "###\n"
        + "## SearchBar at mouse cursor  \n"
        + "With this release, the searchbar can be shown at cursor by pressing a shortcut key. The default shortcut is 'S'.\n"
        + "To show the searchbar at the cursor, press 'S'. To hide it, press 'S' again.  \n"
        + f'<img src=\"{os.path.join(pathImages, "SearchBar at pointer.png")}\"/>  \n'
        + "### Changing the shortcut  \n"
        + "To change the shortcut, go to Tools->Customize.....  \n"
        + "The customize menu of FreeCAD will popup. On the keyboard tab look for the category 'SearchBar'. \n"
        + "The pointer command will be shown. Here you can set your preferred shortcut.  \n"
        + f'<img src=\"{os.path.join(pathImages, "Change shortcut.png")}\" width=500/>\n')
    
    # Enter the version for which the form must show on startup
    WhatsNewVersion = "1.6"
    
    # Get the main window from FreeCAD
    mw = Gui.getMainWindow()
    
    def __init__(self):

        # Makes "self.on_CreateBOM_clicked" listen to the changed control values instead initial values
        super(LoadDialog, self).__init__()
        
        mw: QMainWindow = self.mw

        # # this will create a Qt widget from our ui file
        self.form = Gui.PySideUic.loadUi(os.path.join(pathUI, "ChangeDialog.ui"))
        
        # Set the window on top
        self.form.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        # Position the dialog in front of FreeCAD
        centerPoint = mw.screen().geometry().center()
        Rectangle = self.form.frameGeometry()
        Rectangle.moveCenter(centerPoint)
        self.form.move(Rectangle.topLeft())

        # Set the size of the dialog
        self.form.setMinimumSize(QSize(600,600))
        self.form.adjustSize()

        # Set the window title
        self.form.setWindowTitle(translate("Searchbar", "Searchbar"))

        # Get the style from the main window and use it for this form
        palette = mw.palette()
        self.form.setPalette(palette)
        Style = mw.style()
        self.form.setStyle(Style)
        self.form.setStyleSheet("background-color: " + StyleMapping_SearchBar.ReturnStyleItem("Background_Color") + ";")
        
        # Set the properties for the textEdit
        self.form.textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.form.textEdit.setReadOnly(True)
        self.form.textEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.form.textEdit.setStyleSheet("background-color: " + StyleMapping_SearchBar.ReturnStyleItem("Background_Color") + ";")
        
        # Set the checkbox
        if Parameters_SearchBar.DO_NOT_SHOW_AGAIN is True:
            self.form.DoNotShowAgain.setCheckState(Qt.CheckState.Checked)
        else:
            self.form.DoNotShowAgain.setCheckState(Qt.CheckState.Unchecked)
        self.form.DoNotShowAgain.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        # Connect do not show again checkbox
        def DoNotShowAgain():
            self.on_DoNotShowAgain_clicked()

        self.form.DoNotShowAgain.connect(self.form.DoNotShowAgain, SIGNAL("clicked()"), DoNotShowAgain)
        
        # Set the text
        textBrowser: QTextEdit= self.form.textEdit
        textBrowser.setMarkdown(self.text)
        return
    
    def on_DoNotShowAgain_clicked(self):
        if self.form.DoNotShowAgain.checkState() is Qt.CheckState.Checked:
            Parameters_SearchBar.Settings.SetBoolSetting("DoNotShowAgain", True)
            Parameters_SearchBar.DO_NOT_SHOW_AGAIN = True
        if self.form.DoNotShowAgain.checkState() is Qt.CheckState.Unchecked:
            Parameters_SearchBar.Settings.SetBoolSetting("DoNotShowAgain", False)
            Parameters_SearchBar.DO_NOT_SHOW_AGAIN = False
        return
    

def main():
    # The version for which this form must be shown. Is set at the top of this document
    versionToShow = LoadDialog.WhatsNewVersion
    
    # Get the current version
    PackageXML = os.path.join(os.path.dirname(__file__), "package.xml")
    CurrentVersion = StandardFunctions.ReturnXML_Value(
        PackageXML, "version"
    ).split(".")
    
    versionList = versionToShow.split(".")
    versionString = ""
    
    for i in range(len(versionList)):
        if versionList[i] == CurrentVersion[i]:
            versionString = versionString + versionList[i] + "."
    if versionString.endswith("."):
        versionString = versionString[:-1]
        
    if versionString == versionToShow and Parameters_SearchBar.DO_NOT_SHOW_AGAIN is False:
        # Get the form
        Dialog = LoadDialog().form
        # Show the form
        Dialog.show()

    return