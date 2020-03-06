/********************************************************************************
** Form generated from reading UI file 'QtGuiApplication3.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QTGUIAPPLICATION3_H
#define UI_QTGUIAPPLICATION3_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_QtGuiApplication3Class
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QListWidget *issuList;
    QLineEdit *descriptionEdit;
    QPushButton *addButton;
    QPushButton *resolveButton;
    QPushButton *removeButton;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *QtGuiApplication3Class)
    {
        if (QtGuiApplication3Class->objectName().isEmpty())
            QtGuiApplication3Class->setObjectName(QString::fromUtf8("QtGuiApplication3Class"));
        QtGuiApplication3Class->resize(519, 331);
        centralWidget = new QWidget(QtGuiApplication3Class);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        issuList = new QListWidget(centralWidget);
        issuList->setObjectName(QString::fromUtf8("issuList"));

        gridLayout->addWidget(issuList, 0, 0, 1, 3);

        descriptionEdit = new QLineEdit(centralWidget);
        descriptionEdit->setObjectName(QString::fromUtf8("descriptionEdit"));

        gridLayout->addWidget(descriptionEdit, 1, 0, 1, 1);

        addButton = new QPushButton(centralWidget);
        addButton->setObjectName(QString::fromUtf8("addButton"));

        gridLayout->addWidget(addButton, 1, 1, 1, 1);

        resolveButton = new QPushButton(centralWidget);
        resolveButton->setObjectName(QString::fromUtf8("resolveButton"));

        gridLayout->addWidget(resolveButton, 1, 2, 1, 1);

        removeButton = new QPushButton(centralWidget);
        removeButton->setObjectName(QString::fromUtf8("removeButton"));

        gridLayout->addWidget(removeButton, 2, 1, 1, 1);

        QtGuiApplication3Class->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(QtGuiApplication3Class);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 519, 18));
        QtGuiApplication3Class->setMenuBar(menuBar);
        mainToolBar = new QToolBar(QtGuiApplication3Class);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        QtGuiApplication3Class->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(QtGuiApplication3Class);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        QtGuiApplication3Class->setStatusBar(statusBar);

        retranslateUi(QtGuiApplication3Class);

        QMetaObject::connectSlotsByName(QtGuiApplication3Class);
    } // setupUi

    void retranslateUi(QMainWindow *QtGuiApplication3Class)
    {
        QtGuiApplication3Class->setWindowTitle(QApplication::translate("QtGuiApplication3Class", "QtGuiApplication3", nullptr));
        addButton->setText(QApplication::translate("QtGuiApplication3Class", "Add", nullptr));
        resolveButton->setText(QApplication::translate("QtGuiApplication3Class", "Resolve", nullptr));
        removeButton->setText(QApplication::translate("QtGuiApplication3Class", "Remove", nullptr));
    } // retranslateUi

};

namespace Ui {
    class QtGuiApplication3Class: public Ui_QtGuiApplication3Class {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QTGUIAPPLICATION3_H
