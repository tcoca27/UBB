//
// Created by tudor on 21/05/2019.
//

#include "BagOpenAdressing.h"
#include "BagIterator.h"
#include <stdlib.h>
#include <stdint.h>

BagOpenAdressing::BagOpenAdressing() {
    //AC=BC=WC=theta(13)- intialize the bag
    this->capacity=13;
    this->sizeOf=0;
    this->elems=new TElem[capacity];
    for(int i=0;i<capacity;i++)elems[i]=NULL_TElem;
}

int64_t BagOpenAdressing::hash(TElem e,int64_t i) const {
    //AC=BC=WC=theta(1) - a single operation
    return (abs(e)%capacity+i*(1+(abs(e)%(capacity-1))))%capacity;
}

void BagOpenAdressing::resize() {
    //AC=BC=WC=theta(newSize) - to initialize the new elements array and rehash the first
    int newSize=greaterPrime(capacity*2);
    int oldSize=capacity;
    TElem* newElems= new TElem[newSize];
    for(int i=0;i<newSize;i++)newElems[i]=NULL_TElem;
    capacity=newSize;
    for(int i=0;i<oldSize;i++){
        for(int j=0;j<newSize;j++){
            if(newElems[hash(elems[i],j)]==NULL_TElem){
                newElems[hash(elems[i],j)]=elems[i];
                break;
            }
        }
    }
    delete [] elems;
    elems=newElems;
}

void BagOpenAdressing::add(TElem e) {
    //BC=theta(1) WC=theta(capacity)-when all previous positions are ocuppied OVR=O(capacity)
    if(sizeOf==capacity)resize();
    for(int i=0;i<capacity;i++){
        int64_t pos=hash(e,i);
        if(elems[pos]==NULL_TElem){
            elems[pos]=e;
            sizeOf++;
            break;
        }
    }
}

int BagOpenAdressing::size() const {
    //theta(1)=AC=BC=WC
    return sizeOf;
}

bool BagOpenAdressing::remove(TElem e) {
    //BC=theta(1) WC=theta(capacity)-when element is on last possible position OVR=O(capacity)
    for(int i=0;i<capacity;i++){
        int64_t pos=hash(e,i);
        if(elems[pos]==e){
            elems[pos]=NULL_TElem;
            sizeOf--;
            return true;
        }
    }
    return false;
}

bool BagOpenAdressing::isEmpty() const {
    //AC=BC=WC=theta(1)
    return sizeOf==0;
}

int BagOpenAdressing::nrOccurrences(TElem e) const {
    //AC=WC=BC=theta(capacity)- we go through the array to find all ocurrences on all possible positions OVR=theta(capacity)
    int counter=0;
    for(int64_t i=0;i<capacity;i++){
        int64_t pos=hash(e,i);
        if(elems[pos]==e) {
            counter++;
        }
    }
    return counter;
}

bool BagOpenAdressing::search(TElem e) const {
    //BC=theta(1)-when its on first pos WC=theta(capacity)-when on last OVR=O(capacity)
    for(int64_t i=0;i<capacity;i++){
        int64_t pos=hash(e,i);
        if(elems[pos]==e){
            return true;
        }
    }
    return false;
}

bool BagOpenAdressing::prime(int x) {
    //BC=theta(1)- when is divisible to 2 BC=WC=O(sqrt(x)) OVR=O(sqrt(x))
    for(int d=2;d<=x/2;d++)if(x%d==0)return false;
    return true;
}

int BagOpenAdressing::elementsWithMaximumFrequency() const {
    //BC=theta(n)-  OVR=theta(n)
    if(isEmpty())return 0;
    int number=0;
    int max=0;
    for(int i=0;i<capacity;i++){
        if(elems[i]!=NULL_TElem) {
            TElem elem=elems[i];
            int counter = 0;
            for (int64_t j = i; j < capacity; j++) {
                int64_t pos = hash(elem, j);
                if (elems[pos] == elem) {
                    counter++;
                }
            }
            if (counter > max) {
                max = counter;
                number = 1;
            } else if (counter == max)number++;
        }
    }
    return number;
}

int BagOpenAdressing::greaterPrime(int x) {
    //BC=theta(1)-when first number is prime WC???
    int number=x+1;
    while(true){
        if(prime(number))return number;
        number++;
    }
}



BagIterator BagOpenAdressing::iterator() const {
    //AC=BC=WC=theta(1)
    return BagIterator(*this);
}