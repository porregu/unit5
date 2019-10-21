import random
user_games = int(input(" how many games you wanna play "))
dices1= random.randint(1,6)
dices2= random.randint(1,6)
total_dices=dices1+dices2
print(total_dices)
if total_dices==7 or total_dices== 11:
    print("user win")
elif total_dices==2 or total_dices== 3 or total_dices== 12:
    print("user lose ")
else:
    while True:
        dices1 = random.randint(1, 6)
        dices2 = random.randint(1, 6)
        total2_dices= dices2+dices1
        print(total2_dices)
        if total_dices==total2_dices:
            print("user won")
            break
        if total2_dices==7:
            print("user lose")
            break
