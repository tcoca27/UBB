#include "QtGuiApplication3.h"
#include "Repository.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Repository r;
	for (auto u : r.getUsers()) {
		QtGuiApplication3* w = new QtGuiApplication3{ r,u };
		r.addO(w);
		w->show();
	}
	return a.exec();
}
