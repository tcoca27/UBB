//
// Created by tudor on 29/05/2019.
//

#include <stdexcept>
#include <iostream>
#include "SortedIndexedList.h"
#include "ListIterator.h"
#include "stdlib.h"

SortedIndexedList::SortedIndexedList(Relation r) {
    //Complexity: BC=AC=WC=T=O(1)
    root= nullptr;
    relation=r;
}

bool SortedIndexedList::isEmpty() const {
    if(root== nullptr)return true;
    //Complexity: BC=AC=WC=T=O(1)
    return false;
}

int SortedIndexedList::size() const {
    if(isEmpty())return 0;
    BSTNode* current=new BSTNode();
    current=root;
    int size=0;
    while(current!= nullptr){
        size+=current->leftchildren+1; // 1 for the current node
        current=current->right;
    }
    return size;
}

int SortedIndexedList::search(TComp e) const {
    //Complexity: BC=O(1) AC=WC=O(n)
    BSTNode* current=root;
    while(current!= nullptr){
        if(current->elem==e){
            int pos=getPos(current);
            return pos;
        }
        if(relation(current->elem,e))current=current->right;
        else current=current->left;
    }
    return -1;
}

int SortedIndexedList::getPos(BSTNode *node) const {
    BSTNode* current=root;
    if(current==node)return current->leftchildren;  //if we want the position of the root
    int plus=0; //additional variable for computing right children
    int position=0;
    while(current!= nullptr && current!=node){
        if(relation(current->elem,node->elem)){
            position+=current->leftchildren;
            current=current->right;
            plus++;
        }
        else if(!relation(current->elem,node->elem)){
            current=current->left;
        }
    }
    position+=current->leftchildren+plus;
    return position;
}

TComp SortedIndexedList::getElement(int pos) const {
    if(pos<0 || pos>size()-1)
        throw std::runtime_error("Invalid position");
    BSTNode* current=root;
    int currentPos=getPos(current);
    while(currentPos!=pos){
        if(currentPos>pos){
            current=current->left;
            currentPos=getPos(current);
        }
        else {
            current=current->right;
            currentPos=getPos(current);
        }
    }
    return current->elem;
}

TComp SortedIndexedList::remove(int pos) {
    if(pos<0 || pos>size()-1){
        throw std::runtime_error("Invalid position");
    }
    BSTNode* current=root;
    BSTNode* prev= nullptr;
    int currentPos=getPos(current);
    while(currentPos!=pos) {
        if (currentPos > pos) {
            prev = current;
            current = current->left;
            currentPos=getPos(current);
        } else {
            prev = current;
            current = current->right;
            currentPos=getPos(current);
        }
    }
    int deleted=current->elem;
    if(current->left== nullptr && current->right== nullptr){
        if(prev== nullptr){
            current= nullptr;
            root= nullptr;
            return deleted;
        }
        if(prev->right==current)prev->right= nullptr;
        else {
            prev->leftchildren--;
            prev->left= nullptr;
            while(parent(prev)!= nullptr){
                BSTNode* Parent=parent(prev);
                if(Parent->left==prev)Parent->leftchildren--;
                else break;
                prev=Parent;
            }
        }
        delete current;
    }
    else if(current->left!= nullptr && current->right!= nullptr){
//        BSTNode* maximum=current->left;
//        BSTNode* previous=current;
//        while(maximum->right!= nullptr){
//            current=maximum;
//            maximum=maximum->right;
//        }
//        current->elem=maximum->elem;
//        if(maximum->left== nullptr)
//            previous->right= nullptr;
//        else {
//            maximum=maximum->left;
//            maximum->left= nullptr;
//        }
        BSTNode* minimum=current;
        BSTNode* previous=current;

        while(minimum->left!= nullptr)minimum=minimum->left;
        while(previous->left->elem !=minimum->elem)previous=previous->left;
        current->elem=minimum->elem;
        previous->left= nullptr;
        current->leftchildren--;
        while(parent(current)!= nullptr){
            BSTNode* Parent=parent(current);
            if(Parent->left==current)Parent->leftchildren--;
            else break;
            current=Parent;
        }
        delete minimum;
    }
    else{
        if(prev== nullptr){
            if(current->left!= nullptr)root=current->left;
            else root=current->right;
        }
        else if(prev->left==current) {
            if (current->left != nullptr) {
                prev->left = current->left;
                prev->leftchildren--;
                while(parent(prev)!= nullptr){
                    BSTNode* Parent=parent(prev);
                    if(Parent->left==prev)Parent->leftchildren--;
                    else break;
                    prev=Parent;
                }
            }
            else {
                prev->left->elem=current->right->elem;
                prev->left->right= nullptr;
            }
        }
        else{
            if (current->left != nullptr) {
                prev->right = current->left;
            }
            else prev->right=current->right;
        }
    }
    return deleted;
}

void SortedIndexedList::add(TComp e) {
    BSTNode* node=insertRec(root,e);
    if(root== nullptr)
        root=node;
}

BSTNode* SortedIndexedList::initNode(TComp e) {
    BSTNode* node=new BSTNode();
    node->elem=e;
    node->leftchildren=0;
    node->left= nullptr;
    node->right= nullptr;
    return node;
}

BSTNode* SortedIndexedList::insertRec(BSTNode* node, TComp e) {
    if (node == nullptr)
        node = initNode(e);
    else if (relation(node->elem, e))
        node->right = insertRec(node->right, e);
    else {
        node->leftchildren++;
        node->left = insertRec(node->left, e);
    }
    return node;
}

ListIterator SortedIndexedList::iterator() const {
    return ListIterator(*this);
}

BSTNode* SortedIndexedList::parent(BSTNode *node) {
    BSTNode* current=root;
    if(current==node)return nullptr;
    while(current!= nullptr && current->left!=node && current->right!=node){
        if(relation(current->elem,node->elem))current=current->right;
        else current=current->left;
    }
    return current;
}

void SortedIndexedList::empty(BSTNode* node) {
    //for(int i=0;i<size();i++)remove(i);
    if (node == nullptr)
        return;
    if (node->left== nullptr && node->right== nullptr) {
        if(node==root)
            root= nullptr;
        delete node;
        return;
    }

    if (node->left != nullptr)
        empty(node->left);
    if (node->right != nullptr)
        empty(node->right);
    delete node;
    if(node==root)
        root= nullptr;
}