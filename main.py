import mindThief as mt

myDeck = mt.MIND_THIEF()
print(myDeck._deck._cards)

print(myDeck.perkDict)

myDeck.perkDict["addTwoPlusOneRolling"]()
print(myDeck._deck._cards)

# myDeck._deck.shuffle()
# myDeck._deck.getData()
# print(myDeck._deck.cardTotal / myDeck._deck.cardEndx)
# print(myDeck._deck.missCount)
# print(myDeck._deck.missCount / myDeck._deck.cardEndx)
# print(myDeck._deck.critCount)
# print(myDeck._deck.critCount / myDeck._deck.cardEndx)
