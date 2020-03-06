//
// Created by tudor on 06/05/2019.
//

#ifndef TEST2_BMI_H
#define TEST2_BMI_H


#include "MedicalAnalysis.h"

class BMI: public MedicalAnalysis {
private:
    double value;

public:
    BMI(const std::string& date, double val): MedicalAnalysis(date), value(val){};
    bool isResultOK() override ;
    std::string toString() override ;
    ~BMI(){};

};


#endif //TEST2_BMI_H
