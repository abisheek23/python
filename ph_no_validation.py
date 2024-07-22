"""importent"""

"phone number validation"
# import re
# a=str(input('enter your ph number:'))
# if len(a)==10 and a.isdigit():
#     if re.search('[6-9].{9}',a):
#         print('valid',a)
#     else:
#         print('not valid')
# else:
#     print('not valid')

"email validation"
import re
a=input("enter your email")
pattern = r"^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]).{8,}$"
if re.search(pattern,a):
    print ("valid")
else:
    print("invalid")



    


