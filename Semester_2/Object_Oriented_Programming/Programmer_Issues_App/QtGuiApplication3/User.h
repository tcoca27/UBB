#pragma once
#include<string>
class User
{
private:
	std::string name;
	std::string type;
public:
	User(std::string name, std::string type) {
		this->name = name;
		this->type = type;
	}
	std::string getName() { return name; }
	std::string getType() { return type; }
	~User() {};
};

