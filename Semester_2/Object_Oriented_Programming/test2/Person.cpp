//
// Created by tudor on 06/05/2019.
//

#include <fstream>
#include <iostream>
#include "Person.h"

void Person::addAnalysis(MedicalAnalysis a) {
    analysis.push_back(&a);
}

std::vector<MedicalAnalysis*> Person::getAllAnalysisByMonth(int month) {
    std::vector<MedicalAnalysis*> result;
    for(auto a: getAllAnalysis()){
        if(int month=stoi(a->getDate().substr((5,2)))==month)result.push_back(a);
    }
    return result;
}

std::vector<MedicalAnalysis*> Person::getAllAnalysisBetweenDates(const std::string &date1, const std::string &date2) {
    std::vector<MedicalAnalysis*> result;
    int month,day,year;
    for(auto a: getAllAnalysis()){
        day=stoi(a->getDate().substr(8, 2));
        month = stoi(a->getDate().substr(5, 2));
        year = stoi(a->getDate().substr(0, 4));
        if(year>=stoi(date1.substr(0, 4)) && year<=stoi(date2.substr(0, 4)) && month>=stoi(date1.substr(5, 2)) && month<=stoi(date2.substr(5, 2)) && day>=stoi(date1.substr(8, 2)) && day<=stoi(date2.substr(8, 2)))result.push_back(a);
    }
    return result;
}

bool Person::isIll(int month) {
    for(auto a:getAllAnalysisByMonth(month))if(a->isResultOK())return false;
    return true;
}

void Person::writeToFile(const std::string &filename, const std::string &date1, const std::string &date2) {
    std::ofstream out(filename);
    if(!out.is_open()){
        std::cout<<"CANT OPEN";
        return;
    }
    for(auto a: getAllAnalysisBetweenDates(date1,date2))out<<a->toString();
    out.close();
}