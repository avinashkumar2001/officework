import random
class dice:
    def roll():
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        dirs=( d1,d2)
        return dirs



print(dice.roll())