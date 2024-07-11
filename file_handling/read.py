"importent"

# f=open('python/file_handling/new2.txt','a')
# f.write("absdfvdesx")

# t=open('python/file_handling/new2.txt','r')
# print(t.read())

# t=open('python/file_handling/new2.txt','r')
# print(t.readlines())
# print('_'*20)
# print(t.read())
"to find number of words in a text file"
t=open('python/file_handling/new2.txt','r')
l=len(t.readlines())
t.seek(0)
word=0
let=0
for i in range(l):
    a=t.readline().strip()
    for j in a:
        if j==0:
            word+=1
        else:
            let+=1
    print(a[::-1])
    word+=1
print(word)
print(let)

t=open('python/file_handling/new2.txt','r')
l=len(t.readlines())
t.seek(0)
word=0
let=0
cap=0
smal=0
for i in range(l):
    a=t.readline().strip()
    for j in a:
        if j==0:
            word+=1
        else:
            let+=1
            if j.isupper():
                cap+=1
            else:
                smal+=1
                print(a[::-1])
    word+=1
print(word)
print(let)
print(cap)
print(smal)




