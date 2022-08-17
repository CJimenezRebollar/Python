import random
roll = random.randint(1,6)
guess = int(input('GUess the dice roll:\n'))
if guess == roll:
    print("You win! They rolled a " + str(roll))
else:
    print("You lose! They rolled a " + str(roll))
