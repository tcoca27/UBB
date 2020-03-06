#pragma once
#include<vector>>
#include"Observer.h"
class Subject
{
private:
	std::vector<Observer*> observers;
public:
	Subject();
	void addO(Observer* o) { observers.push_back(o); }
	void notify() {
		for (auto o : observers)o->update();
	}
	~Subject();
};

