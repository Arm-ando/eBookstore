# Ebookstore Management System

<h2>Project Summary</h2>
This ebookstore management system is a comprehensive program designed to streamline the tasks of a bookstore clerk, providing efficient management of the bookstore's inventory. The program offers a user-friendly interface that allows the clerk to perform key operations, such as adding new books, updating book information, deleting books, and searching the database for specific titles.

<h2>Project Structure</h2>
<h4>ebookstore_db.py:</h4>
<li>This script contains the code responsible for populating the database with initial data. When executed, it creates a file named ebookstore_db in the \data directory. The main program will subsequently open and interact with this database file</li>

<h4>ebookstore_main.py:</h4>
<li>This is the main program responsible for managing the ebookstore database. It opens and interacts with the ebookstore_db file, facilitating operations such as adding new books, updating book information, deleting books, and searching the database for specific titles</li>

<h2>Database Structure</h2>
<h4>The system is backed by a robust database named "ebookstore," featuring a well-defined table named "books." The table's structure includes essential fields:</h4>
<li><b>id:</b> Unique identifier for each book.</li>
<li><b>Title:</b> The title of the book.</li>
<li><b>Author:</b> The author of the book.</li>
<li><b>Qty:</b> The quantity of available copies in the inventory.</li>

###
The initial data in the table includes a selection of classic books, and the clerk has the flexibility to add additional entries to cater to the specific inventory of the bookstore.

<h2>User Interaction</h2>
<h4>The program provides an intuitive menu-driven interface for the clerk to interact with the system. The main menu offers the following options:</h4>

<ol type ="1">
<li><b>Enter book:</b> Add new books to the database.</li>
<li><b>Update book:</b> Modify and update existing book information.</li>
<li><b>Delete book:</b> Remove books from the database.</li>
<li><b>Search books:</b> Find specific books based on title, author, or other criteria.</li>
<li><b>Exit:</b> Close the program.</li>
</ol>

<h2>How to Run the Program</h2>
<h4>To use the ebookstore management system:</h4>
<ol type ="1">
<li>Set up a database named "ebookstore."</li>
<li>Create a table named "books" with the specified structure.</li>
<li>Populate the table with initial values or add your own entries.</li>
<li>Run the program and navigate through the menu options to perform desired operations.</li>
</ol>

The project emphasizes the practical application of fundamental programming concepts, offering a versatile solution for bookstore clerks to efficiently manage their inventory.
