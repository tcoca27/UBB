//
// Created by tudor on 30/03/2019.
//

#ifndef SET_SETITERATOR_H
#define SET_SETITERATOR_H

#pragma once

#include "Set.h"
typedef int TElem;

class SetIterator {
    friend class Set;
private:
    //Constructor receives a reference of the container.

    //after creation the iterator will refer to the first element of the container, or it will be invalid if the container is empty
    SetIterator(const Set  &s): set(s) {current=0;};
    const Set& set;
    int current;
    //contains a reference of the container it iterates over
    /* representation specific for the iterator*/

public:
    //sets the iterator to the first element of the container
    void first();

    //moves the iterator to the next element
    //throws exception if the iterator is not valid
    void next();

    //checks if the iterator is valid
    bool valid() const;

    //returns the value of the current element from the iterator
    // throws exception if the iterator is not valid
    TElem getCurrent() const;
};




#endif //SET_SETITERATOR_H
