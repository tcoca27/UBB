//
// Created by tudor on 06/05/2019.
//

#ifndef TEST2_BP_H
#define TEST2_BP_H


#include "MedicalAnalysis.h"

class BP: public MedicalAnalysis {
private:
    int systolicValue;
    int diastolicValue;

public:
    BP(const std::string& date, int SV,int DV):MedicalAnalysis(date), systolicValue(SV), diastolicValue(DV){};
    bool isResultOK() override ;
    std::string toString() override ;
    ~BP(){};
};


#endif //TEST2_BP_H
