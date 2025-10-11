set(Namespace_SRCS
    animAopt.gif
    animB2op.gif
    BuiltInSearchResults.py
    CMakeLists.txt
	Edit_Cancel.svg
    GetItemGroups.py
    IndentedItemDelegate.py
    InitGui.py
    Init.py
	LoadChangeDialog_SearchBar.py
	MouseBar.py
    RefreshTools.py
    ResultsDocument.py
    ResultsPreferences.py
    ResultsRefreshTools.py
    ResultsToolbar.py
    SafeViewer.py
    screenshot.png
    SearchBoxLight.py
    SearchBox.py
    SearchResults.py
    Serialize.py
    Tango-System-search.svg
    Tango-Tools-spanner-hammer.svg
	Change shortcut.png
	Enable 3D Previewer in preferences.png
	FilterOptions.png
	Highlight example.png
	New clear button.png
	screenshot.png
	SearchBar at pointer.png
	ChangeDialog.ui
	PreferencesUI_SearchBar.ui
	ui_ChangeDialog.py
	ui_PreferencesUI_SearchBar.py
)



SOURCE_GROUP("" FILES ${Namespace_SRCS})

ADD_CUSTOM_TARGET(SEARCHBAR ALL
        SOURCES ${Namespace_SRCS}
)

fc_copy_sources(SEARCHBAR "${CMAKE_BINARY_DIR}/Mod/SearchBar" ${Namespace_SRCS})

INSTALL(
    FILES
        ${Namespace_SRCS}
    DESTINATION
        Mod/SearchBar
)
