set(Namespace_SRCS
    BuiltInSearchResults.py
    CMakeLists.txt	
    GetItemGroups.py
    IndentedItemDelegate.py
    InitGui.py
    Init.py
	LoadChangeDialog_SearchBar.py
	MouseBar.py
    Parameters_SearchBar.py
    RefreshTools.py
    ResultsDocument.py
    ResultsPreferences.py
    ResultsRefreshTools.py
    ResultsToolbar.py
    SafeViewer.py
    SearchBoxLight.py
    SearchBox.py
    SearchResults.py
    Serialize_SearchBar.py
    StandardFunctions_SearchBar.py
    StyleMapping_SearchBar.py
    Tango-System-search.svg
    Tango-Tools-spanner-hammer.svg
	Edit_Cancel.svg
	animAopt.gif
    animB2op.gif
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

add_subdirectory(Resources)

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
