t=0
for x in range(0,1000,3):
    print(x)
for y in range(0,1000,5):
    print(y)
if x%3==0:
    t=t+x
if y%5==0:
    t=t+y
if y==x:
    t = t + y
print("the total sum of the numbers is ",t)