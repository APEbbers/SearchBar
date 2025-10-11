set(ICONS_SRCS
    Tango-System-search.svg
    Tango-Tools-spanner-hammer.svg
	Edit_Cancel.svg
	preferences-searchbar.svg
)

ADD_CUSTOM_TARGET(SearchBarIcons ALL
    SOURCES ${ICONS_SRCS}
)

fc_copy_sources(SearchBarIcons "${CMAKE_BINARY_DIR}/Mod/SearchBar/Resources/Icons" ${ICONS_SRCS})

INSTALL(FILES ${ICONS_SRCS} DESTINATION Mod/SearchBar/Resources/Icons)