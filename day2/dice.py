import random
class Dice:
    def roll(self):
        first = random.randint (0, 6)
        second = random.randint(0, 6)
        rand =  (first, second)
        print(rand)
        return rand
        # can be return first, second 



d1 = Dice()
d1.roll()
count = 1

while True:
    rand = d1.roll()
    count += 1

    if rand == (6,6): 
        print(f"it took {count} rolls")
        break