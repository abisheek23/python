recipes =[]

while True:
    print("Recipe Book")
    print("1. Add Recipe")
    print("2. View Recipes")
    print("3. Update Recipe")
    print("4. Delete Recipe")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice==1:
        recipe_id = input("Enter Recipe ID: ")
        if recipe_id in recipes:
            print("Recipe ID already exists. Please enter a unique ID.\n")
        else:
            name = input("Enter Recipe Name: ")
            ingredients = input("Enter Ingredients (comma separated): ").split(',')
            instructions = input("Enter Instructions: ")
            recipes[recipe_id] = {"name": name, "ingredients": ingredients, "instructions": instructions}
            print("Recipe added successfully!\n")
    elif choice==2:
        if not recipes:
            print("\nNo recipes available.\n")
        else:
            print("\n{:<10} {:<20} {:<50}".format("ID", "Name", "Ingredients"))
            print("-" * 80)
            for recipe_id, details in recipes.items():
                print("{:<10} {:<20} {:<50}".format(recipe_id, details['name'], ', '.join(details['ingredients'])))
                print("Instructions: " + details['instructions'])
                print("-" * 80)
            print("")
    elif choice==3:
        recipe_id = input("Enter Recipe ID to update: ")
        if recipe_id in recipes:
            print("Current Name: " + recipes[recipe_id]['name'])
            new_name = input("Enter new name (leave blank to keep current): ")
            recipes[recipe_id]['name'] = new_name or recipes[recipe_id]['name']
            
            print("Current Ingredients: " + ', '.join(recipes[recipe_id]['ingredients']))
            new_ingredients = input("Enter new ingredients (comma separated, leave blank to keep current): ")
            recipes[recipe_id]['ingredients'] = new_ingredients.split(',') if new_ingredients else recipes[recipe_id]['ingredients']
            
            print("Current Instructions: " + recipes[recipe_id]['instructions'])
            new_instructions = input("Enter new instructions (leave blank to keep current): ")
            recipes[recipe_id]['instructions'] = new_instructions or recipes[recipe_id]['instructions']
            
            print("Recipe updated successfully!\n")
        else:
            print("Recipe not found!\n")
    
    elif choice==4:
        recipe_id = input("Enter Recipe ID to delete: ")
        if recipe_id in recipes:
            del recipes[recipe_id]
            print("Recipe deleted successfully!\n")
        else:
            print("Recipe not found!\n")
    
    elif choice==5:
        print("Exiting the system. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.\n")
