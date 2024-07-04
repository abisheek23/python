# l=[1,2,3,4,5,6,7,8,9]
# d1=filter(lambda a:a%2==0,l)
# print(list(d1))
# def fun1(a):
#     return a%2==0
# d1=filter(fun1,l)
# print(list(d1))

# l=['apple','mango']

# def fun1(a):
#     return a[1]=='a'
# d1=filter(fun1,l)
# print(list(d1))

import functools
l=[1,2,3,4,5]
data=functools.reduce(lambda total,value:total*value,l)
print(data)