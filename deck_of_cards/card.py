from random import shuffle

class Card:
   def __init__(self, value, suit):
      self.value = value 
      self.suit = suit

   def __repr__(self):
      return f"{self.value} of {self.suit}"

class Deck:
   def __init__(self):
      suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
      values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
      self.cards = [Card(value, suit) for value in values for suit in suits]

   def count(self):
      return len(self.cards)
     
   def __repr__(self):
      return f"There are {self.count()} cards left in the deck"

   def _deal(self, num): # internal method - other methods will call on this method
      count = self.count()
      removal = min([count, num]) # so it can only remove cards when it's possible
      if count == 0:
         raise ValueError("No cards left!")
      hand = self.cards[-removal:]
      self.cards = self.cards[:-removal]
      return hand

   def deal_card(self):
      return self._deal(1)[0]
      
   def deal_hand(self, hand_size):
      return self._deal(hand_size)

   def shuffle(self):
      if self.count() < 52:
         raise ValueError("Only full decks can be shuffled")
      shuffle(self.cards)
      return self

d = Deck()
d.shuffle()

# card = d.deal_card()
# print(card)

d.deal_hand(51)
# print(d.cards[0])
