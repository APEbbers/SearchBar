import FreeCAD as App
import FreeCADGui as Gui
import os
import sys


from PySide6.QtGui import QIcon, QPixmap, QAction, QGuiApplication, QTextDocument
from PySide6.QtWidgets import QCheckBox, QTextEdit
from PySide6.QtCore import Qt, QObject

import StandardFunctions_SearchBar as StandardFunctions
import Parameters_SearchBar

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
    
    # Enter the version for which the form must show on startup
    WhatsNewVersion = "1.6"
    
    # Get the main window from FreeCAD
    mw = Gui.getMainWindow()
    
    def __init__(self):

        # Makes "self.on_CreateBOM_clicked" listen to the changed control values instead initial values
        super(LoadDialog, self).__init__()
        
        mw = self.mw

        # # this will create a Qt widget from our ui file
        self.form = Gui.PySideUic.loadUi(os.path.join(pathUI, "ChangeDialog.ui"))
        
        self.form.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        
        # Set the window title
        self.form.setWindowTitle(translate("Searchbar", "What's new?"))

        # Get the style from the main window and use it for this form
        palette = mw.palette()
        self.form.setPalette(palette)
        Style = mw.style()
        self.form.setStyle(Style)
        
        if Parameters_SearchBar.DO_NOT_SHOW_AGAIN is True:
            self.form.DoNotShowAgain.setCheckState(Qt.CheckState.Checked)
        else:
            self.form.DoNotShowAgain.setCheckState(Qt.CheckState.Unchecked)
        
        # Connect do not show again checkbox
        self.form.DoNotShowAgain.clicked.connect(self.on_DoNotShowAgain_clicked)
        
        textBrowser: QTextEdit= self.form.textEdit
        # htmlFile = open(os.path.join(pathchangelog, "What's new.html")).read()
        tekst = f"""
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
        <html>
        <b>New in SearchBar version 1.6.0:</b>
        <br/>
        <p>
        With this release, the searchbar can be shown at cursor by pressing a shortcut key. The default shortcut is 'S'.
        To show the searchbar at the cursor, press 'S'. To hide it, press 'S' again.
        </p>
        <img src=\":/Images/Resources/Images/2025-09-11 Change shortcut.png\" />
        <p>
        <br/>
        The shortcut can be changed. To do this, go to Tools->Customize.....
        The customize menu of FreeCAD will popup.  
        On the keyboard tab look for the catagory 'SearchBar'. 
        The pointer command will be shown. Here you can set your prefferred shortcut.
        </p></html>
        """

        textBrowser.setHtml(tekst)
        return
    
    def on_DoNotShowAgain_clicked(self):
        Parameters_SearchBar.Settings.SetBoolSetting("DoNotShowAgain", self.form.DoNotShowAgain.isChecked())
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
        
    print(versionString)
    print(versionToShow)
        
    if versionString == versionToShow:
        # Get the form
        Dialog = LoadDialog().form
        # Show the form
        Dialog.show()

    return