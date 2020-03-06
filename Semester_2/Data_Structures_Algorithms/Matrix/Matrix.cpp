//
// Created by tudor on 16/04/2019.
//

#include <exception>
#include <iostream>
#include "Matrix.h"

Matrix::Matrix(int nrLines, int nrCols) {
    //Complexity:theta(nrcols*nrlin)
    if(nrLines<=0 || nrCols<=0)throw std::exception();
    else {
        sparseMatrixSLLA.capacity=nrLines*nrCols;
        sparseMatrixSLLA.elements=new Element[sparseMatrixSLLA.capacity];
        sparseMatrixSLLA.next=new int[sparseMatrixSLLA.capacity];
        sparseMatrixSLLA.head=-1;
        numberCols=nrCols;
        numberLines=nrLines;

        for(int i=0;i<sparseMatrixSLLA.capacity-1;i++)sparseMatrixSLLA.next[i]=i+1;

        sparseMatrixSLLA.next[sparseMatrixSLLA.capacity-1]=-1;
        sparseMatrixSLLA.firstEmpty=0;
        size=0;
    }
}

//Complexity:theta(1)
int Matrix::nrColumns() const { return numberCols;}

//Complexity:theta(1)
int Matrix::nrLines() const { return numberLines;}

//Complexity:BC:O(1), WC:O(n), AC:O(n), T:O(n)
TElem Matrix::element(int i, int j) const {
    if (i < 0 || i >= nrLines() || j < 0 || j >= nrColumns())throw std::exception();
    int index=sparseMatrixSLLA.head;
    int tr=1;
    while(index!=-1 && tr)
    {
        if(sparseMatrixSLLA.elements[index].column==j && sparseMatrixSLLA.elements[index].line==i)tr=0;
        else index=sparseMatrixSLLA.next[index];
    }
    if(index==-1)return NULL_TELEM;
    else return sparseMatrixSLLA.elements[index].value;
}

int Matrix::index(int i, int j) const {
    //Complexity:BC:O(1), WC:O(n), AC:O(n), T:O(n)
    int index=sparseMatrixSLLA.head;
    int tr=1;
    while(index!=-1 && tr) {
        if (sparseMatrixSLLA.elements[index].column == j && sparseMatrixSLLA.elements[index].line == i)tr = 0;
        index = sparseMatrixSLLA.next[index];
    }
    return index;
}

TElem Matrix::modify(int i, int j, TElem e) {
    //Complexity:BC:O(1), WC:O(n), AC:O(n), T:O(n)
    if (i < 0 || i >= nrLines() || j < 0 || j >= nrColumns())throw std::exception();
    if(e==NULL_TELEM){
        if(element(i,j)==NULL_TELEM)return NULL_TELEM;
        else
        {
            TElem initialV=element(i,j);
            remove(i,j);
            return initialV;
        }
    }
    else
    {
        TElem initialV=element(i,j);
        if(initialV!=NULL_TELEM){
            sparseMatrixSLLA.elements[index(i,j)].value=e;
            return initialV;
        }
        else{
            int k=add(i,j,e);
            return NULL_TELEM;
        }
    }
}

void Matrix::remove(int i, int j) {
    //Complexity:BC:O(1), WC:O(n), AC:O(n), T:O(n)

    //function to remove an element from the list
    //is called only if it is a valid position in the matrix

    int currentIdx=sparseMatrixSLLA.head;
    int previousIdx=-1;

    int tr=1;
    while(currentIdx!=-1 && tr)
    {
        if(sparseMatrixSLLA.elements[currentIdx].column==j && sparseMatrixSLLA.elements[currentIdx].line==i)tr=0;
        previousIdx=currentIdx;
        currentIdx=sparseMatrixSLLA.next[currentIdx];
    }
    //corner case if element is head
    if(currentIdx==sparseMatrixSLLA.head)sparseMatrixSLLA.head=sparseMatrixSLLA.next[currentIdx];
    else sparseMatrixSLLA.next[previousIdx]=sparseMatrixSLLA.next[currentIdx]; //any other possibility

    sparseMatrixSLLA.next[currentIdx]=sparseMatrixSLLA.firstEmpty;
    sparseMatrixSLLA.firstEmpty=currentIdx;
}

int Matrix::add(int i, int j, TElem e) {
    //Complexity:BC:O(1), WC:O(n), AC:O(n), T:O(n)

    //function which adds an element at the right position in the list
    //is called only if it is a valid position in the matrix
    int currentIdx=sparseMatrixSLLA.head;
    int previousIdx=-1;

    while(currentIdx!=-1 && (sparseMatrixSLLA.elements[currentIdx].line<=i && sparseMatrixSLLA.elements[currentIdx].column<j))
    {
        previousIdx=currentIdx;
        currentIdx=sparseMatrixSLLA.next[currentIdx];
    }

    if(currentIdx==-1)
    {
        if(previousIdx==-1)//insert first element
        {
            sparseMatrixSLLA.elements[sparseMatrixSLLA.firstEmpty].value=e;
            sparseMatrixSLLA.elements[sparseMatrixSLLA.firstEmpty].line=i;
            sparseMatrixSLLA.elements[sparseMatrixSLLA.firstEmpty].column=j;

            int position=sparseMatrixSLLA.firstEmpty;

            sparseMatrixSLLA.firstEmpty=sparseMatrixSLLA.next[sparseMatrixSLLA.firstEmpty];

            sparseMatrixSLLA.next[position]=-1;
            sparseMatrixSLLA.head=position;
            return position;
        }
        else //insert last element
        {
            int position=sparseMatrixSLLA.firstEmpty;
            sparseMatrixSLLA.elements[position].line=i;
            sparseMatrixSLLA.elements[position].column=j;
            sparseMatrixSLLA.elements[position].value=e;

            sparseMatrixSLLA.firstEmpty=sparseMatrixSLLA.next[position];
            sparseMatrixSLLA.next[position]=-1;
            sparseMatrixSLLA.next[previousIdx]=position;
            return position;
        }
    }
    else
    {
        //add for no corner case
        int position=sparseMatrixSLLA.firstEmpty;
        sparseMatrixSLLA.elements[position].line=i;
        sparseMatrixSLLA.elements[position].column=j;
        sparseMatrixSLLA.elements[position].value=e;

        sparseMatrixSLLA.firstEmpty=sparseMatrixSLLA.next[position];

        sparseMatrixSLLA.next[position]=currentIdx;

        if(previousIdx!=-1)sparseMatrixSLLA.next[previousIdx]=position;

        if(sparseMatrixSLLA.head==currentIdx)sparseMatrixSLLA.head=position;
        return position;
    }
}