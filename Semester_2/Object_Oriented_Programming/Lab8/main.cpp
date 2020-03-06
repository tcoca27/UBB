#include <iostream>
#include <assert.h>
#include <string>

#include "UI.h"
#include "FakeRepo.h"
using namespace std;

int test()
{
    TrenchCoat coat1=TrenchCoat("Opt","S",56,"abc.jpg");
    TrenchCoat coat2=TrenchCoat("Opt","S",56,"abc.jpg");
    TrenchCoat coat3=TrenchCoat("COpt","M",56,"abc.jpg");
    assert(coat1.getSize()=="S");
    assert(coat1.getName()=="Opt");
    assert(coat1.getPrice()==56);
    assert(coat1==coat2);
//    //InMemoryRepository repository{};
//    assert(repository.addCoat(coat1)==0);
//    assert(repository.addCoat(coat2));
//    assert(repository.addCoat(coat3)==0);
//    assert(repository.findCoatPosition("COpt")==1);
//    assert(repository.updateCoat("Opt", "D",88,"asd.d")==0);
//    assert(repository.removeCoat("Opt")==0);
//    TextFileRepository repository1("C:\\UBB\\c+\\Teme\\Lab5\\TrenchCoats.txt");
//    //assert(repository1.addCoat(coat3)==0);
//    assert(repository1.updateCoat("Opt","s",89,"s")==0);
//    repository1.saveFile();
    return 0;
}

void testControllerAdd(){
    TrenchCoat coatSucces("o","o",9,"o");
    TrenchCoat coatFail("o","s",9,"o");
    FakeRepo* fakerepo= new FakeRepo();
    FakeRepo* fakeshop= new FakeRepo();
    Controller controller{fakerepo,fakeshop};
    assert(controller.addCoatController(coatSucces.getName(),coatSucces.getSize(),coatSucces.getPrice(),coatSucces.getPhotograph())==0);
    assert(fakerepo->coats.size()==1);
    assert(fakerepo->coats[0].getName()=="o");
    assert(fakerepo->coats[0].getSize()=="o");
    assert(fakerepo->coats[0].getPrice()==9);
    assert(fakerepo->coats[0].getPhotograph()=="o");
    try {
        assert(controller.addCoatController(coatFail.getName(), coatFail.getSize(), coatFail.getPrice(),
                                            coatFail.getPhotograph()) != 0);
    }
    catch (std::runtime_error& re){
        assert(fakerepo->coats.size()==1);
    }
    try{
        assert(controller.addCoatController("","",0,""));
    }
    catch (ValidatorException& ve){
        assert(fakerepo->coats.size()==1);
    }
}

int main(int argc, char* argv[]) {
    test();
    testControllerAdd();
    Repository* repository= new TextFileRepository;
    Repository* shoppingList= new TextFileRepository;
    Controller controller(repository,shoppingList);
    UI ui{controller};
    ui.GetCommand();
    return 0;
//    qDebug() << QT_VERSION_STR;
//    return 1;
}