//
// Created by tudor on 12/04/2019.
//

#ifndef LAB5_VALIDATOR_H
#define LAB5_VALIDATOR_H



#include "TrenchCoat.h"
#include "string"
#include "string.h"



class ValidatorException {

public:

    ValidatorException(std::string message) : message(std::move(message)) {};

    const std::string& getMessage() const { return message;}

private:
    std::string message;
};



class Validator {

public:
    static bool validateTrenchCoat(const std::string& name, const std::string& size, const int& price, const std::string& photograph);

    static bool validateSize(const std::string& size);

    static bool validateName(const std::string& name);

    static bool validatePrice(int price);

    static bool validatePhotograph(const std::string& photograph);

};



#endif //LAB5_VALIDATOR_H

