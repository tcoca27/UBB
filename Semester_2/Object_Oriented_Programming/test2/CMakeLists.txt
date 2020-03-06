cmake_minimum_required(VERSION 3.13)
project(test2)

set(CMAKE_CXX_STANDARD 14)

add_executable(test2 main.cpp MedicalAnalysis.cpp MedicalAnalysis.h BMI.cpp BMI.h BP.cpp BP.h Person.cpp Person.h UI.cpp UI.h)