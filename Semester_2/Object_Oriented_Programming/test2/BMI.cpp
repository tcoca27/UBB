//
// Created by tudor on 06/05/2019.
//

#include <sstream>
#include "BMI.h"

bool BMI::isResultOK() {
    if(value>=18.5 && value<=25)return true;
    return false;
}

std::string BMI::toString() {
    std::stringstream ss;
    ss<<"BMI   Date:"<<date<<" Value:"<<value<<'\n';
    return ss.str();
}

