set(IMAGES_SRCS
	animAopt.gif
    animB2op.gif
	"Change shortcut.png"
	"Enable 3D Previewer in preferences.png"
	FilterOptions.png
	"Highlight example.png"
	"New clear button.png"
	screenshot.png
	"SearchBar at pointer.png"
)

ADD_CUSTOM_TARGET(SearchBarImages ALL
    SOURCES ${IMAGES_SRCS}
)

fc_copy_sources(SearchBarImages "${CMAKE_BINARY_DIR}/Mod/SearchBar/Resources/Images" ${IMAGES_SRCS})

INSTALL(FILES ${IMAGES_SRCS} DESTINATION Mod/SearchBar/Resources/Images)