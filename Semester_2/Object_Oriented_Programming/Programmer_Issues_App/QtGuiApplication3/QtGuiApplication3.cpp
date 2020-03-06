#include "QtGuiApplication3.h"
#include<qmessagebox.h>
QtGuiApplication3::QtGuiApplication3(Repository& repo,User user,QWidget *parent)
	: QMainWindow(parent),repository(repo), user(user)
{
	ui.setupUi(this);
	setWindowTitle(QString::fromStdString(user.getName() + " " + user.getType()));
	ui.descriptionEdit->setPlaceholderText("Description:");
	disableAdd();
	disableResolve();
	showIssues();
	connect(ui.addButton, SIGNAL(clicked()), this, SLOT(handleAdd()));
	connect(ui.removeButton, SIGNAL(clicked()), this, SLOT(handleRemove()));
	connect(ui.issuList, SIGNAL(itemClicked(QListWidgetItem*)), this, SLOT(handleClicked(QListWidgetItem*)));
	connect(ui.resolveButton, SIGNAL(clicked()), this, SLOT(handleResolve()));
}



void QtGuiApplication3::showIssues()
{
	ui.issuList->clear();
	std::vector<Issue> issues = repository.getIssues();
	
	for (auto i : issues) {
		std::string show = i.getDescription() + ", " + i.getStatus() + ", " + i.getReporter() + ", " + i.getSolver();
		new QListWidgetItem(show.c_str(), ui.issuList);
	}
}

void QtGuiApplication3::disableAdd()
{
	if (user.getType() == "programmer")ui.addButton->setDisabled(true);
}

void QtGuiApplication3::disableResolve()
{
	if (user.getType() == "tester")ui.resolveButton->setDisabled(true);
}

void QtGuiApplication3::update()
{
	showIssues();
}

void QtGuiApplication3::handleAdd() {
	std::string desc = ui.descriptionEdit->text().toStdString();
	try {
		repository.addIssue(desc, user.getName());
	}
	catch (std::exception& e) {
		QMessageBox q;
		q.critical(0, "Error", QString::fromStdString(e.what()));
	}
	showIssues();
}

void QtGuiApplication3::handleRemove() {
	int nr = ui.issuList->currentIndex().row();
	try {
		repository.removeIssue(nr);
	}
	catch (std::exception& e) {
		QMessageBox q;
		q.critical(0, "Error", QString::fromStdString(e.what()));
	}
	showIssues();
}

void QtGuiApplication3::handleClicked(QListWidgetItem*) {
	int nr = ui.issuList->currentIndex().row();
	if (repository.getIssues()[nr].getStatus() == "closed")ui.resolveButton->setDisabled(true);
	else ui.resolveButton->setEnabled(true);
}

void QtGuiApplication3::handleResolve() {
	int nr = ui.issuList->currentIndex().row();
	repository.resolveIssue(nr,user.getName());
	showIssues();
}