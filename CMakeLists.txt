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
    Resourses/Icons/Tango-System-search.svg
    Resourses/Icons/Tango-Tools-spanner-hammer.svg
	Resourses/Icons/Edit_Cancel.svg
	Resourses/Images/animAopt.gif
    Resourses/Images/animB2op.gif
	Resourses/Images/Change shortcut.png
	Resourses/Images/Enable 3D Previewer in preferences.png
	Resourses/Images/FilterOptions.png
	Resourses/Images/Highlight example.png
	Resourses/Images/New clear button.png
	Resourses/Images/screenshot.png
	Resourses/Images/SearchBar at pointer.png
	Resourses/ui/ChangeDialog.ui
	Resourses/ui/PreferencesUI_SearchBar.ui
	Resourses/ui/ui_ChangeDialog.py
	Resourses/ui/ui_PreferencesUI_SearchBar.py
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
