import deck

myDeck = deck.DECK()
print(myDeck._cards)
myDeck.shuffle()
myDeck.getData()
print(myDeck.cardTotal / myDeck.cardEndx)
print(myDeck.missCount)
print(myDeck.missCount / myDeck.cardEndx)
print(myDeck.critCount)
print(myDeck.critCount / myDeck.cardEndx)