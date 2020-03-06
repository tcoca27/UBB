//
// Created by tudor on 12/05/2019.
//

#include "FakeRepo.h"

int FakeRepo::addCoat(const TrenchCoat &trenchCoat) {
    for(auto coat: coats)
        if(coat.getName()==trenchCoat.getName())
            throw std::runtime_error("coat in repo\n");
        coats.push_back(trenchCoat);
    return 0;
}
