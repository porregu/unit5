import random
def role_dices():
    """
    this function makes the role of the dices reapet and make less codes
    :return:
    """
    dices1 = random.randint(1, 6)#role dice and pick a random number
    dices2 = random.randint(1, 6)#role dice and pick a random number
    total_dices = dices1 + dices2# make the total of the two dices
    return total_dices
user_games = int(input("how many games you want play today? "))
total_wins=0#for later calculate the number of wins
total_lose=0#for later calculate the number of loses
for x in range (user_games):

    total_dices=role_dices()
    #print("this is your totlat dices",total_dices)
    if total_dices==7 or total_dices== 11:
        total_wins=total_wins+1
        #print("user win")
    elif total_dices==2 or total_dices== 3 or total_dices== 12:
        total_lose=total_lose+1
        #print("user lose ")
    else:
        while True:
            total2_dices= role_dices()
            #print("this is your total for your second try",total2_dices)
            if total_dices==total2_dices:
                total_wins = total_wins + 1
                #print("user won")
                break
            if total2_dices==7:
                total_lose = total_lose + 1
                #print("user lose")
                break
print(" the user win",total_wins,"times")
print(total_wins/user_games*100,"%","of wins")
print(total_lose/user_games*100,"%","of loses")