import deck


class MIND_THIEF(deck.DECK):
    def __init__(self):
        self._deck = deck.DECK()
        self.numFrostPlusTwo = 0
        self.numPlusOneRolling = 0
        self.numPullRolling = 0
        self.numMuddleRolling = 0
        self.numImmobilizeRolling = 0
        self.numStunRolling = 0
        self.numDisarmRolling = 0
        self.perkList = []
        self.perkDict = {}
        self.buildDict()
        self.buildList()
        self.populate()

    def buildDict(self):
        self.perkDict['removeTwoMinusOne'] = self.removeTwoMinusOne
        self.perkDict['removeFourZero'] = self.removeFourZero
        self.perkDict['repTwoPlusOnePlusTwo'] = self.repTwoPlusOnePlusTwo
        self.perkDict['repMinusTwoZero'] = self.repMinusTwoZero
        self.perkDict['addFrostPlusTwo'] = self.addFrostPlusTwo
        self.perkDict['addTwoPlusOneRolling'] = self.addTwoPlusOneRolling

    def buildList(self):
        self.perkList.append('removeTwoMinusOne')
        self.perkList.append('removeTwoMinusOne')
        self.perkList.append('removeFourZero')
        self.perkList.append('repTwoPlusOnePlusTwo')
        self.perkList.append('repMinusTwoZero')
        self.perkList.append('addFrostPlusTwo')
        self.perkList.append('addFrostPlusTwo')
        self.perkList.append('addTwoPlusOneRolling')
        self.perkList.append('addTwoPlusOneRolling')

    def removeTwoMinusOne(self):
        self._deck.numMinusOne -= 2
        self.populate()

    def removeFourZero(self):
        self._deck.numZero -= 4
        self.populate()

    def repTwoPlusOnePlusTwo(self):
        self._deck.numPlusOne -= 2
        self._deck.numPlusTwo += 2
        self.populate()

    def repMinusTwoZero(self):
        self._deck.numMinusTwo -= 1
        self._deck.numZero += 1
        self.populate()

    def addFrostPlusTwo(self):
        self.numFrostPlusTwo += 1
        self.populate()

    def addTwoPlusOneRolling(self):
        self.numPlusOneRolling += 2
        self.populate()

    def populate(self):
        self._deck.populate()
        for i in range(self.numFrostPlusTwo):
            self._deck._cards.append(deck.card.CARD('frost', 2, ''))
        for i in range(self.numPlusOneRolling):
            self._deck._cards.append(deck.card.CARD('', 1, 'rolling'))
