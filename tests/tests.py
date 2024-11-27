import re
import unittest
from gallows import word_ru_list, Gallows


class TestSomeFunction(unittest.TestCase):
    def test_list_words(self):
        for i in word_ru_list:
            word = i.rstrip('\n')
            with self.subTest('Результат не совпал с ожидаемым!', i=i):
                self.assertTrue(word.isalpha())
                self.assertTrue(re.search('[а-яА-Я]', word))

    def test_get_guess_letter(self):
        g = Gallows()
        g.word = 'путь'
        g.get_hidden_word()
        check_word = g.get_guess_letter('у')
        self.assertEqual(check_word,  ['*', 'у', '*', '*'])

    def test_win_game(self):
        g = Gallows()
        g.word = 'путь'
        g.get_hidden_word()
        check_word = g.get_guess_letter('у')
        self.assertEqual(check_word, ['*', 'у', '*', '*'])
        check_word = g.get_guess_letter('п')
        self.assertEqual(check_word, ['п', 'у', '*', '*'])
        check_word = g.get_guess_letter('ь')
        self.assertEqual(check_word, ['п', 'у', '*', 'ь'])
        check_word = g.get_guess_letter('т')
        self.assertEqual(check_word, ['п', 'у', 'т', 'ь'])
        result_game = g.win_game()
        self.assertTrue(result_game)

    def test_game_over(self):
        g = Gallows()
        g.number_attempts = 6
        g.word = 'село'
        g.get_hidden_word()
        check_word = g.get_guess_letter('а')
        self.assertEqual(check_word, ['*', '*', '*', '*'])
        check_word = g.get_guess_letter('б')
        self.assertEqual(check_word, ['*', '*', '*', '*'])
        check_word = g.get_guess_letter('в')
        self.assertEqual(check_word, ['*', '*', '*', '*'])
        check_word = g.get_guess_letter('г')
        self.assertEqual(check_word, ['*', '*', '*', '*'])
        check_word = g.get_guess_letter('д')
        self.assertEqual(check_word, ['*', '*', '*', '*'])
        check_word = g.get_guess_letter('з')
        self.assertEqual(check_word, ['*', '*', '*', '*'])
        result_game = g.game_over()
        self.assertTrue(result_game)


if __name__ == '__main__':
    unittest.main()
