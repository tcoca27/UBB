cmake_minimum_required(VERSION 3.13)
project(BagOpenAdressing)

set(CMAKE_CXX_STANDARD 14)

add_executable(BagOpenAdressing main.cpp BagOpenAdressing.h ShortTest.h ShortTest.cpp ExtendedTest.h ExtendedTest.cpp BagOpenAdressing.cpp BagIterator.cpp BagIterator.h)