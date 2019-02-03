import random
import card
from datetime import datetime


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
        self.cardEndx = 100000
        self.cardTotal = 0
        self.missCount = 0
        self.critCount = 0
        self.populate()

    def populate(self):
        cards = []
        for i in range(self.numZero):
            cards.append(card.CARD("", 0, ""))
        for i in range(self.numPlusOne):
            cards.append(card.CARD("", 1, ""))
        for i in range(self.numPlusTwo):
            cards.append(card.CARD("", 2, ""))
        for i in range(self.numMinusOne):
            cards.append(card.CARD("", -1, ""))
        for i in range(self.numMinusTwo):
            cards.append(card.CARD("", -2, ""))
        cards.append(card.CARD("crit", 0, ""))
        cards.append(card.CARD("miss", 0, ""))

        self._cards = cards
        self._defaultCards = cards

    def shuffle(self):
        random.seed(datetime.now())
        random.shuffle(self._cards)

    def draw(self):
        drawCard = True
        while drawCard:
            drawCard = False
            indx = self.cardIndx
            self.cardTotal += self._cards[indx].number
            self.cardIndx += 1
            if self._cards[indx].rolling:
                drawCard = True

        if self._cards[indx].ability == "miss":
            self.missCount += 1
            self.cardIndx = 0
            self.shuffle()
        elif self._cards[indx].ability == "crit":
            self.critCount += 1
            self.cardIndx = 0
            self.shuffle()

    def getData(self):
        for i in range(self.cardEndx):
            self.draw()
