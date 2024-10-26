library = [
    {"ID": 1, "Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Year of Publish": 1925},
    {"ID": 2, "Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Year of Publish": 1960},
    {"ID": 2, "Title": "To Kill ", "Author": "Harper Lee", "Year of Publish": 1980},
    {"ID": 3, "Title": "1984", "Author": "George Orwell", "Year of Publish": 1949},
    {"ID": 4, "Title": "Pride and Prejudice", "Author": "Jane Austen", "Year of Publish": 1813}
]

while True:
    print('\nWelcome to the Library Management System!')     
    print("1. Add books")
    print("2. View all books")
    print("3. Update a book")
    print("4. delete")
    print("5. Search for a Author")
    print("6. Exit") 
    option = int(input('Select an option: '))

    if option == 1:
        ID = int(input("Enter book ID: "))
        Title = input('Enter the name of the book: ')
        Author = input('Enter the name of the author: ')
        year_of_publish = int(input('Enter the year of publish: '))
        library.append({"ID": ID, "Title": Title, "Author": Author, "Year of Publish": year_of_publish})
        print("Book added successfully!")

    elif option == 2:
        if library:
            print("\nAll books in the library:")
            for book in library:
                print(f"Book ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Year of Publish: {book['Year of Publish']}")
        else:
            print("No books in the library.")

    elif option == 3:
        book_id_update = int(input("Enter the book ID to update: "))
        book_found = False
        for book in library:
            if book["ID"] == book_id_update:
                print("Current Title:", book["Title"])
                new_title = input("Enter new title (leave blank to keep current): ")
                book["Title"] = new_title or book["Title"]
                
                print("Current Author:", book["Author"])
                new_author = input("Enter new author (leave blank to keep current): ")
                book["Author"] = new_author or book["Author"]
                
                print("Current Year of Publish:", book["Year of Publish"])
                new_year = input("Enter new year (leave blank to keep current): ")
                book["Year of Publish"] = int(new_year) if new_year else book["Year of Publish"]
                
                print("Book updated successfully!\n")
                book_found = True
                break        
        if not book_found:
            print("Book not found.")

    elif option == 4:
        book_id_remove = int(input("Enter the book ID to remove: "))
        book_found = False
        for book in library:
            if book["ID"] == book_id_remove:
                library.remove(book)
                book_found = True
                print(f"Book with ID {book_id_remove} has been removed.")
                break
        if not book_found:
            print("Book not found.")

    elif option == 5:
        search_name = input("Enter the name of the Author to search: ").lower()
        found = False
        for book in library:
            if search_name in book["Author"].lower():
                print(f"Found: Book ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Year of Publish: {book['Year of Publish']}")
                found = True
        if not found:
            print("Book not found.")

    elif option == 6:
        print("Exiting the system...")
        break
    else:
        print("Invalid option. Please try again.")
