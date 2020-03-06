#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"
int main() {
    testAll();
    std::cout<<"Short test passed\n";
    testAllExtended();
    std::cout<<"Extended tests passed";
}