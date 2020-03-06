cmake_minimum_required(VERSION 3.13)
project(Set)

set(CMAKE_CXX_STANDARD 14)

add_executable(Set main.cpp Set.cpp Set.h SetIterator.cpp SetIterator.h ShortTest.h ShortTest.cpp ExtendedTest.h ExtendedTest.cpp)