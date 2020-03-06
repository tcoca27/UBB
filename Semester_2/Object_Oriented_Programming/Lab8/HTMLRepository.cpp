//
// Created by tudor on 27/04/2019.
//
#include <string.h>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include "HTMLRepository.h"

HTMLRepository::HTMLRepository() {};
HTMLRepository::~HTMLRepository() {};

void HTMLRepository::saveFile() {
    std::ofstream output(path);
    output<<"<!DOCTYPE html>\n<html>\n<head>\n<title>Shopping Basket</title>\n</head>\n<body>\n<table border=\"1\">\n";
    output<<"<tr>\n<td>Name</td>\n"
               "<td>Size</td>\n"
               "<td>Price</td>\n"
               "<td>Photograph</td>\n"
               "</tr>\n";
    for(int i=0;i<getCoats().size();i++){
        TrenchCoat coat=getCoats()[i];
        output <<"\n"<<"<td>"<<coat.getName().c_str() << "</td>\n"<<"<td>"<< coat.getSize().c_str() <<"</td>\n"<<"<td>"<< coat.getPrice() <<"</td>\n"<<"<td><a href="<<'"'<< coat.getPhotograph().c_str()<<'"'<<">Link</a></td>\n"<<"</tr>\n";
    }
    output <<"</tr>\n"
                "</table>\n"
                "</body>\n"
                "</html>";
    output.close();
}

void HTMLRepository::loadFile() {
    std::ifstream input(path);
    std::string line;
    for(int i=0;i<=13;i++)std::getline(input,line);
    TrenchCoat coat;
    while(line.find("<td>")!=std::string::npos){
        std::getline(input,line);
        break;
    }
    while(line.find("<td>")!=std::string::npos && line.find("</td>")!=std::string::npos)
    {
        std::string name;
        name=line.substr(7,line.size()-12);
        coat.setName(name);
        std::getline(input,line);

        std::string size;
        size=line.substr(7,line.size()-12);
        coat.setSize(size);
        std::getline(input,line);

        std::string price;
        price=line.substr(7,line.size()-12);
        try {
            int Price = stoi(price);
            coat.setPrice(Price);
            std::getline(input,line);
        }
        catch (std::exception& e){
            break;
        }

        std::string photograph;
        photograph=line.substr(7,line.size()-12);
        coat.setPhotography(photograph);
        std::getline(input,line);
        addCoat(coat);
    }
    input.close();
}

void HTMLRepository::open() {
    system(path.c_str());
}