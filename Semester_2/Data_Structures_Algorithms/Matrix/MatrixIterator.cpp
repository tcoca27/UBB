//
// Created by tudor on 17/04/2019.
//

#include <exception>
#include <iostream>
#include "MatrixIterator.h"
#include "Matrix.h"


MatrixIterator::MatrixIterator(const Matrix &matrix): m(matrix) {
    currentIdx=m.sparseMatrixSLLA.head;
    currentLine=0;
    currentColumn=0;
}

void MatrixIterator::next() {
    currentIdx=m.sparseMatrixSLLA.next[currentIdx];
    //throw std::exception();
}

void MatrixIterator::first() {
    if(valid())currentIdx=m.sparseMatrixSLLA.head;
    throw std::exception();
}

Element MatrixIterator::getCurrent() {
    if(valid()){
        if(m.element(currentLine,currentColumn)==NULL_TELEM)
        {
            std::cout<<currentLine<<","<<currentColumn<<'\n';
            Element e;
            e.line=currentLine;
            e.column=currentColumn;
            e.value=NULL_TELEM;
            if(currentColumn==m.nrColumns()-1){
                currentLine++;
                currentColumn=0;
                std::cout<<currentLine<<","<<currentColumn<<'\n';
            }
            else currentColumn++;
            return e;
        }
        if(currentColumn==m.nrColumns()-1){
            currentLine++;
            currentColumn=0;
        }
        else currentColumn++;
        return m.sparseMatrixSLLA.elements[currentIdx];
    }
    throw std::exception();
}

bool MatrixIterator::valid() {
    return currentIdx!=-1;
}

//Element MatrixIterator::getCurrent() {
//    if(valid()){
//        return m.sparseMatrixSLLA.elements[currentIdx];
//    }
//    throw std::exception();
//}
