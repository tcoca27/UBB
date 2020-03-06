//
// Created by tudor on 06/05/2019.
//

#include "UI.h"
#include "BP.h"
#include "BMI.h"
#include <iostream>
#include <cstring>

void UI::getCommand() {
    char input[200];
    char* command;
    char* commandInformation;
    while(true)
    {
        std::cout<<"Enter a command: ";
        std::cin.getline(input,199);
        command=strtok(input," ");
        if(strcmp(command,"add")==0){
            commandInformation=strtok(NULL," ");
            std::string date=commandInformation;
            commandInformation=strtok(NULL," ");
            std::string type=commandInformation;
            if(type=="BP"){
                std::cout<<"Give systolic value:";
                std::cin.getline(input,199);
                std::string str=input;
                int sv=stoi(str);
                std::cout<<"Give diastolic value:";
                std::cin.getline(input,199);
                str=input;
                int dv=stoi(str);
                BP bp(date,sv,dv);
                person.addAnalysis(bp);
            }
            else if(type=="BMI"){
                std::cout<<"Give value:";
                std::cin.getline(input,199);
                std::string str=input;
                int sv=stoi(str);
                BMI bp(date,sv);
                person.addAnalysis(bp);
            }
            else std::cout<<"Invalid type\n";
        }
        else if(strcmp(command,"exit")==0)return;
        else if(strcmp(command,"list")==0){
            for(auto a: person.getAllAnalysis())std::cout<<a->toString();
        }
        else if(strcmp(command,"ill")==0)
        {
            commandInformation=strtok(NULL," ");
            std::string Mnth=commandInformation;
            int month=stoi(Mnth);
            if(person.isIll(month))std::cout<<"Is ill :( \n";
            else std::cout<<"Is not ill :) \n";
        }
        else if(strcmp(command,"save")==0)
        {
            commandInformation=strtok(NULL," ");
            std::string file=commandInformation;
            commandInformation=strtok(NULL," ");
            std::string date1=commandInformation;
            commandInformation=strtok(NULL," ");
            std::string date2=commandInformation;
            person.writeToFile(file,date1,date2);
        }
        else std::cout<<"Invalid command";

    }
}