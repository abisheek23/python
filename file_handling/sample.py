name=[]
f=open('python/file_handling/new3.text','x')
a=int(input("enter the limit :"))
for i in range(a):
    b=str(input("enter the name"))
    name.append(b)
    f.write(b)
print(name)
