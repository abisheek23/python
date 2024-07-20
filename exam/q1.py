
"How to remove duplicates in a list using for loop?"
# a=[]
# l=[10,20,30,40,40,50,]
# print(l)
# for i in l:
#     if i not in a:
#      a.append(i)
# print(a)

""". Write a Python program to print the following pattern:

A	
B	A
C	B	A
D	C	B	A
"""
# for i in range(0,4):
#     for j in range(i, -1, -1):
#         print(chr(65 + j), end='\t')
#     print()


"""Write a Python function to calculate the factorial of a given number?"""
num= int(input("Enter a number: "))
a= 1
for i in range(1, num + 1):
        a *= i
print(f"The factorial of {num} is {a}.")


