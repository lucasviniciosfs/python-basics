import random

class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suit = ""
    value = ""

    def __init__(self):
        self.suit = random.choice(self.suits)
        self.value = random.choice(self.values)

    def __repr__(self) -> str:
        return f"{self.suit} of {self.value}"

    def create_cards(self) -> list:
        full_cards = []
        for key in self.values:
            for value in self.suits:
                full_cards.append({ key: value})
        return full_cards


