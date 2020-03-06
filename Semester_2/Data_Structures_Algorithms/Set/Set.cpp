//
// Created by tudor on 30/03/2019.
//

#include "Set.h"

Set::Set(int capacity) {
    //Complexity: theta(1)
    this->Size=0;
    this->capacity=capacity;
    this->elements= new TElem[capacity];
}

bool Set::add(TElem e) {
    //Complexity: BC: O(1), WC:O(n), AC:O(n)
    //looks for the element in the whole set
    if(search(e))return false;
    else
    {
        if(Size==capacity){
            //doubles the size if needed, copying its elems in a auxiliary vector of doubled capacity and recopying; then adds the element
            capacity*=2;
            TElem* newArray=new TElem[capacity];
            for(int i=0;i<Size;i++)newArray[i]=elements[i];
            delete[] elements;
            elements=newArray;
            elements[Size++]=e;
            return true;
        }
        else{
            //adds the element at the end
            elements[Size++]=e;
            return true;
        }
    }
}

bool Set::remove(TElem e) {
    //Complexity: BC: O(1), WC:O(n), AC:O(n)
    //looks for the elem in the whole set
    if(!search(e))return false;
    int positionToDelete=0;
    //gets the position of the elem
    for(int i=0; i<Size;i++)if(elements[i]==e)positionToDelete=i;
    // moves every elem to the left
    for(int i=positionToDelete;i<Size-1;i++){
        elements[i]=elements[i+1];
    }
    Size--;
    return true;
}

int Set::size() const { return Size;}//Complexity: theta(1)

bool Set::search(TElem elem) const {
    //Complexity: BC: O(1), WC:O(n), AC:O(n)
    for(int i=0;i<Size;i++)if(elements[i]==elem)return true;
    return false;
}

bool Set::isEmpty() const { return (Size==0);}//Complexity: theta(1)

Set::~Set() {
    //Complexity: theta(n)
    delete[] elements;
}

SetIterator Set::iterator() const {
    //Complexity: theta(1)
    return SetIterator(*this);
}



