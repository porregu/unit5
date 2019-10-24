user_number = int(input("what number do you want to put?"))
while user_number!=1:
    print(user_number)
    if user_number%2==0:
        user_number/=2
        print(user_number*2,"/ 2 =",user_number)
    else:
        user_number=user_number*3+1
        print(user_number/3-1,"*3+1 = ",user_number)


