import random
from datetime import datetime


class CARD:
    def __init__(self, ability, number, rolling):
        self.ability = ability
        self.number = number
        self.rolling = rolling

    def __repr__(self):
        return self.ability + " " + str(self.number) + " " + self.rolling


class DECK:
    def __init__(self):
        self._cards = []
        self._defaultCards = []
        self.numZero = 6
        self.numPlusOne = 5
        self.numPlusTwo = 1
        self.numMinusOne = 5
        self.numMinusTwo = 1
        self.crit = 1
        self.miss = 1
        self.cardIndx = 0
        self.cardEndx = 1000000
        self.cardTotal = 0
        self.missCount = 0
        self.critCount = 0
        self.populate()

    def populate(self):
        cards = []
        for i in range(self.numZero):
            cards.append(CARD("", 0, ""))
        for i in range(self.numPlusOne):
            cards.append(CARD("", 1, ""))
        for i in range(self.numPlusTwo):
            cards.append(CARD("", 2, ""))
        for i in range(self.numMinusOne):
            cards.append(CARD("", -1, ""))
        for i in range(self.numMinusTwo):
            cards.append(CARD("", -2, ""))
        cards.append(CARD("crit", 0, ""))
        cards.append(CARD("miss", 0, ""))

        self._cards = cards
        self._defaultCards = cards

    def shuffle(self):
        random.seed(datetime.now())
        random.shuffle(self._cards)

    def draw(self):
        indx = self.cardIndx
        self.cardTotal += self._cards[indx].number
        self.cardIndx += 1

        if self._cards[indx].ability == "miss":
            myDeck.missCount += 1
            self.cardIndx = 0
            self.shuffle()
        elif self._cards[indx].ability == "crit":
            myDeck.critCount += 1
            self.cardIndx = 0
            self.shuffle()

    def getData(self):
        for i in range(self.cardEndx):
            self.draw()


myDeck = DECK()
print(myDeck._cards)
myDeck.shuffle()
myDeck.getData()
print(myDeck.cardTotal / myDeck.cardEndx)
print(myDeck.missCount)
print(myDeck.missCount / myDeck.cardEndx)
print(myDeck.critCount)
print(myDeck.critCount / myDeck.cardEndx)