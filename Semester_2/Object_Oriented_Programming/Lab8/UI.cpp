//
// Created by tudor on 20/03/2019.
//

#include "UI.h"
#include <string.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <iostream>


using namespace std;

int  UI::GetCommand()
{
    /*
     * reads first command from the user and stars mode A if received
     */
    char inputString[200];
    char *commandInformation;
    char *command;
    while (true)
    {
        cout << "Welcome to Proper Trench Coats! Respectfully insert a mode: ";
        cin.get(inputString, 199);
        cin.ignore();
        commandInformation = strtok(inputString, " ");
        command = commandInformation;
        if (strcmp(command, "mode") == 0)
        {
            char* modeType = NULL;
            commandInformation = strtok(NULL, " ");
            modeType = commandInformation;
            if (strcmp(modeType, "A") == 0) {
                int result = runAdministrator();
                if (result == 1)return 0;
            }
            else if (strcmp(modeType, "B") == 0)
            {
                int result = runUser();
                if (result == 1)return 0;
            }
            else
            {
                cout << "Invalid mode! Bye\n";
                return 0;
            }

        }
        else if (strcmp(command, "fileLocation") == 0) {
            commandInformation = strtok(NULL, ",");
            std::string path = commandInformation;
            size_t pos = path.find_first_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
            if (pos != -1)
                path.erase(0, pos);
            controller.clearRepo();
            controller.setPath(path);
        }
        else if (strcmp(command, "mylistLocation") == 0) {
            commandInformation = strtok(NULL, ",");
            std::string path = commandInformation;
            size_t pos = path.find_first_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
            if (pos != -1)
                path.erase(0, pos);
            controller.clearShopping();
            controller.setPathmyList(path);
        }
        else if (strcmp(command, "exit") == 0)
            return 0;
        else
        {
            cout << ("Invalid command.\n");
        }
    }
}

int UI::runAdministrator() {
    /*
     * calls the functions for mode A
     */
    char inputString[200];
    char* command;
    char* commandInformation;
    printOptionsAdmin();
    while (true) {
        cout << "Enter your command\n";
        cout << ">";
        cin.get(inputString, 199);
        cin.ignore();
        commandInformation = strtok(inputString, " ");
        command = commandInformation;
        try {
            if (strcmp(command, "add") == 0) {
                commandInformation = strtok(NULL, ",");
                std::string name = commandInformation;
                commandInformation = strtok(NULL, ",");
                EliminateFirstSpace(commandInformation);
                std::string size = commandInformation;
                commandInformation = strtok(NULL, ",");
                char *Price = commandInformation;
                EliminateFirstSpace(Price);
                int price = atoi(Price);
                commandInformation = strtok(NULL, ",");
                EliminateFirstSpace(commandInformation);
                std::string photograph = commandInformation;
                try {
                    int result = this->controller.addCoatController(name, size, price, photograph);
                    if (result == 1)cout << "Coat already in repository \n";
                    else controller.saveFile();
                }
                catch (ValidatorException &exception) {
                    cout << exception.getMessage();
                }
            } else if (strcmp(command, "delete") == 0) {
                commandInformation = strtok(NULL, ",");
                std::string name = commandInformation;
                try {
                    int result = this->controller.removeCoatController(name);
                    if (result == 1)cout << "Coat not in repository \n";
                    else controller.saveFile();
                }
                catch (ValidatorException &exception) {
                    cout << exception.getMessage();
                }
            } else if (strcmp(command, "update") == 0) {
                commandInformation = strtok(NULL, ",");
                std::string name = commandInformation;
                commandInformation = strtok(NULL, ",");
                EliminateFirstSpace(commandInformation);
                std::string size = commandInformation;
                commandInformation = strtok(NULL, ",");
                char *Price = commandInformation;
                EliminateFirstSpace(Price);
                int price = atoi(Price);
                commandInformation = strtok(NULL, ",");
                EliminateFirstSpace(commandInformation);
                std::string photograph = commandInformation;
                try {
                    int result = this->controller.updateCoatController(name, size, price, photograph);
                    if (result == 1)cout << "Coat not in repository or bad input \n";
                    else controller.saveFile();
                }
                catch (ValidatorException &exception) {
                    cout << exception.getMessage();
                }

            } else if (strcmp(command, "fileLocation") == 0) {
                commandInformation = strtok(NULL, ",");
                std::string path = commandInformation;
                size_t pos = path.find_first_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
                if (pos != -1)
                    path.erase(0, pos);
                controller.clearRepo();
                controller.setPath(path);
            } else if (strcmp(command, "mylistLocation") == 0) {
                commandInformation = strtok(NULL, ",");
                std::string path = commandInformation;
                size_t pos = path.find_first_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
                if (pos != -1)
                    path.erase(0, pos);
                controller.clearShopping();
                controller.setPathmyList(path);
            } else if (strcmp(command, "mode") == 0) {
                commandInformation = strtok(NULL, ",");
                char *modeType = commandInformation;
                if (strcmp(modeType, "B") == 0) {
                    int result = runUser();
                    if (result == 1)return 1;
                } else cout << "Wrong mode\n";
            } else if (strcmp(command, "list") == 0) {
                listRepo();
            } else if (strcmp(command, "exit") == 0)return 1;
            else cout << "Invalid command \n";
        }
        catch (std::runtime_error& re)
        {
            std::cout<<re.what();
        }
    }
}

int UI::runUser() {
    /*
     * calls the user functions
     */
    char inputString[200];
    char* command;
    char* commandInformation;
    int positionInList=0;
    int html=0;
    printOptionsUser();
    while (true) {
        cout << "Enter your command\n";
        cout << ">";
        cin.get(inputString, 199);
        cin.ignore();
        commandInformation = strtok(inputString, " ");
        command = commandInformation;
        if (strcmp(command, "next") == 0)
        {
            commandInformation = strtok(NULL, " ");
            if (commandInformation == NULL) {
                TrenchCoat coat=controller.getFromPosition(positionInList);
                if(positionInList==controller.getRepo()->getCoats().size()-1)positionInList=0;
                else positionInList++;
                cout<<coat.CoatToString()<<'\n';
            }
            else
            {
                std::string size = commandInformation;
                int result = controller.existsWithSize(size);
                if (result == 1)cout << "No coat with given size\n";
                else {
                    TrenchCoat coat=controller.getFromPosition(positionInList);
                    if(positionInList==controller.getRepo()->getCoats().size()-1)positionInList=0;
                    else positionInList++;
                    while (coat.getSize() != size){
                        coat=controller.getFromPosition(positionInList);
                        if(positionInList==controller.getRepo()->getCoats().size()-1)positionInList=0;
                        else positionInList++;
                    }
                    cout << coat.CoatToString() << '\n';
                }
            }
        }
        else if (strcmp(command, "save") == 0)
        {
            commandInformation = strtok(NULL, " ");
            std::string name = commandInformation;
            int result = this->controller.saveToShoppingList(name);
            controller.saveShopping();
            if (result == 1)cout << "No coat with this name\n";
        }
        else if (strcmp(command, "mylist") == 0)
        {
            controller.open();
        }
        else if (strcmp(command, "fileLocation") == 0) {
            commandInformation = strtok(NULL, ",");
            std::string path = commandInformation;
            size_t pos = path.find_first_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
            if (pos != -1)
                path.erase(0, pos);
            controller.clearRepo();
            controller.setPath(path);
        }
        else if (strcmp(command, "mylistLocation") == 0) {
            commandInformation = strtok(NULL, ",");
            std::string path = commandInformation;
            size_t pos = path.find_first_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
            if (pos != -1)
                path.erase(0, pos);
            controller.clearShopping();
            controller.setPathmyList(path);
        }
        else if (strcmp(command, "mode") == 0) {
            commandInformation = strtok(NULL, ",");
            char* modeType = commandInformation;
            if (strcmp(modeType, "A") == 0) {
                int result = runAdministrator();
                if (result == 1)return 1;
            }
            else cout << "Wrong mode\n";
        }
        else if (strcmp(command, "exit") == 0)return 1;
        else cout << "Invalid command\n";
    }
}

void UI::printShoppingList() {
    /*
     * prints the shopping cart
     */
    double price = 0;
    if (controller.getShoppingList()->getCoats().empty())cout << "There are no coats saved\n";
    std::vector<TrenchCoat> trenchCoat = controller.getShoppingList()->getCoats();
    for (auto i = trenchCoat.begin(); i != trenchCoat.end(); i++) {
        TrenchCoat coat = TrenchCoat(i->getName(), i->getSize(), i->getPrice(), i->getPhotograph());
        cout << "Name: " << coat.getName() << " Size: " << coat.getSize() << " Price: " << coat.getPrice() << " Photograph: " << coat.getPhotograph() << '\n';
        //price+=this->controller.getShoppingList().getCoats().getAll()[i].getPrice();
    }
    //cout<<"Your total is: "<<price<<'\n';
}

void UI::listRepo() {
    /*
     * lists everything from the repository
     */
    for (int i = 0; i < controller.getRepo()->getCoats().size(); i++)
        cout << this->controller.getRepo()->getCoats()[i].CoatToString() << "\n";
}

void UI::EliminateFirstSpace(char* stringToEliminateFrom)
{
    /*
     * function which eliminates the redundant first space from the parameters
     */
    for (int i = 0; i < strlen(stringToEliminateFrom); i++)
        stringToEliminateFrom[i] = stringToEliminateFrom[i + 1];
}

void UI::printOptionsAdmin()
{
    /*
     * prints the options to the admin
     */
    cout << endl;
    cout << "Administrator mode entered. Here are your commands:\n";
    cout << "add name, size, price, photograph\n";
    cout << "update name, newSize, newPrice, newPhotograph\n";
    cout << "delete name (e.g. delete neo)\n";
    cout << "list\n";
    cout << "exit\n";
    cout << endl;
}

void UI::printOptionsUser()
{
    /*
     * prints the options to the admin
     */
    cout << endl;
    cout << "User mode entered. Here are your commands:\n";
    cout << "next\n";
    cout << "save name (e.g. save neo)\n";
    cout << "list size, price (e.g. list M-XL, 60)\n";
    cout << "myList\n";
    cout << "exit\n";
    cout << endl;
}

//int UI::runTextFile(const std::string &path) {
//    TextFileRepository repository(path);
//    Controller controller1(repository);
//}

