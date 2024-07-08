# def up (data):
#     id=input("enter user id to update")
#     for i in data:
#         if i ["id"]==id:
#             print("current name:"+i['name'])
#             new_name=input("enter new name(leave blank to keep current):")
#             i['name']=new_name or i['name']

#             print("current age :"+i['age'])
#             new_age=input("")
def update(data):
    id_to_update = int(input("Enter the ID to update: "))
    for record in data:
        if record['id'] == id_to_update:
            print("Current Name: " + record['name'])
            new_name = input("Enter new name (leave blank to keep current): ")
            record['name'] = new_name or record['name']

            print("Current Age: " + str(record['age']))
            new_age = input("Enter new age (leave blank to keep current): ")
            if new_age:
                record['age'] = int(new_age)

            print("Current Place: " + record['place'])
            new_place = input("Enter new place (leave blank to keep current): ")
            record['place'] = new_place or record['place']

            print("Record updated")
            break
    else:
        print("ID not found")