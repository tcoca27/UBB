//
// Created by tudor on 20/03/2019.
//

#ifndef LAB5_TRENCHCOAT_H
#define LAB5_TRENCHCOAT_H


#include <iostream>
#include <vector>
#include <sstream>

class TrenchCoat
{
private:
    std::string name;
    std::string size;
    double price;
    std::string photograph;

public:
    TrenchCoat();
    TrenchCoat(const std::string& name, const std::string& size, const int& price, const std::string& photograph);

    std::string getName() const {return name;};
    std::string getSize() const {return size;};
    double getPrice() const { return price;};
    std::string getPhotograph() const { return photograph;};

    void setName(std::string& newName){this->name=newName;};
    void setSize(std::string& newSize){this->size=newSize;};
    void setPhotography (std::string& newPhotography) {this->photograph=newPhotography;};
    void setPrice (int newPrice) {this->price=newPrice;};

    std::string CoatToString();

    int operator==( TrenchCoat trenchCoat);
    friend std::istream& operator>> (std::istream& in, TrenchCoat& trenchCoat);
    friend std::ostream& operator<< (std::ostream& out,const TrenchCoat& trenchCoat);
    //void open();
};


#endif //LAB5_TRENCHCOAT_H
