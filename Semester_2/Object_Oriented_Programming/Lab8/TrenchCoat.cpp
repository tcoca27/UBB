//
// Created by tudor on 20/03/2019.
//

#include "TrenchCoat.h"
#include <stdlib.h>
#include <string>
#include <string.h>
#include <iostream>
#include <vector>
#include <sstream>


std::vector<std::string> tokenize(std::string inputString, char delimiter) {
    std::vector<std::string> result;
    std::stringstream ss(inputString);
    std::string token;

    while (std::getline(ss, token, delimiter))
        result.push_back(token);

    return result;
}

TrenchCoat::TrenchCoat(const std::string &name, const std::string &size, const int &price,
                       const std::string &photograph){
    /*
     * Constructor of the TrenchCoat object
     * input: name, size, price, photograph
     */
    this->name=name;
    this->size=size;
    this->price=price;
    this->photograph=photograph;
}

//default constructor for the object
TrenchCoat::TrenchCoat():name(""),size(""),price(0),photograph("") {}

std::string TrenchCoat::CoatToString()
{
    /*
     * function which returns a string from a coat
     */
    std::string coat("name:"+this->name+" size:"+this->size+" price:"+std::to_string(int(this->price))+" photograph:"+this->photograph);
    return coat;
}

int TrenchCoat::operator==( TrenchCoat trenchCoat)
{
    /*
     * definition of how == operator should work for coats
     */
    return this->getName()==trenchCoat.getName() && this->getSize()==trenchCoat.getSize() && this->getPrice()==trenchCoat.getPrice() && this->getPhotograph()==trenchCoat.getPhotograph();
}

//void TrenchCoat::open()
//{
//    ShellExecuteA(NULL, NULL, "chrome.exe", this->getPhotograph().c_str(), NULL, SW_SHOWMAXIMIZED);
//}

std::istream& operator>> (std::istream& in, TrenchCoat& trenchCoat){
    std::string line;
    std::getline(in,line);

    std::vector<std::string> tokens= tokenize(line, ',');
    if(tokens.size()!=4)return in;

    trenchCoat.name=tokens[0];
    trenchCoat.size=tokens[1];
    trenchCoat.price=stoi(tokens[2]);
    trenchCoat.photograph=tokens[3];
    return in;
}

std::ostream& operator<< (std::ostream& out,const TrenchCoat& trenchCoat)
{
    out<<trenchCoat.name<<","<<trenchCoat.size<<","<<trenchCoat.price<<","<<trenchCoat.photograph<<"\n";
    return out;
}

