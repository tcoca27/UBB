//
// Created by tudor on 30/03/2019.
//

#ifndef SET_SET_H
#define SET_SET_H

#pragma once

#include "SetIterator.h"

typedef int TElem;

class Set {
    friend class SetIterator;
private:
    /* representation of Set*/
    TElem* elements;
    int Size;
    int capacity;

public:
    //implicit constructor
    Set(int capacity=10);

    //adds an element to the  set
    //if the element was added, the operation returns true, otherwise (if the element was already in the set)
    //it returns false
    bool add(TElem e);

    //removes an element from the set
    //if the element was removed, it returns true, otherwise false
    bool remove(TElem e);



    //checks if an element is in the  set

    bool search(TElem elem) const;



    //returns the number of elements;

    int size() const;

    //checks if the set is empty
    bool isEmpty() const;

    //returns an iterator for the set
    SetIterator iterator() const;

    //destructor
    ~Set();



};


#endif //SET_SET_H
