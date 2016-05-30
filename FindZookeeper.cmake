# Try to find zookeeper
# Once done, this will define
#
# ZOOKEEPER_FOUND        - system has zookeeper
# ZOOKEEPER_INCLUDE_DIRS - zookeeper include directories
# ZOOKEEPER_LIBRARIES    - libraries need to use zookeeper

find_path(
	ZOOKEEPER_INCLUDE_DIR
	NAMES zookeeper/zookeeper.h
	PATHS ${CONAN_INCLUDE_DIRS_ZOOKEEPER}
)

find_library(
	ZOOKEEPER_LIBRARY
	NAMES zookeeper_st
	PATHS ${CONAN_LIB_DIRS_ZOOKEEPER}
)

set(ZOOKEEPER_FOUND TRUE)
set(ZOOKEEPER_INCLUDE_DIRS ${ZOOKEEPER_INCLUDE_DIR})
set(ZOOKEEPER_LIBRARIES ${ZOOKEEPER_LIBRARY})

mark_as_advanced(ZOOKEEPER_LIBRARY ZOOKEEPER_INCLUDE_DIR)
