set(UI_SRCS
	ChangeDialog.ui
	PreferencesUI_SearchBar.ui
	ui_ChangeDialog.py
	ui_PreferencesUI_SearchBar.py
)

ADD_CUSTOM_TARGET(SearchBarUI ALL
    SOURCES ${UI_SRCS}
)

fc_copy_sources(SearchBarUI "${CMAKE_BINARY_DIR}/Mod/SearchBar/Resources/ui" ${UI_SRCS})

INSTALL(FILES ${UI_SRCS} DESTINATION Mod/SearchBar/Resources/ui)
