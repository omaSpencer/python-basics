import random

for i in range(3):
    print(random.randint(10, 20))

members = ['Spencer', 'Roland', 'Ádám']
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)


dice = Dice()
print(dice.roll())
