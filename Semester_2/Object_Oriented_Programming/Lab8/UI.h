//
// Created by tudor on 20/03/2019.
//
#pragma once
#ifndef LAB5_UI_H
#define LAB5_UI_H

#include "Controller.h"

class UI
{
private:
    Controller controller;

public:
    UI(Controller& controller1) : controller(controller1) {};
    int GetCommand();
    Controller getController() const{ return controller;}
    void listRepo();
    void printShoppingList();


private:
    static void printOptionsAdmin();
    static void printOptionsUser();
    void EliminateFirstSpace(char* stringToEliminateFrom);
    void ElimSpace(char* stringToEliminateFrom);
    int runAdministrator();
    int runUser();
    //int runTextFile(const std::string& path);
};

#endif //LAB5_UI_H
