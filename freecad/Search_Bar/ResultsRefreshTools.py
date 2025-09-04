import FreeCAD as App
from PySide import QtGui

from .Parameters_SearchBar import genericToolIcon_Pixmap
from .Serialize_SearchBar import iconToHTML

genericToolIcon = QtGui.QIcon(QtGui.QIcon(genericToolIcon_Pixmap))

# Define the translation
translate = App.Qt.translate


def refreshToolsAction(nfo):
    from .RefreshTools import refreshToolsAction
    refreshToolsAction()


def refreshToolsToolTip(nfo, setParent):
    return (
        iconToHTML(genericToolIcon)
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
            "icon": genericToolIcon,
            "text": translate("SearchBar", "Refresh cached results"),
            "toolTip": "",
            "action": {"handler": "refreshTools"},
            "subitems": [],
        }
    ]
