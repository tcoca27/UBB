//
// Created by tudor on 12/05/2019.
//

#ifndef LAB8_FAKEREPO_H
#define LAB8_FAKEREPO_H


#include "InMemoryRepository.h"

class FakeRepo: public InMemoryRepository {
public:
    std::vector<TrenchCoat> coats;
    FakeRepo(){};
    int addCoat(const TrenchCoat& trenchCoat) override ;

};


#endif //LAB8_FAKEREPO_H
