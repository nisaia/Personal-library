# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/XML/allAuthors_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_allAuthors_window(object):
    def setupUi(self, allAuthors_window):
        allAuthors_window.setObjectName("allAuthors_window")
        allAuthors_window.resize(890, 730)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(allAuthors_window)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(allAuthors_window)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(allAuthors_window)
        self.lineEdit.setPlaceholderText('Search author for [Name - Surname]')
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tableView = QtWidgets.QTableView(allAuthors_window)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setCursor(QtCore.Qt.PointingHandCursor)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)

        self.retranslateUi(allAuthors_window)
        QtCore.QMetaObject.connectSlotsByName(allAuthors_window)

    def retranslateUi(self, allAuthors_window):
        _translate = QtCore.QCoreApplication.translate
        allAuthors_window.setWindowTitle(_translate("allAuthors_window", "Form"))
        self.label.setText(_translate("allAuthors_window", "All authors"))