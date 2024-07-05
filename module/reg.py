def add(data):
    name=input("enter your name:")
    id=int(input("enter id:"))
    age=int(input("enter your age:"))
    place=(input("enter your place:"))
    data.append({"name":name,"id":id,"age":age,"place":place})