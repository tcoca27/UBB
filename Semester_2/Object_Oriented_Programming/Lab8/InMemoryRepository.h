//
// Created by tudor on 22/04/2019.
//

#ifndef LAB5_INMEMORYREPOSITORY_H
#define LAB5_INMEMORYREPOSITORY_H

#include "Repository.h"

class InMemoryRepository: public Repository {
protected:
    std::vector<TrenchCoat> TrenchCoats;

public:
    InMemoryRepository();

    int addCoat(const TrenchCoat& trenchCoat) override ;
    int removeCoat(const std::string& name) override ;
    int updateCoat(const std::string& name, const std::string& newSize, int newPrice, const std::string& newPhotograph) override ;
    int findCoatPosition(const std::string& name) override ;
    std::vector<TrenchCoat> getCoats()const override ;
    void saveFile() override {};
    void setPath(const std::string& path )override {};
    void loadFile()override {};
    void open()override {};
    //TrenchCoat getFromPosition(int position) override ;

    ~InMemoryRepository();
};


#endif //LAB5_INMEMORYREPOSITORY_H
