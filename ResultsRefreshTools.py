import FreeCAD as App
import FreeCADGui as Gui

import os
from PySide import QtGui
import Serialize_SearchBar
import Parameters_SearchBar as Parameters

RefreshToolIcon = Gui.getIcon("view-refresh")

# Define the translation
translate = App.Qt.translate


def refreshToolsAction(nfo):
    import RefreshTools

    RefreshTools.refreshToolsAction()


def refreshToolsToolTip(nfo, setParent):
    return (
        Serialize_SearchBar.iconToHTML(RefreshToolIcon)
        + "<p>"
        + translate(
            "SearchBar",
            "Load all workbenches to refresh the cached results. This may take a minute, depending on the number of installed workbenches.",
        )
        + "</p>"
    )


def refreshToolsResultsProvider():
    return [
        {
            "icon": RefreshToolIcon,
            "text": translate("SearchBar", "Refresh cached results"),
            "toolTip": "",
            "action": {"handler": "refreshTools"},
            "subitems": [],
        }
    ]
