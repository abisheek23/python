# while True:
#     try:
#         a=int(input("enter  the number:"))
#         print(a)
#         break
#     except:
#         print("enter a number")

# l=[1,2,3,4.5,'abc',10]
# sum=0
# for i in l:
#         try:
#             sum+=i         
#     # if type (i)==int or type (i)==float:
#         except:
#             pass
# print(sum)

try:
    print(10+'36')
except TypeError:
    print('its type error')
else:
    print("else")
finally:
    print('finally')