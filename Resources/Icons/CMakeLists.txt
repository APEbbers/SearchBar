set(Namespace_SRCS
    Tango-System-search.svg
    Tango-Tools-spanner-hammer.svg
	Edit_Cancel.svg
	preferences-searchbar.svg
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
        Mod/SearchBar/Resources/Icons
)