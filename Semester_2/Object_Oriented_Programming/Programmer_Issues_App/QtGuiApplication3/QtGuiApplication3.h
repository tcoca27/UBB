#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_QtGuiApplication3.h"
#include "Repository.h"
#include "Observer.h"
#include "User.h"

class QtGuiApplication3 : public QMainWindow,public Observer
{
	Q_OBJECT

public:
	QtGuiApplication3(Repository& repo,User user,QWidget *parent = Q_NULLPTR);
	void showIssues();
	void disableAdd();
	void disableResolve();
	void update() override;

private:
	Ui::QtGuiApplication3Class ui;
	Repository& repository;
	User user;

private slots:
	void handleAdd();
	void handleRemove();
	void handleResolve();
	void handleClicked(QListWidgetItem*);
};
