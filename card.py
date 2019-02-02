class CARD:
    def __init__(self, ability, number, rolling):
        self.ability = ability
        self.number = number
        self.rolling = rolling

    def __repr__(self):
        return self.ability + " " + str(self.number) + " " + self.rolling
