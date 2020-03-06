#pragma once

#include "MatrixIterator.h"
#include <utility>

class MatrixIterator;

typedef int TElem;

struct Element{
    int line;
    int column;
    TElem value;
};

typedef struct SLLA{
    Element* elements;
    int* next;
    int capacity;
    int head;
    int firstEmpty;
}SLLA;

#define NULL_TELEM 0

class Matrix {
    friend class MatrixIterator;
private:
    SLLA sparseMatrixSLLA;
    int numberLines;
    int numberCols;
    int size;


public:

    //constructor
    //throws exception if nrLines or nrCols is negative or zero
    Matrix(int nrLines, int nrCols);



    //returns the number of lines
    int nrLines() const;



    //returns the number of columns
    int nrColumns() const;



    //returns the element from line i and column j (indexing starts from 0)
    //throws exception if (i,j) is not a valid position in the Matrix
    TElem element(int i, int j) const;

    int index(int i, int j) const;

    //modifies the value from line i and column j
    //returns the previous value from the position
    //throws exception if (i,j) is not a valid position in the Matrix
    TElem modify(int i, int j, TElem e);

    void remove(int i, int j);

    int add(int i, int j, TElem e);


    /*
     * creates an iterator over all elements in the matrix (no matter if they are NULL_TELEM or not). The iterator will return
     * the elements by line (first elements of the first line, then second line, etc)
     */
    MatrixIterator iterator() const { return MatrixIterator(*this);};

};
