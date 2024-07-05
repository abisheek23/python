"""type of fuction"""

"""function with positional argument"""

# def add(a,b):
#     return a+b
# print(add(10,20))
# print(add('asd','qwe'))

"""function with default parameter value"""

# def add(name,age=20):
#     return name,age
# print(add('saan',35))
# print(add('praan',))

'''function with keyword argument'''

# def add(name,age):
#     print('name :',name)
#     print('age',age)

# add('saan',35)
# add(age=45,name='insaan')

'''function with arbitury argument'''

# def add(*a):# *used to select the arguments
#     return a
# print(add('saan',35))
# print(add())

'''function with arbitury keyword argument'''

def add(**a):# *used to select the arguments
    return a
print(add(name='saan',age=35,place='ekm'))

print(add())