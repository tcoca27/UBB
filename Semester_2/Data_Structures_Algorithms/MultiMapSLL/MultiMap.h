//
// Created by tudor on 31/03/2019.
//

#ifndef MULTIMAPSLL_MULTIMAP_H
#define MULTIMAPSLL_MULTIMAP_H

#pragma once

#include <vector>
#define NULL_TKey -1
#include <utility>



using namespace std;

typedef int TKey;

typedef int TValue;

typedef std::pair<TKey, TValue> TElem;

struct node{
    TElem elem;
    node* next;
};

struct SLL{
    node* head;
    node* tail;
};


typedef bool(*Relation)(TKey, TKey);

class SortedMultiMap {
    friend class SMMIterator;
private:
    /* representation of the SortedMultiMap */
    SLL* MultiMap;
    Relation relation;


public:
    // constructor
    SortedMultiMap(Relation r);

    //adds a new key value pair to the sorted multi map
    void add(TKey c, TValue v);

    //returns the values belonging to a given key
    vector<TValue> search(TKey c) const;

    //removes a key value pair from the sorted multimap
    //returns true if the pair was removed (it was part of the multimap), false if nothing is removed
    bool remove(TKey c, TValue v);


    //returns the number of key-value pairs from the sorted multimap
    int size() const;

    //verifies if the sorted multi map is empty
    bool isEmpty() const;

    // returns an iterator for the sorted multimap. The iterator will return the pairs as required by the relation (given to the constructor)
    SMMIterator iterator() const;

    // destructor
    ~SortedMultiMap();

    int getKeyRange() const;

};


#endif //MULTIMAPSLL_MULTIMAP_H
