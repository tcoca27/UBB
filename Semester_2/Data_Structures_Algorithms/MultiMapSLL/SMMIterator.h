//
// Created by tudor on 31/03/2019.
//

#ifndef MULTIMAPSLL_SMMITERATOR_H
#define MULTIMAPSLL_SMMITERATOR_H

#pragma once
#include "MultiMap.h"


class SMMIterator {
    friend class SortedMultiMap;
private:
    SMMIterator(const SortedMultiMap& map): m(map){
        currentNode=m.MultiMap->head;
    };
    const SortedMultiMap& m;
    node* currentNode;

public:
    void first();
    void next();
    bool valid() const;
    TElem getCurrent() const;


};

#endif //MULTIMAPSLL_SMMITERATOR_H
