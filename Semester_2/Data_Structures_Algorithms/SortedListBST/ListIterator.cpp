//
// Created by tudor on 30/05/2019.
//

#include <stdexcept>
#include "ListIterator.h"

ListIterator::ListIterator(const SortedIndexedList &l):list(l) {
    BSTNode* node=list.root;
    while (node!= nullptr){
        stack.push(node);
        node=node->left;
    }
    if(!stack.empty())current=stack.top();
    else current= nullptr;
}

void ListIterator::first() {
    while(!stack.empty())stack.pop();
    BSTNode* node=list.root;
    while (node!= nullptr){
        stack.push(node);
        node=node->left;
    }
    if(!stack.empty())current=stack.top();
    else current= nullptr;
}

TComp ListIterator::getCurrent() {
    if(!valid())throw std::runtime_error("iterator not valid");
    return current->elem;
}

bool ListIterator::valid() {
    if(current== nullptr)return false;
    return true;
}

void ListIterator::next() {
    if (!valid())
        throw std::invalid_argument("not valid");

    BSTNode* node = this->stack.top();
    stack.pop();

    if (node->right != nullptr)
    {
        node = node->right;
        while (node != nullptr)
        {
            stack.push(node);
            node = node->left;
        }
    }

    if (!stack.empty())
        current = stack.top();
    else
        current = nullptr;
}