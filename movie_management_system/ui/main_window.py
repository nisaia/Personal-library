# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie-management-system/assets/XML/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1000, 600)
        self.horizontalLayout = QtWidgets.QHBoxLayout(main_window)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_button = QtWidgets.QPushButton(main_window)
        self.home_button.setObjectName("home_button")
        self.verticalLayout.addWidget(self.home_button)
        self.addMovie_button = QtWidgets.QPushButton(main_window)
        self.addMovie_button.setObjectName("addMovie_button")
        self.verticalLayout.addWidget(self.addMovie_button)
        self.allMovies_button = QtWidgets.QPushButton(main_window)
        self.allMovies_button.setObjectName("allMovies_button")
        self.verticalLayout.addWidget(self.allMovies_button)
        self.addFilmDirector_button = QtWidgets.QPushButton(main_window)
        self.addFilmDirector_button.setObjectName("addFilmDirector_button")
        self.verticalLayout.addWidget(self.addFilmDirector_button)
        self.allFilmDirectors_button = QtWidgets.QPushButton(main_window)
        self.allFilmDirectors_button.setObjectName("allFilmDirectors_button")
        self.verticalLayout.addWidget(self.allFilmDirectors_button)
        self.addGenre_button = QtWidgets.QPushButton(main_window)
        self.addGenre_button.setObjectName("addGenre_button")
        self.verticalLayout.addWidget(self.addGenre_button)
        self.allGenres_button = QtWidgets.QPushButton(main_window)
        self.allGenres_button.setObjectName("allGenres_button")
        self.verticalLayout.addWidget(self.allGenres_button)
        self.statistics_button = QtWidgets.QPushButton(main_window)
        self.statistics_button.setObjectName("statistics_button")
        self.verticalLayout.addWidget(self.statistics_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(main_window)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Form"))
        self.home_button.setText(_translate("main_window", "Home"))
        self.addMovie_button.setText(_translate("main_window", "Add movie"))
        self.allMovies_button.setText(_translate("main_window", "All movies"))
        self.addFilmDirector_button.setText(_translate("main_window", "Add film director"))
        self.allFilmDirectors_button.setText(_translate("main_window", "All film directors"))
        self.addGenre_button.setText(_translate("main_window", "Add genre"))
        self.allGenres_button.setText(_translate("main_window", "All genres"))
        self.statistics_button.setText(_translate("main_window", "Statistics"))
