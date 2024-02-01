# tests/test_game.py
from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        game = Game()

        # exercise
        grid = game.grid

        # verify
        assert type(grid) == list
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        # setup
        game = Game()

        # exercise
        assert game.is_valid('') == False

    def test_word_is_valid(self):
        # setup
        game = Game()
        grid = "KWEUEAKRZ"
        word = "EUREKA"

        # exercise
        game.grid = list(grid)

        # verify
        assert game.is_valid(word) == True

        # teardown
        assert game.grid == list(grid)

    def test_word_is_invalid(self):
        # setup
        game = Game()
        grid = "KWEUEAKRZ"
        word = "SANDWICH"

        # exercise
        game.grid = list(grid)

        # verify
        assert game.is_valid(word) == False

        # teardown
        assert game.grid == list(grid)
