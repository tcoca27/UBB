#pragma once
#include<string>
class Issue
{
private:
	std::string description, status, solver, reporter;
public:
	Issue(std::string description, std::string reporter, std::string solver = "", std::string status = "open") {
		this->description = description;
		this->reporter = reporter;
		this->solver = solver;
		this->status = status;
	}
	std::string getDescription() { return description; }
	std::string getStatus() { return status; }
	std::string getReporter() { return reporter; }
	std::string getSolver() { return solver; }
	void setStatus(std::string newS) { status = newS; }
	void setSolver(std::string newS) { solver = newS; }
	~Issue() {};
};

