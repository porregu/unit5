import random
es=0
os=0
for x in range(10):
    d=((int)(random.randint(1,100)))
    print(d)
    m = d%2
    if m==0:
        es=es+d
    if m!=0:
        os=os+d
print("this is the sum of the even numbers",es)
print("this is the sum of the odd numbers",os)




