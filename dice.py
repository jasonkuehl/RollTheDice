from random import randint
import random

DiceNumber = int(input("Dice Side Number: "))
RollTimes = int(input("How Many Dice To Roll: "))

for rollin in range(RollTimes):
    result =random.randint(1, DiceNumber)
    print(f"Dice Number - {result}")