import random

from card import Card

class Deck:
    cards = []

    def __init__(self):
        self.cards = Card().create_cards()

    def __repr__(self) -> str:
        return f"Deck of {self.count()} cards"

    def _deal(self, qntd_to_remove) -> list:
        cards_removed = []
        if self.count() > 0:
            if qntd_to_remove < self.count():
               for card in range(self.count(), (self.count()-qntd_to_remove), -1):
                    cards_removed.append(self.cards.pop())
            else:
               for card in range(self.count(), 0, -1):
                    cards_removed.append(self.cards.pop())
            return cards_removed
        else:
            raise ValueError("All cards have been dealt")

    def count(self) -> int:
        return len(self.cards)

    def shuffle(self) -> list:
        if self.count() == 52:
            return random.shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, qntd_to_remove):
        return self._deal(qntd_to_remove)

card1 = Card()
print(card1)
my_deck = Deck()
print(my_deck)
my_deck.shuffle()
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(5)
print(hand)
print(my_deck)
