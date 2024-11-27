"""
GUI игры виселица.
"""
import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QMessageBox, QPushButton)

from gallows import Gallows


class MainWindow(QMainWindow):
    """
        Класс для построения пользовательского интерфейса приложения.
    """
    def __init__(self):
        """Устанавливает атрибуты для объекта MainWindow.

        Attributes:
            self.gallows1: Экземпляр класса Gallows.
            self.random_word: Случайное слово для отгадывания.
            self.button_start: Кнопка начала игры.

        """
        super().__init__()
        self.gallows1 = Gallows()
        self.setWindowTitle("Виселица")
        self.setFixedSize(QSize(500, 500))
        self.random_word: list = []

        #: добавление кнопки "начать новую игру"
        self.button_start = QPushButton("Начать новую игру", self)
        self.button_start.setGeometry(50, 50, 150, 30)
        self.button_start.clicked.connect(self.button_start_was_clicked)

    def button_start_was_clicked(self):
        """Функция обрабатывает нажатие кнопки "Начать новую игру".

        Attributes:
            self.random_word: Случайное слово для отгадывания.
            name_hidden_word: Слово со скрытыми буквами.
            self.picture: Картинка с виселицей.
            label_hidden_word: Поле с зашифрованным словом.
            self.number_attempts: Количество оставшихся попыток.
            name_number_attempts: Надпись 'Количество оставшихся попыток'.
            value_number_attempts: Количество оставшихся попыток.
            alphabet: Буквы русского алфавита.
            self.buttons: Кнопки с буквами русского алфавита.

        """
        self.random_word = self.gallows1.start_game()
        name_hidden_word = self.gallows1.get_hidden_word()

        #: добавление картинки "виселица"
        self.picture = QLabel(self)
        self.picture.setPixmap(QPixmap('picture/6.jpg'))
        self.picture.resize(200, 200)
        self.picture.move(50, 150)
        self.picture.show()

        #: добавление загаданного слова
        label_hidden_word = QLabel(self)
        font = label_hidden_word.font()
        font.setPointSize(20)
        label_hidden_word.setFont(font)
        label_hidden_word.setText(' '.join(name_hidden_word))
        label_hidden_word.setGeometry(50, 100, 400, 30)
        label_hidden_word.setStyleSheet("background-color: white;")
        label_hidden_word.show()

        #: добавление количества оставшихся попыток
        self.number_attempts = self.gallows1.number_attempts
        name_number_attempts = QLabel('Количество оставшихся попыток', self)
        name_number_attempts.setGeometry(230, 50, 200, 30)
        name_number_attempts.show()

        value_number_attempts = QLineEdit(self, readOnly=True)
        value_number_attempts.setText(f'   {str(self.number_attempts)}')
        value_number_attempts.setGeometry(420, 50, 30, 30)
        value_number_attempts.show()

        # добавление кнопок с буквами русского алфавита
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.buttons = {}
        for x in range(1, 12):
            self.buttons[f'btn{x}'] = QPushButton(alphabet[x-1], self)
            self.buttons[f'btn{x}'].setGeometry(300, 120+x*30, 30, 30)
            self.buttons[f'btn{x}'].clicked.connect(
                lambda checked, btn=self.buttons[f'btn{x}']:
                self.the_letter_was_clicked(btn, value_number_attempts,
                                            label_hidden_word))
            self.buttons[f'btn{x}'].show()
        for x in range(12, 23):
            self.buttons[f'btn{x}'] = QPushButton(alphabet[x-1], self)
            self.buttons[f'btn{x}'].setGeometry(350, 120+(x-11)*30, 30, 30)
            self.buttons[f'btn{x}'].clicked.connect(
                lambda checked, btn=self.buttons[f'btn{x}']:
                self.the_letter_was_clicked(btn, value_number_attempts,
                                            label_hidden_word))
            self.buttons[f'btn{x}'].show()
        for x in range(23, 34):
            self.buttons[f'btn{x}'] = QPushButton(alphabet[x-1], self)
            self.buttons[f'btn{x}'].setGeometry(400, 120+(x-22)*30, 30, 30)
            self.buttons[f'btn{x}'].clicked.connect(
                lambda checked, btn=self.buttons[f'btn{x}']:
                self.the_letter_was_clicked(btn, value_number_attempts,
                                            label_hidden_word))
            self.buttons[f'btn{x}'].show()

    def the_letter_was_clicked(self, btn, value_number_attempts,
                               label_hidden_word):
        """Функция обрабатывает нажатие кнопок с буквами.

        Args:
            btn: Кнопка с буквами русского алфавита.
            value_number_attempts: Количество оставшихся попыток.
            label_hidden_word: Поле с зашифрованным словом.

        """

        btn.setDisabled(True)
        label_text = " ".join(self.gallows1.get_guess_letter(btn.text()))
        label_hidden_word.setText(label_text)
        value_number_attempts.setText(
            f'   {str(self.gallows1.number_attempts)}')
        match self.gallows1.number_attempts:
            case 1:
                self.picture.setPixmap(QPixmap('picture/1.jpg'))
            case 2:
                self.picture.setPixmap(QPixmap('picture/2.jpg'))
            case 3:
                self.picture.setPixmap(QPixmap('picture/3.jpg'))
            case 4:
                self.picture.setPixmap(QPixmap('picture/4.jpg'))
            case 5:
                self.picture.setPixmap(QPixmap('picture/5.jpg'))
            case 6:
                self.picture.setPixmap(QPixmap('picture/6.jpg'))

        #: Изменение интерфейса игры при окончании (победа/поражение).
        if self.gallows1.win_game():
            self.picture.setPixmap(QPixmap('picture/picture_win.jpg'))
            self.picture.show()
            for x in range(1, 34):
                self.buttons[f'btn{x}'].setDisabled(True)
        if self.gallows1.game_over():
            self.picture.setPixmap(QPixmap('picture/0.png'))
            self.picture.show()
            for x in range(1, 34):
                self.buttons[f'btn{x}'].setDisabled(True)

    def closeEvent(self, event):
        """Функция обрабатывает событие CloseEvent.

        Args:
            event: Событие.

        Attributes:
            question: Окно сообщение с выбором Yes/No.
            answer: Окно сообщение с загаданным словом.

        """
        if len(self.random_word) == 0:
            event.accept()
        else:
            question = QMessageBox.question(
                self, 'Вопрос:', 'Показать задуманное слово?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if question == QMessageBox.StandardButton.Yes:
                event.ignore()
                answer = QMessageBox(self)
                answer.setWindowTitle("Cлово:")
                answer.setText(str(self.random_word))
                answer.show()
            else:
                event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
