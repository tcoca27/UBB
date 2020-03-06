cmake_minimum_required(VERSION 3.13)
project(SortedListBST)

set(CMAKE_CXX_STANDARD 14)

add_executable(SortedListBST main.cpp SortedIndexedList.cpp SortedIndexedList.h ShortTest.cpp ShortTest.h ExtendedTest.cpp ExtendedTest.h ListIterator.cpp ListIterator.h)