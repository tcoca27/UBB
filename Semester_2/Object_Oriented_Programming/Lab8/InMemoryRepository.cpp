//
// Created by tudor on 22/04/2019.
//

#include "InMemoryRepository.h"

InMemoryRepository::InMemoryRepository() {
}

int InMemoryRepository::addCoat(const TrenchCoat &trenchCoat) {
    /*
     * function which adds a coat to the repo
     * input: coat
     */
    try {
        std::string name = trenchCoat.getName();
        findCoatPosition(name);
        return 1;
    }
    catch (std::runtime_error &e) {
        TrenchCoats.push_back(trenchCoat);
        return 0;
    }
}

int InMemoryRepository::findCoatPosition(const std::string &name) {
    /*
     * searches for the coat in repo and returns its position
     * input: name
     * output: position or -1 if there isn't
     */
    for(int i=0;i<TrenchCoats.size();i++)
    {
        if(TrenchCoats[i].getName()==name){
            return i;
        }
    }
    throw std::runtime_error("Coat not in repo\n");
}

int InMemoryRepository::removeCoat(const std::string &name) {
    /*
     * function which removes a coat from the repo
     * input: name
     */
    auto position = findCoatPosition(name);
    TrenchCoats.erase(TrenchCoats.begin()+position);
    return 0;
}

int InMemoryRepository::updateCoat(const std::string &name, const std::string &newSize, int newPrice,
                                   const std::string &newPhotograph) {
    /*
     * function which updates a coat from the repo
     * input: coat
     */
    auto position = findCoatPosition(name);
    TrenchCoats.emplace(TrenchCoats.begin()+position, TrenchCoat{name, newSize, newPrice, newPhotograph});
    position++;
    TrenchCoats.erase(TrenchCoats.begin()+position);
    return 0;
}

std::vector<TrenchCoat> InMemoryRepository::getCoats() const {
    return TrenchCoats;
}

//TrenchCoat InMemoryRepository::getFromPosition(int position) {
//    auto iterator=getCoats().begin()+position;
//    TrenchCoat coat=*iterator;
//    return coat;
//}

InMemoryRepository::~InMemoryRepository() {}
