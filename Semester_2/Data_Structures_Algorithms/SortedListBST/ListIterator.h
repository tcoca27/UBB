//
// Created by tudor on 30/05/2019.
//

#ifndef SORTEDLISTBST_LISTITERATOR_H
#define SORTEDLISTBST_LISTITERATOR_H

#include <stack>
#include "SortedIndexedList.h"

typedef int TElem;

typedef TElem TComp;

struct BSTNode;

class ListIterator {
    friend class SortedIndexedList;

private:
    BSTNode* current;
    std::stack<BSTNode*> stack;
    const SortedIndexedList& list;
    ListIterator(const SortedIndexedList& l);

public:
    void next();
    TComp getCurrent();
    bool valid();
    void first();
};


#endif //SORTEDLISTBST_LISTITERATOR_H
