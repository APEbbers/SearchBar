# *************************************************************************
# *                                                                       *
# * Copyright (c) 2019-2024 Paul Ebbers                                   *
# *                                                                       *
# * This program is free software; you can redistribute it and/or modify  *
# * it under the terms of the GNU Lesser General Public License (LGPL)    *
# * as published by the Free Software Foundation; either version 3 of     *
# * the License, or (at your option) any later version.                   *
# * for detail see the LICENCE text file.                                 *
# *                                                                       *
# * This program is distributed in the hope that it will be useful,       *
# * but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# * GNU Library General Public License for more details.                  *
# *                                                                       *
# * You should have received a copy of the GNU Library General Public     *
# * License along with this program; if not, write to the Free Software   *
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# * USA                                                                   *
# *                                                                       *
# *************************************************************************
import FreeCAD as App
import FreeCADGui as Gui
import os
from PySide.QtGui import QIcon, QPixmap, QAction
from PySide.QtWidgets import (
    QListWidgetItem,
    QTableWidgetItem,
    QListWidget,
    QTableWidget,
    QToolBar,
    QToolButton,
    QComboBox,
    QPushButton,
    QMenu,
    QWidget,
    QMainWindow,
)
from PySide.QtCore import Qt, SIGNAL, Signal, QObject, QThread
import sys
import json
from datetime import datetime
import shutil
import Standard_Functions_RIbbon as StandardFunctions
import Parameters_Ribbon
import webbrowser
import time

# Get the resources
pathIcons = Parameters_Ribbon.ICON_LOCATION
pathStylSheets = Parameters_Ribbon.STYLESHEET_LOCATION
pathUI = Parameters_Ribbon.UI_LOCATION
pathBackup = Parameters_Ribbon.BACKUP_LOCATION
sys.path.append(pathIcons)
sys.path.append(pathStylSheets)
sys.path.append(pathUI)
sys.path.append(pathBackup)


def ReturnStyleItem(ControlName, ShowCustomIcon=False, IgnoreOverlay=False):
    """
    Enter one of the names below:

    ControlName (string):
        "Background_Color" returns string,
        "Border_Color" returns string,
        "FontColor" returns string,
        "FontColor" returns string,
    """
    # define a result holder and a dict for the StyleMapping file
    result = "none"

    # Get the current stylesheet for FreeCAD
    FreeCAD_preferences = App.ParamGet("User parameter:BaseApp/Preferences/MainWindow")
    currentStyleSheet = FreeCAD_preferences.GetString("StyleSheet")
    IsInList = False
    for key, value in StyleMapping_default["Stylesheets"].items():
        if key == currentStyleSheet:
            IsInList = True
            break
    if IsInList is False:
        currentStyleSheet = "none"

    try:
        result = StyleMapping_default["Stylesheets"][currentStyleSheet][ControlName]
        if result == "" or result is None:
            result = StyleMapping_default["Stylesheets"][""][ControlName]
        return result
    except Exception as e:
        print(e)
        return None


def ReturnColor(ColorType="Background_Color"):
    mw: QMainWindow = Gui.getMainWindow()
    palette = mw.style().standardPalette()
    # Get the color
    Color = palette.base().color().toTuple()  # RGBA tupple
    if ColorType == "Border_Color":
        Color = palette.buttonText().color().toTuple()
    if ColorType == "Background_Color_Hover":
        Color = palette.highlight().color().toTuple()

    HexColor = StandardFunctions.ColorConvertor(Color, Color[3] / 255, True, False)

    return HexColor


def ReturnFontColor():
    fontColor = "#000000"
    IsDarkTheme = DarkMode()

    if IsDarkTheme is True:
        fontColor = "#ffffff"

    return fontColor


def DarkMode():
    import xml.etree.ElementTree as ET
    import os

    # Define the standard result
    IsDarkTheme = False

    # Get the current stylesheet for FreeCAD
    FreeCAD_preferences = App.ParamGet("User parameter:BaseApp/Preferences/MainWindow")
    currentStyleSheet = FreeCAD_preferences.GetString("StyleSheet")

    path = os.path.dirname(__file__)
    # Get the folder with add-ons
    for i in range(2):
        # Starting point
        path = os.path.dirname(path)

    # Go through the sub-folders
    for root, dirs, files in os.walk(path):
        for name in dirs:
            # if the current stylesheet matches a sub directory, try to geth the pacakgexml
            if currentStyleSheet.replace(".qss", "").lower() in name.lower():
                try:
                    packageXML = os.path.join(path, name, "package.xml")

                    # Get the tree and root of the xml file
                    tree = ET.parse(packageXML)
                    treeRoot = tree.getroot()

                    # Get all the tag elements
                    elements = []
                    namespaces = {"i": "https://wiki.freecad.org/Package_Metadata"}
                    elements = treeRoot.findall(".//i:content/i:preferencepack/i:tag", namespaces)

                    # go throug all tags. If 'dark' in the element text, this is a dark theme
                    for element in elements:
                        if "dark" in element.text.lower():
                            IsDarkTheme = True
                            break
                except Exception:
                    continue

    return IsDarkTheme


StyleMapping_default = {
    "Stylesheets": {
        "": {
            "Background_Color": "#f0f0f0",
            "Background_Color_Hover": "#ced4da",
            "Border_Color": "#646464",
            "FontColor": ReturnFontColor(),
        },
        "none": {
            "Background_Color": "none",
            "Background_Color_Hover": "#48a0f8",
            "Border_Color": ReturnColor("Border_Color"),
            "FontColor": ReturnFontColor(),
        },
        "FreeCAD Dark.qss": {
            "Background_Color": "#333333",
            "Background_Color_Hover": "#48a0f8",
            "Border_Color": "#ffffff",
            "FontColor": "#ffffff",
        },
        "FreeCAD Light.qss": {
            "Background_Color": "#f0f0f0",
            "Background_Color_Hover": "#48a0f8",
            "Border_Color": "#646464",
            "FontColor": "#000000",
        },
        "OpenLight.qss": {
            "Background_Color": "#dee2e6",
            "Background_Color_Hover": "#a5d8ff",
            "Border_Color": "#1c7ed6",
            "FontColor": "#000000",
        },
        "OpenDark.qss": {
            "Background_Color": "#212529",
            "Background_Color_Hover": "#1f364d",
            "Border_Color": "#264b69",
            "FontColor": "#ffffff",
        },
        "Behave-dark.qss": {
            "Background_Color": "#232932",
            "Background_Color_Hover": "#557bb6",
            "Border_Color": "#3a7400",
            "FontColor": ReturnFontColor(),
        },
        "ProDark.qss": {
            "Background_Color": "#333333",
            "Background_Color_Hover": "#557bb6",
            "Border_Color": "#adc5ed",
            "FontColor": ReturnFontColor(),
        },
        "Darker.qss": {
            "Background_Color": "#444444",
            "Background_Color_Hover": "#4aa5ff",
            "Border_Color": "#696968",
            "FontColor": ReturnFontColor(),
        },
        "Light-modern.qss": {
            "Background_Color": "#f0f0f0",
            "Background_Color_Hover": "#4aa5ff",
            "Border_Color": "#646464",
            "FontColor": ReturnFontColor(),
        },
        "Dark-modern.qss": {
            "Background_Color": "#2b2b2b",
            "Background_Color_Hover": "#4aa5ff",
            "Border_Color": "#ffffff",
            "FontColor": ReturnFontColor(),
        },
        "Dark-contrast.qss": {
            "Background_Color": "#444444",
            "Background_Color_Hover": "#4aa5ff",
            "Border_Color": "#787878",
            "FontColor": ReturnFontColor(),
        },
    }
}
