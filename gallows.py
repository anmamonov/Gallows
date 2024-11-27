import random


#: открываем файл со списком русских слов.
with open('words_ru.txt', 'r', encoding='utf_8_sig') as file:
    word_ru_list = [line for line in file]


class Gallows():
    """
        Класс виселица.
    """
    def __init__(self) -> None:
        """Устанавливает атрибуты для объекта MainWindow.

        Attributes:
            self.hidden_word: Слово со скрытыми буквами.

        """
        self.hidden_word: list = []

    def start_game(self) -> str:
        """Получает случайное слово из списка и устанавливает количество попыток.

        Attributes:
            self.word: Случайное слово из списка.
            self.number_attempts: Количество попыток.

        Return:
            Случайное слово из списка.

        """
        self.word: str = random.choice(word_ru_list).rstrip('\n').upper()
        self.number_attempts: int = 6
        print(f'слово {self.word}') #: подсказка для отгадывания
        return self.word

    def get_hidden_word(self) -> list:
        """Возвращает слово со скрытыми буквами.

        Attributes:
            self.hidden_word: Слово со скрытыми буквами.

        Return:
            Слово со скрытыми буквами.

        """
        self.hidden_word = list('*' * len(self.word))
        return self.hidden_word

    def get_guess_letter(self, letter: str):
        """Открывает буквы в слове со скрытыми буквами.

        Args:
            letter: Буква введенная игроком.

        Attributes:
            count_letter_in_word: Счетчик вхождений буквы в слово.
            indexes_letter: Список индексов отгаданной буквы.
            self.number_attempts: Количество попыток.

        Return:
            Слово с открытыми и скрытыми буквами.

        """
        count_letter_in_word: int = 0
        indexes_letter: list = [i for i in range(len(self.word)) if self.word[i] == letter]
        for each_index in indexes_letter:
            self.hidden_word[each_index] = letter
            count_letter_in_word += 1
        if count_letter_in_word == 0:
            self.number_attempts -= 1
        return self.hidden_word

    def win_game(self) -> bool:
        """Функция проверяет ход на победу.

        Attributes:
            self.hidden_word: Слово со скрытыми буквами.

        Return:
            True.

        """
        if '*' not in self.hidden_word:
            return True

    def game_over(self) -> bool:
        """Функция проверяет ход на проигрыш.

        Attributes:
            self.number_attempts: Количество попыток.

        Return:
            True.

        """
        if self.number_attempts == 0:
            return True


if __name__ == '__main__':
    g = Gallows()
    print(g.start_game())
    print(g.get_hidden_word())
    #symbol = input("Введите букву:")
    print(g.get_guess_letter('у'))
