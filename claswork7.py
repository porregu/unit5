import random
def user_times():
    product=1
    number_numbers=0
    sum_all=0
    while True:
        user_number=(input("what number do you want to put?"))
        if user_number=="q":
            break
        else:
            user_number=int(user_number)
            sum_all=sum_all+user_number
            number_numbers+=1
            product*=user_number
            avergeae=sum_all/number_numbers
    print(product," this is the product of all the number combined")
    print(sum_all,"this is the sum of all the numbers ")
    print(number_numbers,"this is the times the user put a integir")
    print(avergeae,"this is the averege number")
user_times()








