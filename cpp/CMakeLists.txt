# Specify the minimum version for CMake
cmake_minimum_required(VERSION 3.10)

# Project's name
project(compute_pi LANGUAGES CXX)

###############################################################################
# build setup
###############################################################################

# Set the output folder where your program will be created
set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR})

###############################################################################
# Compiler flags
###############################################################################

if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CXX_FLAGS)
  #release comes with -O3 by default
  set(CMAKE_BUILD_TYPE Release CACHE STRING
    "Choose the type of build, options are: None Debug Release RelWithDebInfo MinSizeRel." FORCE)
endif(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CXX_FLAGS)

###############################################################################
# dependencies
###############################################################################


# Search for pybind11
find_package(pybind11 REQUIRED)

find_package(OpenMP)
if (OPENMP_FOUND)
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

###############################################################################
# targets
###############################################################################
add_library(scientific_module scientific_module)

target_include_directories(scientific_module
  PUBLIC
  ${PROJECT_SOURCE_DIR}/include
)

set_target_properties(scientific_module
  PROPERTIES
  CXX_STANDARD 14
  CXX_STANDARD_REQUIRED ON
  )

target_compile_options(scientific_module
  PUBLIC
  "-Wall"
)

target_link_libraries(scientific_module
  PRIVATE
  pybind11::module
  )
