cmake_minimum_required(VERSION 3.13)
project(MultiMapSLL)

set(CMAKE_CXX_STANDARD 14)

add_executable(MultiMapSLL main.cpp MultiMap.cpp MultiMap.h SMMIterator.cpp SMMIterator.h ShortTest.cpp ShortTest.h ExtendedTest.cpp ExtendedTest.h)