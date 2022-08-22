import random
com_score = random.randint(1,100)
player_score = int(input('Choose a number 1-100:\n'))
high_score = 3
if player_score > com_score:
    print("Congratulations, you win!")
    win_counter = wins = +1
elif player_score == com_score:
    print("It's a tie")
else:
    print("Sorry, you lose.")
if win_counter > high_score:
    print("You have the new High Score!")
else:
    print("Try aiming for the High Score.")