# You can add your own result proviers and action/tooltip handlers, by importing this module and calling the registration functions as follows.
# We use wrapper functions which import the actual implementation and call it, in order to avoid loading too much code during startup.

from .SearchResults import registerResultProvider , registerResultHandler

def registerResults ():

    from .ResultsRefreshTools import refreshToolsResultsProvider

    registerResultProvider(
        "refreshTools",
        getItemGroupsCached=lambda: refreshToolsResultsProvider() ,
        getItemGroupsUncached=lambda: [],
    )

    from .ResultsDocument import documentResultsProvider

    registerResultProvider(
        "document",
        getItemGroupsCached=lambda: [],
        getItemGroupsUncached=lambda: documentResultsProvider()
    )

    from .ResultsToolbar import toolbarResultsProvider

    registerResultProvider(
        "toolbar",
        getItemGroupsCached=lambda: toolbarResultsProvider(),
        getItemGroupsUncached=lambda: [],
    )

    from .ResultsPreferences import paramResultsProvider

    registerResultProvider(
        "param",
        getItemGroupsCached=lambda: paramResultsProvider(),
        getItemGroupsUncached=lambda: [],
    )

    from .ResultsRefreshTools import refreshToolsToolTip , refreshToolsAction

    registerResultHandler(
        "refreshTools",
        action=lambda nfo: refreshToolsAction(nfo),
        toolTip=lambda nfo, setParent: refreshToolsToolTip(nfo, setParent),
    )

    from .ResultsToolbar import toolbarToolTip , toolbarAction

    registerResultHandler(
        "toolbar",
        action=lambda nfo: toolbarAction(nfo),
        toolTip=lambda nfo, setParent: toolbarToolTip(
            nfo, setParent
        ),
    )

    from .ResultsToolbar import subToolToolTip , subToolAction

    registerResultHandler(
        "tool",
        action=lambda nfo: subToolAction(nfo),
        toolTip=lambda nfo, setParent: subToolToolTip(
            nfo, setParent
        ),
    )

    registerResultHandler(
        "subTool",
        action=lambda nfo: subToolAction(nfo),
        toolTip=lambda nfo, setParent: subToolToolTip(
            nfo, setParent
        ),
    )

    from .ResultsDocument import documentToolTip , documentAction

    registerResultHandler(
        "document",
        action=lambda nfo: documentAction(nfo),
        toolTip=lambda nfo, setParent: documentToolTip(
            nfo, setParent
        ),
    )

    from .ResultsDocument import documentObjectToolTip , documentObjectAction

    registerResultHandler(
        "documentObject",
        action=lambda nfo: documentObjectAction(nfo),
        toolTip=lambda nfo, setParent: documentObjectToolTip(
            nfo, setParent
        ),
    )

    from .ResultsPreferences import paramToolTip , paramAction

    registerResultHandler(
        "param",
        action=lambda nfo: paramAction(nfo),
        toolTip=lambda nfo, setParent: paramToolTip(
            nfo, setParent
        ),
    )

    from .ResultsPreferences import paramGroupToolTip , paramGroupAction

    registerResultHandler(
        "paramGroup",
        action=lambda nfo: paramGroupAction(nfo),
        toolTip=lambda nfo, setParent: paramGroupToolTip(
            nfo, setParent
        ),
    )
