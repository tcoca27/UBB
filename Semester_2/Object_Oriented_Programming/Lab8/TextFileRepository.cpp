//
// Created by tudor on 17/04/2019.
//

#include "TextFileRepository.h"

TextFileRepository::TextFileRepository() {
}

TextFileRepository::~TextFileRepository() {
}

void TextFileRepository::loadFile() {
    std::ifstream input(path);
    if(!input.good())
        return;
    TrenchCoat trenchCoat;
    while(input >> trenchCoat){
        addCoat(trenchCoat);
    }
    input.close();
}

void TextFileRepository::saveFile() {
    std::ofstream output(path);
    if(!output.is_open()){
        return;
    }
    for(int i=0;i<getCoats().size();i++) {
        output << getCoats()[i];
    }
    output.close();
}

void TextFileRepository::open() {
    system(path.c_str());
}

TextFileRepository::TextFileRepository(const TextFileRepository &repository): InMemoryRepository(repository) {
    path=repository.path;
    loadFile();
}