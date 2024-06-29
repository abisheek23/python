std=[]
for i in range(3):
    name=input('enter the name:')
    age=int(input('enter the age:'))
    place=input('enter the place:')
    ph_no=int(input('enter the phone no:'))
    std.append({'name':name,'age':age,'place':place,'ph_no':ph_no,})
print(std)
print("{:<10}{:<6}".format('name','age'))
print('_'*20)
for i in std:
    print("{:<10}{:<6}")