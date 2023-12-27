import sqlite3

from tabulate import tabulate

db = sqlite3.connect('ebookstore.db')


# Function 1: Enter book details
def enter_book():
    cursor = db.cursor()

    id = int(input("\nEnter book ID: "))
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    qty = int(input("Enter the book quantity: "))

    cursor.execute('''INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', (id, title, author, qty))
    db.commit()
    print("Book added successfully")


# Function 2: Update book
def update_book():
    cursor = db.cursor()
    book_id = int(input("\nHi, please enter the book ID number: "))
    cursor.execute('''SELECT * FROM books WHERE id LIKE?''', (book_id,))
    book = cursor.fetchall()
    headers = ["ID", "Title", "Author", "Qty"]
    print("\nEditing book:")
    print(tabulate(book, headers=headers))



    selection = input("""
    What would you like to edit:
    1. Title
    2. Author
    3. Quantity
    
    Enter here: """)

    if selection == '1':
        selection = 'Title'

        cursor.execute('''SELECT Title FROM books WHERE id = ?''', (book_id,))
        current_title = cursor.fetchone()[0]
        print(f"\nCurrent Title: {current_title} ")

        updated_title = input("\nPlease enter updated title: ")
        cursor.execute(f'''UPDATE books SET {selection} = ? WHERE id = ?''', (updated_title, book_id))
        db.commit()
        print("Title successfully updated.")

    elif selection == '2':
        selection = 'Author'

        cursor.execute('''SELECT Author FROM books WHERE id = ?''', (book_id,))
        current_author = cursor.fetchone()[0]
        print(f"\nCurrent Author: {current_author} ")

        updated_author = input("\nPlease enter up-to-date author: ")
        cursor.execute(f'''UPDATE books SET {selection} = ?  WHERE id = ?''', (updated_author, book_id))
        db.commit()
        print("Author successfully updated.")

    elif selection == '3':
        selection = 'Qty'
        cursor.execute('''SELECT Qty FROM books WHERE id = ?''', (book_id,))
        current_qty = cursor.fetchone()[0]
        print(f"\nCurrent quantity: {current_qty} ")
        updated_quan = int(input("\nPlease enter updated quantity: "))
        cursor.execute(f'''UPDATE books SET {selection} = ? WHERE id = ?''', (updated_quan, book_id))
        db.commit()
        print("Quantity successfully updated.")


# Function 3: Delete book
def delete_book():
    cursor = db.cursor()
    book_id = int(input("\nEnter book ID: "))
    cursor.execute('''SELECT * FROM books WHERE id = ?''', (book_id,))
    rows = cursor.fetchall()
    print(f"\nDeleting book: {rows}")
    cursor.execute('''DELETE FROM books WHERE id = ?''', (book_id,))
    db.commit()
    print("Book deleted successfully.")


# Function 4: Search for book
def search_books():
    cursor = db.cursor()

    book_id = input("\nPlease enter book id to search for:  ")
    cursor.execute('''SELECT * FROM books WHERE id = ? ''', (book_id,))
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("\nNo books found. Please enter the correct book ID")

    else:
        for row in rows:
            print(f"""
            ID: {row[0]}
            Title: {row[1]}
            Author: {row[2]}
            Quantity: {row[3]} 
                        """)
    db.commit()


# Function 5: Display all books
def display_books():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    headers = ["ID", "Title", "Author", "Qty"]
    print("\nAll books:")
    print(tabulate(books, headers=headers))
    db.commit()


# Function 6: display menu
# Main program which displays the menu and calls all the relevant functions
def menu():
    print("\n========= Bookstore Clerk Program =========")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("5. View all books")
    print("0. Exit")
    return input("\nEnter your choice: ")



while True:
    choice = menu()

    if choice == '1':
        enter_book()

    elif choice == '2':
        update_book()

    elif choice == '3':
        delete_book()

    elif choice == '4':
        search_books()

    elif choice == '5':
        display_books()

    elif choice == '0':
        print("Goodbye!")
        exit()

    else:
        print("\n========= Please select a valid option! =========")













