//
// Created by tudor on 29/05/2019.
//

#ifndef SORTEDLISTBST_SORTEDINDEXEDLIST_H
#define SORTEDLISTBST_SORTEDINDEXEDLIST_H


#define NULL_TComp -999999

typedef int TElem;

typedef TElem TComp;

typedef bool (*Relation)(TComp, TComp);

class ListIterator;

struct BSTNode{
    TElem elem;
    BSTNode* left;
    BSTNode* right;
    int leftchildren;
};

class SortedIndexedList {
    friend class ListIterator;
private:
    BSTNode* root;
    Relation relation;

public:
    // constructor
    SortedIndexedList (Relation r);


    // returns the number of elements from the list
    int size() const;


    // checks if the list is empty
    bool isEmpty() const;

    int getPos(BSTNode* node) const;

    // returns an element from a position
    //throws exception if the position is not valid
    TComp getElement(int pos) const;



    // adds an element to the end of the list
    void add(TComp e);


    // removes an element from a given position
    //returns the removed element
    //throws an exception if the position is not valid
    TComp remove(int pos);


    // searches for an element and returns the first position where the element appears or -1 if the element is not in the list
    int search(TComp e)  const;

    BSTNode* initNode(TComp e);

    BSTNode* insertRec(BSTNode* node, TComp e);

    BSTNode* parent(BSTNode* node);

    // returns an iterator set to the first element of the list or invalid if the list is empty
    ListIterator iterator() const;

    void empty(BSTNode* node);

    BSTNode* getRoot(){ return root;};


    //destructor
    ~SortedIndexedList(){};


};


#endif //SORTEDLISTBST_SORTEDINDEXEDLIST_H
