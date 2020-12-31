class Dice():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        from random import randint
        x = randint(1, self.sides)
        print(x)


dice_six = Dice()
print("\nRoll the dice with " + str(dice_six.sides) + " sides for 10 times:")
for rolldice in range(10):
    dice_six.roll_dice()

dice_ten = Dice(10)
print("\nRoll the dice with " + str(dice_ten.sides) + " sides for 10 times:")
for rolldice in range(10):
    dice_ten.roll_dice()


dice_twenty = Dice(20)
print("\nRoll the dice with " + str(dice_twenty.sides) +
      " sides for 10 times:")
for rolldice in range(10):
    dice_twenty.roll_dice()
