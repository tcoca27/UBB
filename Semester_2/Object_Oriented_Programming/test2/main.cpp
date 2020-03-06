#include <iostream>
#include "UI.h"
#include "BP.h"
#include "BMI.h"
#include <vector>

int main() {
    BP bp("2009.06.16", 100,68);
    BP bp2("2019.06.16", 130,60);
    BMI bmi("2014.09.23",19);
    BMI bmi2("2017.03.22",16);
    std::vector<MedicalAnalysis*> analysis;
    analysis.push_back(&bp);
    analysis.push_back(&bp2);
    analysis.push_back(&bmi);
    analysis.push_back(&bmi2);
    Person p("Nicu",analysis);
    UI ui(p);
    ui.getCommand();
    return 0;
}