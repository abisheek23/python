l=[1,2,3,4,5,6,7,8,9]

# data=map(lambda a:a**2,l)
# print(data)
# print(list(data))
print(l)
def fun1(a):
    return a**2
data=map(fun1,l)
print(list(data))