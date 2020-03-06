//
// Created by tudor on 06/05/2019.
//

#include <sstream>
#include "BP.h"

bool BP::isResultOK() {
    if(systolicValue>=90 && systolicValue<=119 && diastolicValue>=60 && diastolicValue<=79)return true;
    return false;
}

std::string BP::toString() {
    std::stringstream ss;
    ss<<"BP   Date:"<<date<<" Diastolic Value:"<<diastolicValue<<" Systolic Value: "<<systolicValue<<'\n';
    return ss.str();
}