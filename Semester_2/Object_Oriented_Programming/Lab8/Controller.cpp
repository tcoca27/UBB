//
// Created by tudor on 23/03/2019.
//

#include "Controller.h"
#include "HTMLRepository.h"
#include <string>
#include <algorithm>


int Controller::addCoatController(const std::string &name,const std::string &size, int price,const std::string &photography) {
    /*
    * Tries to add a coat to the repo, returns 0 if success and 1 or 2 if error
    * input: name, size, price, photograph
    * output: int
    */
    //if(isValidSize(size)==0)return 2;
    validator.validateTrenchCoat(name,size,price,photography);
    TrenchCoat CoatToAdd=TrenchCoat(name,size,price,photography);
    int result=repository->addCoat(CoatToAdd);
    return result;
}

int Controller::removeCoatController(const std::string& name) {
    /*
     * Tries to remove a coat from the repo, returns 0 if success and 1 for error
     * input: name
     * output: int
     */
    validator.validateName(name);
    int result=this->repository->removeCoat(name);
    return result;
}

int Controller::updateCoatController(const std::string& name,const std::string& newSize, int newPrice,const std::string& newPhotography) {
    /*
     * Tries to update a coat from the repo, returns 0 if success and 1 if error
     * input: name, size, price, photograph
     * output: int
     */
    validator.validateTrenchCoat(name, newSize, newPrice, newPhotography);
    int result = this->repository->updateCoat(name, newSize, newPrice, newPhotography);
    return result;
}

TrenchCoat Controller::getFromPosition(int position) {
    std::vector<TrenchCoat> coats=getRepo()->getCoats();
    int counter=0;
    for(auto& iterator: coats){
        if(counter==position){
            TrenchCoat coat=iterator;
            return coat;
        }
        counter++;
    }
}



int Controller::existsWithSize(std::string& size) {
    /*
     * checks if there are trench coats with the given size. Returns 0 if true
     */
    std::vector<TrenchCoat> trenchCoats=repository->getCoats();
    for(auto i=trenchCoats.begin(); i!=trenchCoats.end();i++)
    {
        if(i->getSize()==size)return 0;
    }
    throw std::exception();
}

int Controller::saveToShoppingList(std::string& name) {
    /*
     * saves a trench coat to the shopping list
     */
    std::vector<TrenchCoat> trenchCoats=repository->getCoats();
    for(int i=0; i<trenchCoats.size();i++)
    {
        if(this->repository->getCoats()[i].getName()==name){
            ShoppingList->addCoat(repository->getCoats()[i]);
            return 0;
        }
    }
    return 1;
}

//void Controller::saveFile() {
//    TextFileRepository* textRepository= dynamic_cast<TextFileRepository*>(repository);
//    if(textRepository==NULL)throw(ValidatorException("Downcast didnt work\n"));
//    textRepository->saveFile();
//}
void Controller::saveFile() {
    repository->saveFile();
}

void Controller::saveShopping() {
//    TextFileRepository* textRepository= dynamic_cast<TextFileRepository*>(ShoppingList);
//    if(textRepository==NULL)throw(ValidatorException("Downcast didnt work\n"));
//    textRepository->saveFile();
    ShoppingList->saveFile();
}

void Controller::setPath(const std::string &newPath) {
//    TextFileRepository* textRepository= dynamic_cast<TextFileRepository*>(repository);
//    if(textRepository==NULL)throw(ValidatorException("Downcast didnt work\n"));
//    textRepository->setPath(newPath);
    repository->setPath(newPath);
}

void Controller::setPathmyList(const std::string &newPath) {
//    TextFileRepository* textRepository= dynamic_cast<TextFileRepository*>(ShoppingList);
//    if(textRepository==NULL)throw(ValidatorException("Downcast didnt work\n"));
//    textRepository->setPath(newPath);
    if( newPath.compare(newPath.size()-4,4,"html")==0)
    {
        ShoppingList=new HTMLRepository;
    }
    ShoppingList->setPath(newPath);
}

void Controller::clearRepo() {
    for(auto coat : repository->getCoats()){
        repository->removeCoat(coat.getName());
    }
}

void Controller::clearShopping() {
    for(auto coat : getShoppingList()->getCoats()){
        repository->removeCoat(coat.getName());
    }
}

void Controller::open() {
//    TextFileRepository* textRepository= dynamic_cast<TextFileRepository*>(ShoppingList);
//    if(textRepository==NULL)throw(ValidatorException("Downcast didnt work\n"));
//    textRepository->openCsv();
    ShoppingList->open();
}

void Controller::loadFile() {
    repository->loadFile();
}

//
//std::vector<TrenchCoat> Controller::filterByPriceAndSize(std::string& size, int price) {
//    /*
//     * filters all trench coats by size and price
//     * input: size and price
//     * output: filtered list
//     */
//    std::vector<TrenchCoat> filter (repository.getCoats().size());
////    for(int i=0;i<repository.getCoats().size();i++)
////    {
////        filter.copy_if(this->repository.getCoats()[i].getSize()==size && this->repository.getCoats().getAll()[i].getPrice()<price)
////            filter.add(this->repository.getCoats().getAll()[i]);
////    }
////    return filter;
//    auto it = std::copy_if (repository.getCoats().begin(), repository.getCoats().end(), filter.begin(), [size,price](TrenchCoat coat){return (coat.getSize()==size && coat.getPrice()==price);});
//}
