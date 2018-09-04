cmake_minimum_required(VERSION 2.8)

project(dlib_resnet)


find_package(dlib REQUIRED)
include_directories(${dlib_INCLUDE_DIRS})

aux_source_directory(. SRC_LIST)
add_executable(${PROJECT_NAME} ${SRC_LIST})
target_link_libraries(${PROJECT_NAME} ${dlib_LIBRARIES})

