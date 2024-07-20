from q21 import *
print("1.add \n 2.sub \n 3.mult \n 4.div \n 5.mod")
while True:
 x=int(input("enter the no:"))
 y=int(input("enter second no:"))
 a=int(input("enter your choice:"))
 if a==1:
     add(x+y)
 elif a==2:
    subtract(x-y)
 elif a==3:
    multiply(x*y)
 elif a==4:
    divide(x/y)
 elif a>4:
    print("invalid no")
    break