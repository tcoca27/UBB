//
// Created by tudor on 17/04/2019.
//

#ifndef LAB5_TEXTFILEREPOSITORY_H
#define LAB5_TEXTFILEREPOSITORY_H

#include <iostream>
#include <fstream>
#include <vector>
#include <windows.h>
#include <fcntl.h>
#include <winuser.h>
#include <shellapi.h>
#include "InMemoryRepository.h"

class TextFileRepository: public InMemoryRepository {
private:
    std::string path;
    std::vector<TrenchCoat> TrenchCoats;

public:
    TextFileRepository();
    ~TextFileRepository();
    TextFileRepository(const std::string& newPath): InMemoryRepository(){
        path=newPath;
        loadFile();
    }
    void setPath(const std::string& newPath)override {
        path=newPath;
        loadFile();
    };
    void loadFile() override;
    TextFileRepository(const TextFileRepository& repository);
    void saveFile() override;
    void open()override ;
};


#endif //LAB5_TEXTFILEREPOSITORY_H
