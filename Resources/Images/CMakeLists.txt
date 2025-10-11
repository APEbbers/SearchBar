set(Namespace_SRCS
	animAopt.gif
    animB2op.gif
	Change shortcut.png
	Enable 3D Previewer in preferences.png
	FilterOptions.png
	Highlight example.png
	New clear button.png
	screenshot.png
	SearchBar at pointer.png
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
        Mod/SearchBar/Resources/Images
)
