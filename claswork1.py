def claswork1():
    numbers = range(21,0, -1)
    for i in numbers:
        print(i)
    un=(int(input("what is the maximun number you want ?")))
    for x in range(1, un):
        print(x)
    un2=(int(input("what is the minimun number you want ?")))
    if un<un2:
        print(" the minimun number is bigger than the maximun number")
        for a in range(un2,un,-1):
            print(a)
print(claswork1())