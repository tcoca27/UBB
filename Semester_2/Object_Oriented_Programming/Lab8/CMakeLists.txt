cmake_minimum_required(VERSION 3.13)
project(Lab8)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
et(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_PREFIX_PATH "C:\\Qt\\5.12.3\\mingw73_64\\lib\\cmake")

find_package(Qt5Widgets CONFIG REQUIRED)

include_directories(${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_PROJECT_NAME}_autogen/include/include)

add_executable(Lab8 main.cpp TrenchCoat.cpp TrenchCoat.h UI.cpp UI.h Validator.cpp Validator.h TextFileRepository.cpp TextFileRepository.h Repository.cpp Repository.h InMemoryRepository.cpp InMemoryRepository.h Controller.cpp Controller.h HTMLRepository.cpp HTMLRepository.h FakeRepo.cpp FakeRepo.h GUI.h GUI.cpp)

qt5_use_modules(Lab8 Widgets)
target_link_libraries(Lab8 Qt5::Widgets)
