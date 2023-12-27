import sqlite3

db = sqlite3.connect('ebookstore.db')

cursor = db.cursor()

cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)''')
db.commit()

cursor = db.cursor()
id1 = 3001
Title1 = 'A Tale of Two Cities'
Author1 = 'Charles Dickens'
Qty1 = 30

id2 = 3002
Title2 = "Harry Potter and the Philosopher's Stone"
Author2 = "J.K. Rowling"
Qty2 = 40

id3 = 3003
Title3 = 'The Lion, the Witch and the Wardrobe'
Author3 = 'C.S. Lewis'
Qty3 = 25

id4 = 3004
Title4 = 'The Lord of the Rings'
Author4 = 'J.R.R Tolkien'
Qty4 = 37

id5 = 3005
Title5 = 'Alice in Wonderland'
Author5 = 'Lewis Carroll'
Qty5 = 12

books_list = [(id1, Title1, Author1, Qty1), (id2, Title2, Author2, Qty2), (id3, Title3, Author3, Qty3), (id4, Title4, Author4, Qty4), (id5, Title5, Author5, Qty5)]

cursor.executemany('''INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', books_list)
print("All books have successfully been added.")
db.commit()
db.close()

print("Connection to database off.")






