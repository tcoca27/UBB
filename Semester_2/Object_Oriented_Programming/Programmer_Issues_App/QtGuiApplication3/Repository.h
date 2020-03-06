#pragma once
#include"User.h"
#include "Issue.h"
#include "Subject.h"
#include<vector>
#include<fstream>


class Repository: public Subject
{
private:
	std::vector<Issue> issues;
	std::vector<User> users;
public:
	Repository() {
		readUsers();
		readIssues();
	};
	void addIssue(std::string description, std::string reporter, std::string solver = "", std::string status = "open") {
		Issue issue=Issue(description, reporter, solver, status);
		for (auto a : issues) {
			if (a.getDescription() ==description)throw std::exception{ "Issue with this description" };
		}
		issues.push_back(issue);
		std::sort(issues.begin(), issues.end(), cmp3);
		std::sort(issues.begin(), issues.end(), cmp4);
		notify();
	}
	void addUser(std::string name,std::string type) {
		User user = User{ name,type };
		users.push_back(user);
	}

	static bool cmp3(Issue a, Issue b) {
		if (a.getDescription() < b.getDescription())return true;
		return false;
	}
	static bool cmp4(Issue a, Issue b) {
		if (a.getStatus() < b.getStatus())return true;
		return false;
	}
	void readIssues() {
		std::ifstream input{ "Issues.txt" };
		std::string desc, solver, reporter, status;
		char delimiter = ',';
		while (std::getline(input, desc, delimiter)) {
			std::getline(input, status, delimiter);
			std::getline(input, reporter, delimiter);
			std::getline(input, solver);
			addIssue(desc, reporter, solver, status);
		}
	}
	void readUsers() {
		std::ifstream input{ "Users.txt" };
		std::string name, type;
		while (std::getline(input, name, ',')) {
			std::getline(input, type);
			addUser(name, type);
		}
	}
	void removeIssue(int pos){
		if (issues[pos].getStatus() == "open")throw(std::exception{ "issue is not closed" });
		issues.erase(issues.begin()+pos);
		notify();
	}
	void resolveIssue(int pos,std::string name) {
		issues[pos].setStatus("closed");
		issues[pos].setSolver(name);
		std::sort(issues.begin(), issues.end(), cmp4);
		notify();
	}
	std::vector<User> getUsers() { return users; }
	std::vector<Issue> getIssues() { return issues; }
	~Repository() { saveIssues(); };
	void saveIssues() {
		std::ofstream out{ "Issues.txt" };
		for (auto i : issues) {
			out << i.getDescription() << ',' << i.getStatus() << ',' << i.getReporter() << ',' << i.getSolver()<<'\n';
		}
	}
};

