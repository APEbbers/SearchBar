set(ICONS_SRCS
    Tango-System-search.svg
    Tango-Tools-spanner-hammer.svg
	Edit_Cancel.svg
	preferences-searchbar.svg
)

SOURCE_GROUP("" FILES ${ICONS_SRCS})

fc_copy_sources(SEARCHBAR "${CMAKE_BINARY_DIR}/Mod/SearchBar" ${ICONS_SRCS})

INSTALL(
    FILES
        ${ICONS_SRCS}
    DESTINATION
        Mod/SearchBar/Resources/Icons
)