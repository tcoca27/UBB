//
// Created by tudor on 17/04/2019.
//

#ifndef MATRIX_MATRIXITERATOR_H
#define MATRIX_MATRIXITERATOR_H

//#include "Matrix.h"

class Matrix;
struct Element;

class MatrixIterator {
    friend class Matrix;

private:
    MatrixIterator(const Matrix& matrix);
    const Matrix& m;
    int currentIdx;
    int currentLine;
    int currentColumn;

public:
    void first();
    void next();
    bool valid();
    Element getCurrent();
};


#endif //MATRIX_MATRIXITERATOR_H
