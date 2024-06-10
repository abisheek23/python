# salary=int (input("enter the salary"))
# exp=int (input("enter the year of experianc"))
# if exp >=5:
#   salary+=salary*0.05
#   print (salary)
# else :
#    print("not ")
# number=int(input("enter the no"))
# lastdigit=number%10
# if lastdigit %3==0:
#     print("the last digit of the number is divicible by 3")
# else :
#     print("the number is not divisible by 3")
# day= int(input("enter the number"))
# if day==1:
#     print("monday")
# elif day==2:
#     print("tusday")
# elif day==3:
#     print("wenesday")
# elif day==4:
#     print("thursday")
# elif day==5:
#     print("friday")
# elif day==6:
#     print("saterday")
# elif day==7:
#     print("sunday")
# else:
#     print("invalid umber")
# city=str(input("enter the city" ))
# if city=="delhi":
#     print("red fort")
# elif city=="agra":
#     print("taj mshsl")
# elif city=="jaipur":
#     print("jai mahal")
# else :
#     print("wrong city")   
unit=int(input("enter the units"))
if unit<=100:
    print("no charges")
elif unit<=200:
    print((unit-100)*5,"is the charg")
else :
    print(((unit-200)*10)+500,"is the chatg")