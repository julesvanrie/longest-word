# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

from random import choice
from string import ascii_uppercase

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(choice(ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        grid_letters = self.grid.copy()
        for letter in word:
            if letter not in grid_letters:
                return False
            grid_letters.remove(letter)
        return True
