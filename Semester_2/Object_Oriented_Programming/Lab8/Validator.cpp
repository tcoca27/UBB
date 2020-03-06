//
// Created by tudor on 12/04/2019.
//

#include "Validator.h"


bool Validator::validateName(const std::string &name) {
    if(name.empty() || name==" ")throw ValidatorException("Name is empty\n");
    return true;
}

bool Validator::validatePhotograph(const std::string& photograph) {
    if(photograph.empty() || photograph==" ")throw ValidatorException("Photograph is empty\n");
    return true;
}

bool Validator::validateSize(const std::string &size) {
    if(size.empty() || size==" ")throw ValidatorException("Size is empty\n");
    return true;
}

bool Validator::validatePrice(int price) {
    if(price<=0)throw ValidatorException("Price is invalid\n");
    return true;
}

bool Validator::validateTrenchCoat(const std::string &name, const std::string &size, const int &price,
                                   const std::string &photograph) {
    Validator::validateName(name) && Validator::validateSize(size) && Validator::validatePrice(price) && Validator::validatePhotograph(photograph);
    /*catch (const ValidatorException& e) {
        std::cout<<e.getMessage()<<'\n';
        return false;
    }*/
    return true;
}