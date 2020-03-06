//
// Created by tudor on 31/03/2019.
//

#include "SMMIterator.h"
#include "MultiMap.h"

void SMMIterator::first() {
    //Complexity: theta(1)
    //current becomes the beginning
    currentNode=m.MultiMap->head;
}

void SMMIterator::next() {
    //Complexity: theta(1)
    if(!valid())throw std::exception("Invalid iterator\n");
    //if iterator is valid current node becomes next node
    if(currentNode!=NULL)currentNode=currentNode->next;
}

bool SMMIterator::valid() const {
    //Compplexity: theta(1)
    //checks if current node is null
    return currentNode!=NULL;
}

TElem SMMIterator::getCurrent() const {
    //Complexity: theta(1)
    if(!valid())throw std::exception("invalid iterator\n");
    // returns the current node if iter is valid
    return currentNode->elem;
}

