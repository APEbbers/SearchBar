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
    Resources.py
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
    package.xml
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
