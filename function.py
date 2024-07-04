# def fun_1():
#     a=int(input("enter the no"))
#     b=int(input("enter the no"))
#     print(a+b)
# fun_1()

"ARITHEMATIC"

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
# def mul(a,b):
#     return a*b
mul=lambda a,b:a*b
# def mod(a,b):
#     return a%b
mod=lambda a,b:a%b
def numbers():
    a=int(input("enter first no:"))
    b=int(input("enter second no:"))
    return a,b 
while True:
    print("1.add \n2.sub\n3.mul\n4.mod")
    ch=int(input("enter your choice:"))
    if ch==1:
        a,b=numbers()
        print(add(a,b))
    elif ch==2:
        a,b=numbers()
        print(sub (a,b))
    elif ch==3:
        a,b=numbers()
        print(mul(a,b))
    elif ch==4:
        a,b=numbers()
        print(mod(a,b))
    elif ch==5:
        break
# add=lambda a,b,c:a+b+c
# print(add(10,12,15))
