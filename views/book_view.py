import sys
from PyQt5.QtWidgets import QWidget
from ui.book_window import *
from PyQt5.QtGui import QPixmap
from database.models import *
from database.db import session
from utils.custom_exceptions import *
from utils.functions import openDialog
from sqlalchemy.exc import IntegrityError
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from views.coverIllustration_view import *
from PyQt5.QtCore import QUrl
from os.path import join
from utils.constants import COVER_PATH
import shutil


class BookView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_book_window()
        self.ui.setupUi(self)

        self.ui.uploadCover_button.clicked.connect(self.get_image_file)
        self.ui.preview_button.clicked.connect(self.displayCover)

        self.ui.editBook_button.clicked.connect(self.editBook)
        self.ui.deleteBook_button.clicked.connect(self.deleteBook)

        self.show()

    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"/", "Image files (*.jpg *.png)")
        self.ui.coverPath_label.setText(file_name)

    def displayCover(self):
        coverIllustration_window = CoverIllustrationView()
        coverIllustration_window.setModal(True)
        
        image = QPixmap(self.ui.coverPath_label.text())
        image = image.scaled(coverIllustration_window.ui.coverIllustration_label.width(), coverIllustration_window.ui.coverIllustration_label.height(), QtCore.Qt.KeepAspectRatio)
        coverIllustration_window.ui.coverIllustration_label.setPixmap(image)
        coverIllustration_window.ui.coverIllustration_label.setScaledContents(True)

        coverIllustration_window.exec_()

    def updateValues(self, book, author, category):
        self.ui.author_comboBox.clear()
        self.ui.category_comboBox.clear()

        authors = session.query(Author).all()
        if len(authors) == 0:
            self.ui.author_comboBox.addItem('No authors founded')
            self.ui.author_comboBox.setDisabled(True)
        else:
            for author in authors:
                self.ui.author_comboBox.addItem(str(author.name + " " + author.surname))
            self.ui.author_comboBox.setDisabled(False)

        categories = session.query(Category).all()
        if len(categories) == 0:
            self.ui.category_comboBox.addItem('No categories founded')
            self.ui.category_comboBox.setDisabled(True)
        else:
            for category in categories:
                self.ui.category_comboBox.addItem(category.name)
            self.ui.category_comboBox.setDisabled(False)

        self.book = book
        self.author = author
        self.category = category

        # FIRST TAB
        self.ui.title.setText(self.book.title)
        self.ui.isbn.setText(self.book.isbn)
        image = QPixmap(self.book.cover_path)
        image = image.scaled(self.ui.cover.width(), self.ui.cover.height(), QtCore.Qt.KeepAspectRatio)
        self.ui.cover.setPixmap(image)
        self.ui.cover.setScaledContents(True)
        self.ui.author.setText(self.author.name + " " + self.author.surname)
        self.ui.category.setText(self.category.name)
        self.ui.description.setText(self.book.description)

        #SECOND TAB
        self.ui.bookTitle_lineEdit.setText(self.book.title)
        self.ui.isbn_lineEdit.setText(self.book.isbn)
        self.ui.coverPath_label.setText(self.book.cover_path)

        self.ui.description_plainTextEdit.setPlainText(self.book.description)


    def editBook(self):
        try:
            book_title = self.ui.bookTitle_lineEdit.text()
            isbn = self.ui.isbn_lineEdit.text()
            author = session.query(Author).filter_by(id=self.ui.author_comboBox.currentIndex() + 1).first()
            category = session.query(Category).filter_by(id=self.ui.category_comboBox.currentIndex() + 1).first()

            if len(book_title) == 0: raise NoInputException('Enter the title of book')
            elif len(isbn) == 0: raise NoInputException('Enter the ISBN of book')
            elif author == None: raise NoInputException('Enter the author of the book')
            elif category == None: raise NoInputException('Enter the category of the book')

            old_cover_path = self.ui.coverPath_label.text()
            file_name = QUrl.fromLocalFile(old_cover_path).fileName()
            print(file_name)
            new_cover_path = join(COVER_PATH, file_name)

            description = self.ui.description_plainTextEdit.toPlainText()

            updates = {
                'title': book_title,
                'isbn': isbn,
                'author_id': author.id,
                'category_id': category.id,
                'cover_path': new_cover_path,
                'description': description
            }

            for key, value in updates.items():
                setattr(self.book, key, value)

            session.commit()

            if old_cover_path != new_cover_path: shutil.copy(old_cover_path, new_cover_path)

            openDialog(QMessageBox.Information, 'Book edited', 'Success')

        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')
        except IntegrityError:
            openDialog(QMessageBox.Critical, 'Field already inserted', 'Error')
            session.rollback()

    def deleteBook(self):
        session.delete(self.book)
        session.commit()
        home_window = self.parent().findChild(QWidget, 'home_window')
        self.parent().setCurrentWidget(home_window)

        openDialog(QMessageBox.Information, 'Book deleted', 'Success')