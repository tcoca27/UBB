//
// Created by tudor on 27/04/2019.
//

#ifndef LAB8_HTMLREPOSITORY_H
#define LAB8_HTMLREPOSITORY_H


#include "InMemoryRepository.h"


class HTMLRepository: public InMemoryRepository {
    std::vector<TrenchCoat> coats;
    std::string path;

public:
    HTMLRepository();
    ~HTMLRepository();
    void setPath(const std::string& newPath) override {
        path=newPath;
        loadFile();
    };
    void loadFile() override ;
    void saveFile() override ;
    void open()override ;
};


#endif //LAB8_HTMLREPOSITORY_H
