//
// Created by tudor on 31/03/2019.
//

#include "MultiMap.h"
#include "SMMIterator.h"
#include <iostream>

SortedMultiMap::SortedMultiMap(Relation r) {
    /*
     * constructor for the class
     * Complexity: AC=BC=WC=T=theta(1)
     */
    MultiMap=new SLL();
    MultiMap->head=NULL;
    relation=r;
}

void SortedMultiMap::add(TKey c, TValue v) {
    /*
     * Complexity: best case:O(1), worst case: O(n), avg: O(n), T:O(n)
     */
    node* newNode = new node();
    newNode->elem.first = c;
    newNode->elem.second = v;
    newNode->next = NULL;
    if (MultiMap->head == NULL) {
        //if map is empty, head and tail become the new node
        MultiMap->head = newNode;
        MultiMap->tail = newNode;
    }
    else {
        node* nodeMap = MultiMap->head;
        while (nodeMap != NULL && relation(nodeMap->elem.first, c)) //go to the next node until the relation isn't met anymore, or we reach the end
            nodeMap = nodeMap->next;

        if (nodeMap == NULL) {
            //if we need to add it on the last position, we have to modify the next of the previously last elem
            node *aux = MultiMap->head;
            while (aux->next != NULL)
                aux = aux->next;
            aux->next = newNode;
            newNode->next = NULL;
            MultiMap->tail=newNode;
        }
        else if (nodeMap == MultiMap->head) {
            // corner case if we have to add on the first position
            newNode->next = MultiMap->head;
            MultiMap->head = newNode;
        }
        else {
            // we get the node after which we have to add the new one
            node *aux = MultiMap->head;
            while (aux->next != nodeMap && aux != NULL)
                aux = aux->next;
            //we add the new one
            newNode->next = nodeMap;
            aux->next = newNode;
        }
    }
}

bool SortedMultiMap::remove(TKey c, TValue v) {
    //Complexity: BC: O(1), WC: O(n), AC:O(n), T:O(n)
    node* nodeMap=MultiMap->head;
    while(nodeMap!=NULL){
        //we go through the map and search for the elem to delete
        if(nodeMap->elem.first==c && nodeMap->elem.second==v)if(MultiMap->head==nodeMap){
            //corner case if it is the first
            MultiMap->head=nodeMap->next;
            return true;
        }
        if(nodeMap->next==MultiMap->tail)
        {
            //corner case if it is the last
            if(MultiMap->tail->elem.first==c && MultiMap->tail->elem.second==v){
                nodeMap->next=NULL;
                MultiMap->tail=nodeMap;
                return true;
            }
            else return false;
        }
        if(nodeMap->next->elem.first==c && nodeMap->next->elem.second==v){
            //basic remove if no corner case; the next of the node before the one to be removed receives the next of the one to be removed
            nodeMap->next=nodeMap->next->next;
            return true;
        }
        nodeMap=nodeMap->next;
    }
    return false;
}

int SortedMultiMap::size() const {
    //Complexity: AC=WC=BC=T=theta(n)
    int size=0;
    node* nodeMap=MultiMap->head;
    while(nodeMap!=NULL){
        // we go trough the whole map and increase a counter
        size++;
        nodeMap=nodeMap->next;
    }
    return size;
}

vector<TValue> SortedMultiMap::search(TKey c) const {
    //Complexity: AC=WC=BC=T=theta(n)
    vector<TValue> newVector;
    node* nodeMap=MultiMap->head;
    while(nodeMap!=NULL)
    {
        //we go through the map and if the key== c we retain its values in a new vector
        if(nodeMap->elem.first==c)newVector.push_back(nodeMap->elem.second);
        nodeMap=nodeMap->next;
    }
    return newVector;
}

bool SortedMultiMap::isEmpty() const {
    //Complexity: AC=BC=WC=T=theta(1)
    return MultiMap->head==NULL;
}

SortedMultiMap::~SortedMultiMap() {
    //Complexity: AC=WC=BC=T=theta(n)
    node* nodeMap=MultiMap->head;
    while(nodeMap!=NULL){
        //destroys all the nodes from the map
        node* aux=nodeMap->next;
        delete nodeMap;
        nodeMap=aux;
    }
    MultiMap->head=NULL;
}

SMMIterator SortedMultiMap::iterator() const {
    //Complexity: AC=BC=WC=T=theta(1)
    return SMMIterator(*this);
}

int SortedMultiMap::getKeyRange() const {
    //Complexity: AC=BC=WC=T=theta(1)
    if(isEmpty())return -1;
    else
        return abs(MultiMap->head->elem.first-MultiMap->tail->elem.first);
}
