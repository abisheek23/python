def delete(data):
    id_to_delete = int(input("Enter the ID to delete: "))
    for record in data:
            if record['id'] == id_to_delete:
                data.remove(record)
                print("Record deleted")
                break
    else:
        print("ID not found")