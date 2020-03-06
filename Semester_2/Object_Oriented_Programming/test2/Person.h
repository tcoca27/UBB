//
// Created by tudor on 06/05/2019.
//

#ifndef TEST2_PERSON_H
#define TEST2_PERSON_H


#include <string>
#include <vector>
#include "MedicalAnalysis.h"

class Person {
private:
    std::string name;
    std::vector<MedicalAnalysis*> analysis;

public:
    Person(const std::string& name,std::vector<MedicalAnalysis*> a): name(name), analysis(a){};
    void addAnalysis(MedicalAnalysis a);
    std::vector<MedicalAnalysis*> getAllAnalysis(){ return analysis;};
    std::vector<MedicalAnalysis*> getAllAnalysisByMonth(int month);
    bool isIll(int month);
    std::vector<MedicalAnalysis*> getAllAnalysisBetweenDates(const std::string& date1,const std::string& date2);
    void writeToFile(const std::string& filename, const std::string& date1,const std::string& date2);
    ~Person(){};
};


#endif //TEST2_PERSON_H
