#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"

int main() {
    testAll();
    std::cout<<"Short test succesfull\n";
    testAllExtended();
    return 0;
}