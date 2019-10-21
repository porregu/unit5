import random
user_games = input(int(" how many games you wanna play "))
dices1= random.randint(1,6)
dices2= random.randint(1,6)
total_dices=dices1+dices2
if total_dices==7 or total_dices== 11:
    print("you win")
elif total_dices==2 or total_dices== 3 or total_dices== 12:
    print("you lose ")
else:
    dices1 = random.randint(1, 6)
    dices2 = random.randint(1, 6)
    total2_dices= dices2+dices1
    if total_dices==total2_dices
