import random


def roll(dice_list, keep_number=None):
    for index, die in enumerate(dice_list):
        if keep_number is None or die != keep_number:
            dice_list[index] = random.choice(range(1, 7))
    return dice_list


dice = [None] * 10
input("Press enter to start")
dice = roll(dice)
print(dice)
target_number = max(dice, key=dice.count)  # Automatically resolves ties
dice_to_reroll = 10 - dice.count(target_number)
while dice_to_reroll > 0:
    dice = roll(dice, target_number)
    dice_to_reroll = 10 - dice.count(target_number)
print("TENZI")
print(dice)