//
// Created by tudor on 23/03/2019.
//

#ifndef LAB5_REPOSITORY_H
#define LAB5_REPOSITORY_H

#pragma once

#include <vector>
#include "TrenchCoat.h"

class Repository
{
private:
    std::vector<TrenchCoat> TrenchCoats;
public:
    Repository();
    virtual int addCoat(const TrenchCoat& coat)=0;
    virtual int removeCoat(const std::string& name)=0;
    virtual int updateCoat(const std::string& name, const std::string& newSize, int newPrice, const std::string& newPhotograph)=0;
    virtual int findCoatPosition(const std::string& name)=0;
    virtual std::vector<TrenchCoat> getCoats()const =0;
    //virtual TrenchCoat getFromPosition(int position)=0;
    virtual void saveFile()=0;
    virtual void setPath(const std::string& path)=0;
    virtual void loadFile()=0;
    virtual void open()=0;
    ~Repository();
};

#endif //LAB5_REPOSITORY_H
