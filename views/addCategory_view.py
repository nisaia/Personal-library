import sys
from PyQt5.QtWidgets import QWidget, QMessageBox
from assets.ui_PY.addCategory_window import *
from database.db import session
from database.models import Category
from utils.custom_exceptions import NoInputException
from sqlalchemy.exc import IntegrityError

class AddCategoryView(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.addCategory_button.clicked.connect(self.addCategory)

        self.show()

    def addCategory(self):
        try:
            name = self.ui.name_lineEdit.text()
            if len(name) == 0: raise NoInputException

            category = Category(name=name)
            session.add(category)
            session.commit()
        except NoInputException:
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setText('Field not valid')
            error_message.setWindowTitle('Error')
            error_message.exec_()
        except IntegrityError:
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setText('Field already inserted')
            error_message.setWindowTitle('Error')
            error_message.exec_()
            session.rollback()


    def clearAll(self):
        self.ui.name_lineEdit.clear()