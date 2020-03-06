//
// Created by tudor on 23/03/2019.
//

#ifndef LAB5_CONTROLLER_H
#define LAB5_CONTROLLER_H

#pragma once

#include "Repository.h"
#include "Validator.h"
#include "TextFileRepository.h"
#include <utility>


class Controller{

private:
    Repository* repository;
    Repository* ShoppingList;
    Validator validator;

public:
    Controller(Repository* r, Repository* shopping) : repository(r), ShoppingList(shopping){}

    Repository* getRepo() const{ return repository;}
    Repository* getShoppingList() const{ return ShoppingList;}

    int addCoatController(const std::string& name,const std::string& size,int price,const std::string& photography);
    int removeCoatController(const std::string& name);
    int updateCoatController(const std::string& name,const std::string& newSize,int newPrice,const std::string& newPhotography);
    int existsWithSize(std::string& size);
    void clearRepo();
    void clearShopping();
    int saveToShoppingList(std::string& name);
    void setPath(const std::string& newPath);
    void setPathmyList(const std::string& newPath);
    void saveFile();
    void saveShopping();
    void loadFile();
    void open();
    TrenchCoat getFromPosition(int position);
    //std::vector<TrenchCoat> filterByPriceAndSize(std::string& size, int price);
};
#endif //LAB5_CONTROLLER_H
