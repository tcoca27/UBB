#include <iostream>
#include "ExtendedTest.h"
#include "ShortTest.h"

int main() {
    testAll();
    std::cout<<"Short test successful\n";
    testAllExtended();
    std::cout<<"Extended test successful\n";
    return 0;
}