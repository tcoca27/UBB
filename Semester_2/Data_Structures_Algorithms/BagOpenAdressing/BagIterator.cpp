//
// Created by tudor on 21/05/2019.
//

#include <exception>
#include "BagIterator.h"


bool BagIterator::valid() const {
    //theta(1)=AC=BC=WC
    if(current<sizeOf)return true;
    return false;
}

void BagIterator::next() {
    //theta(1)=AC=WC=BC
    if (!valid())
        throw std::exception();
    current++;
}

TElem BagIterator::getCurrent() {
    //theta(1)=AC=WC=BC
    if (!valid())
        throw std::exception();
    return elems[current];
}

void BagIterator::first() {
    //theta(1)=AC=WC=BC
    current=0;
}

