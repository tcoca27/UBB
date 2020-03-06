//
// Created by tudor on 21/05/2019.
//

#ifndef BAGOPENADRESSING_BAGOPENADRESSING_H
#define BAGOPENADRESSING_BAGOPENADRESSING_H

#include <stdint-gcc.h>

typedef int TElem;
#define NULL_TElem -9999999
class BagIterator;

class BagOpenAdressing {
    friend class BagIterator;
private:
    int capacity;
    TElem* elems;
    int sizeOf;
public:
    //constructor
    BagOpenAdressing();

    //adds an element to the bag
    void add(TElem e);


    int64_t hash(TElem e, int64_t i) const;

    void resize();

    //removes one occurrence of an element from a bag
    //returns true if an element was removed, false otherwise (if e was not part of the bag)

    bool remove(TElem e);


    //checks if an element appearch is the bag
    bool search(TElem e) const;



    //returns the number of occurrences for an element in the bag
    int nrOccurrences(TElem e) const;



    //returns the number of elements from the bag
    int size() const;

    int elementsWithMaximumFrequency() const;

    //returns an iterator for this bag
    BagIterator iterator() const;



    //checks if the bag is empty
    bool isEmpty() const;


    bool prime(int x);


    int greaterPrime(int x);

    //destructor
    ~BagOpenAdressing(){};

};



#endif //BAGOPENADRESSING_BAGOPENADRESSING_H
