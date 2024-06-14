# a=int(input("enter the value"))
# b=int(input("enter the value"))
# sum=0
# for i in range (a,b+1):
#     sum+=i
# print(sum)
# a=int(input("enter the value"))
# b=int(input("enter the value"))
# sum=0
# for i in range(a,b+1):
#     if i%2!=0:
#         print(i)
#         sum+=i
#         print("the sum =",sum)
a=int(input("enter the value"))
b=int(input("enter the value"))
sum=0
sum1=0
sum2=0
for i in range(a,b+1):
    if i%2!=0:
        sum+=i
    if i%2==0:
         sum1+=i 
    sum2+=i
print("the sum of natural no =",sum2)
print("the sum of odd=",sum)
print("the sum of even =",sum1)




