

x=int(input("enter the number"))
t=0
while x>=0:
    r=x%10
    t=t*10+r
    x=x//10
print("revers no",t)