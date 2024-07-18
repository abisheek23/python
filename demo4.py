# for i in range(3):
#     i+=1
#     print("*")
#     for j in range(1):
#         print("#")
#         j+=2
#         print("*""#",end="\t")
#     print()    
for i in range(4):
    for j in range(4):
        print(j,end="\t")
    print()    
for i in range(4):
    for j in range(4):
        print(i,end="\t")
    print()    
# for i in range(3):
#     for j in range(3):
#         print(j,end="\t")
# for n in range(6,9):
#   print(n,end="\t")
#   print()    
a=0
for i in range(3):
    for j in range(3):
        print(a,end="\t")
        a+=1
    print()
# a=0
# for i in range(4):
#     print(a,end="\t")
#     a+=1
# print()
# for j in range(3):
#         print(a,end="\t")
#         a-=1
# print()
for i in range(4):
    a=2
    for j in range(3):
        if i%2==0:
            print(j,end="\t")
        else:
            print(a,end="\t")
            a-=1
    print("\n")

for i in range(4):
    a=0
    print(a,end="\t")
    for j in range(4):
     a+=1
    print(j,end="\t")
print("\n")  
for i in range(4):
    for j in range(4):
      print(i+j,end= "\t")
    print() 
 
# for i in range(1,6):
#     for j in range(i):
#         i-=1
#         print(i,end="\t")    
#     print()    

for i in range (6):

    for j in range(i):
        print((i+j)%2,end='\t')
    print()



for i in range(1,6):
    for j in range(i):
        if i%2==0:
            print('+',end=" ")
        else:
            print('#',end=" ")
    print()
