//
// Created by tudor on 06/05/2019.
//

#ifndef TEST2_UI_H
#define TEST2_UI_H


#include "Person.h"

class UI {
private:
    Person person;

public:
    UI(const Person& p): person(p){};
    void getCommand();
    ~UI(){};
};


#endif //TEST2_UI_H
