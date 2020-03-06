//
// Created by tudor on 30/03/2019.
//

#include <exception>
#include "SetIterator.h"

TElem SetIterator::getCurrent() const {
    //Complexity: theta(1)
    if(!valid())throw std::exception("Invalid iterator");
    else return set.elements[current];
}

void SetIterator::next() {
    //Complexity: theta(1)
    if(!valid())throw std::exception("Invalid iterator");
    else current++;
}

void SetIterator::first() {
    //Complexity:theta(1)
    current=0;
}

bool SetIterator::valid() const {
    //Complexity: theta(1)
    return (current<set.size());
}