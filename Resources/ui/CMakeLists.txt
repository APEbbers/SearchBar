set(Namespace_SRCS
	ChangeDialog.ui
	PreferencesUI_SearchBar.ui
	ui_ChangeDialog.py
	ui_PreferencesUI_SearchBar.py
)

SOURCE_GROUP("" FILES ${UI_SRCS})

ADD_CUSTOM_TARGET(SEARCHBAR ALL
        SOURCES ${UI_SRCS}
)

fc_copy_sources(SEARCHBAR "${CMAKE_BINARY_DIR}/Mod/SearchBar/" ${UI_SRCS})

INSTALL(
    FILES
        ${Namespace_SRCS}
    DESTINATION
        Mod/SearchBar/Resources/ui
)
