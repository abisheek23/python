from  reg import*
from view import*
from upd import*
from deleat import*


data=[]
# while True:
#     print("1.add\n2.display\n3.update")
#     ch=int(input("enter your choice"))
#     if ch==1:
#        add(data)
while True:
    print("1. Add \n2. View \n3. Update \n4. Delete \n5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        add(data)
    elif ch == 2:
        dis(data)
    elif ch == 3:
        update(data)
    elif ch == 4:
        delete(data)
    # elif ch == 5:
#         exit(data)
        
