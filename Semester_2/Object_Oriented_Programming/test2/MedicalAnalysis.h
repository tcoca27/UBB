//
// Created by tudor on 06/05/2019.
//

#ifndef TEST2_MEDICALANALYSIS_H
#define TEST2_MEDICALANALYSIS_H


#include <string>

class MedicalAnalysis {
protected:
    std::string date;

public:
    MedicalAnalysis(const std::string& date): date(date) {}
    virtual bool isResultOK();
    virtual std::string toString();
    std::string getDate(){ return date;};
    virtual ~MedicalAnalysis(){};

};


#endif //TEST2_MEDICALANALYSIS_H
