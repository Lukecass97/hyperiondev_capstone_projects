import sqlite3
import shutil
import os

# Create database.
conn = sqlite3.connect('ebookstore.db')

# Get cursor.
cursor = conn.cursor()


def add_book():

    '''This function will take user input to add a new book to the database.
    The values input will then be entered into the "book" and "author" tables.
    '''

    while True:
        # Try-except for error handling.
        try:
            # User inputs details of the book they are adding.
            book_id = int(input('''Enter the 4 digit ID of the book you would 
like to add:\n'''))   

            # If ID entered isn't an integer with exactly 4 characters
            # error message displayed.
            if len(str(book_id)) == 4:

                cursor.execute('''SELECT * FROM book 
                                  WHERE id = ?''', (book_id,))

                # If ID entered is already in database, user notified.
                if cursor.fetchone():
                    print("Book is already in database.")

                else:
                    break

            else:
                print("Invalid entry! ID must be a 4 digit number.")

        except ValueError:
            print("Invalid entry! ID must be a 4 digit number.")
    
    book_name = input("Enter the title of the book:\n")
    
    while True:
        try:
            book_author_id = int(input("Enter the 4 digit AuthorID:\n"))
            
            # If AuthorID entered isn't an integer with exactly 4 characters
            # error message displayed. 
            if len(str(book_author_id)) == 4:
                break
            
            else:
                print("Invalid entry! AuthorID must be 4 digits.")
        
        except ValueError:
            print("Invalid entry! AuthorID must be 4 digits.")

    while True: 
        # Error message if integer not entered for quantity.   
        try:
            book_qty = int(input("Enter the quantity of this book:\n"))
            break

        except ValueError:
            print("Invalid entry! Quantity must be a number.")

    author = input("Enter the name of the author:\n")

    author_country = input("Enter the country the author is from:\n")

    # Tuple created.
    new_book_info = (book_id, book_name, book_author_id, book_qty)
        
    # Insert data into book table.
    cursor.execute('''INSERT INTO book
                      VALUES(?, ?, ?, ?)''', 
                      new_book_info)
    
    new_author_info = (book_author_id, author, author_country)
    
    # Insert data into author table.
    cursor.execute('''INSERT INTO author
                      VALUES(?, ?, ?)''',
                      new_author_info)
    
    # Print confirmation message.
    print(f'''"{book_name}" added to database.''')

    # Commit.
    conn.commit()


def update_book():

    '''This function will update book information. The user will enter the
    ID of the book they wish to update and then be presented with option on
    what piece of information they would like to update. The "book" table 
    will then be updated with this new information.
    '''

    while True:
        try:
            # User inputs book ID they wish to update.
            book_to_update = int(input('''Enter the 4 digit ID of the book you 
wish to update:\n'''))
            
            if len(str(book_to_update)) == 4:

                cursor.execute("SELECT * FROM book WHERE id = ?", 
                                (book_to_update,))

                book_found = cursor.fetchone()
                
                # Displays the book so user knows they have the right book.
                if book_found:
                    print("Book to udpate:")
                    print(
f'''-----------------------------------------------------------
ID: {book_found[0]}
Title: {book_found[1]}
AuthorID: {book_found[2]}
Quantity: {book_found[3]}
-----------------------------------------------------------''')
                    break

                else:
                    print("Book is not in database.")
                    
            else:
                print("Invalid entry! ID must be a 4 digit number.")
        
        except ValueError:
            print("Invalid entry! ID must be a 4 digit number.")
                
    while True:
        # try-except shows error if integer not entered.
        try:
            # User selects which piece of info they want to update.
            info_to_update = int(input(f'''\nWhat information would you 
like to update?
Enter the number of one of the following options:
1: Book ID
2: Book title
3: Quantity of the book
4: Exit\n'''))

            # Update book ID.
            if info_to_update == 1:
                while True:
                    try:
                        new_id = int(input("Enter the new 4 digit ID:\n"))

                        if len(str(new_id)) == 4:

                            id_update = (new_id, book_to_update)
                            
                            cursor.execute('''UPDATE book SET id = ?
                                              WHERE id = ?''', 
                                              id_update)
                            
                            # Confirmation message.
                            print(f'''ID updated to "{new_id}".''')

                            conn.commit()
                            break

                        else:
                            print(f'''Invalid entry! ID must be a 4 digit
number.''')
                    
                    except ValueError:
                        print("Invalid entry! ID must be a 4 digit number.")

            # Update book title.
            elif info_to_update == 2:
                new_title = input("Enter the new title of the book:\n")

                title_update = (new_title, book_to_update)

                cursor.execute('''UPDATE book SET title = ? 
                                  WHERE id = ?''', 
                                  title_update)
        
                # Confirmation message.
                print(f'''Title updated to "{new_title}".''')

                conn.commit()

            # Update quantity.
            elif info_to_update == 3:
                while True:
                    try:
                        new_qty = int(input(f'''Enter the new quantity of this
book:\n'''))
                        
                        qty_update = (new_qty, book_to_update)

                        cursor.execute('''UPDATE book SET qty = ?
                                          WHERE id = ?''', 
                                          qty_update)
        
                        # Confirmation message.
                        print(f'''Quantity updated to "{new_qty}".''')

                        conn.commit()
                        break
                    
                    except ValueError:
                        print("Invalid entry! Quantity must be a number.")

            # Update nothing.
            elif info_to_update == 4:
                print("You have exited.")
                break
          
            else:
                print("Invalid entry! Please enter a number.")

        except ValueError:
            print("Invalid entry! Please enter a number.")
    

def author_update():

    '''This function will update author information. The user will enter the
    authorID of the author whose information they would like to update and 
    then select what information they would like to change. The new 
    information will be entered into the "author" table. If the authorID is 
    updated, the authorID in the "book" table will also be updated.
    '''
    
    while True:
        try:
            author_to_update = int((input(f'''Enter the 4 digit AuthorID 
of the author you would like to update:\n''')))
            
            if len(str(author_to_update)) == 4:

                cursor.execute('''SELECT * FROM author where id = ?''', 
                                 (author_to_update,))
    
                author_found = cursor.fetchone()

                # Displays info of author.
                if author_found:
                    print("Author to update")
                    print(
f'''-----------------------------------------------------------
AuthorID: {author_found[0]}
Author: {author_found[1]}
Country: {author_found[2]}
-----------------------------------------------------------''')
                    break
                    
                # If AuthorID not found, error message shown.    
                else:
                    print("AuthorID not found! Please try again.")
            
            else:
                print("Invalid entry! AuthorID must be a 4 digit number.")

        except ValueError:
            print("Invalid entry! AuthorID must be a 4 digit number.")
            
    while True:
        try:
            # User selects what info they would like to update.
            update_details = int(input(f'''\nWhat details would you like 
to update?
Enter the number of one of the following options:
1: AuthorID
2: Author
3: Country
4: Exit\n'''))
                
            # Update AuthorID.    
            if update_details == 1:
                while True:
                    try:
                        new_auth_id = int(input("Enter the new AuthorID:\n"))

                        if len(str(new_auth_id)) == 4:

                            auth_id_update = (new_auth_id, author_to_update)
                            
                            cursor.execute('''UPDATE author SET id = ?
                                              WHERE id = ?''',                                               
                                              auth_id_update)
                            
                            conn.commit()
                            
                            # Update book table.
                            cursor.execute('''UPDATE book 
                                              SET authorID = (
                                              SELECT id
                                              FROM author
                                              WHERE id = ?)
                                              WHERE authorID = ? 
                                              ''',
                                              (new_auth_id, author_to_update))
        
                            print(f'''AuthorID updated to "{new_auth_id}".''')

                            conn.commit()
                            break

                        else:
                            print(f'''Invalid entry! AuthorID must be a
4 digit number.''')
                    
                    except ValueError:
                        print(f'''Invalid entry! AuthorID must be a 
4 digit number.''')

            # Update author's name.
            elif update_details == 2:
                new_author = input("Enter the new name of author:\n")

                name_update = (new_author, author_to_update)

                cursor.execute('''UPDATE author SET name = ?
                                  WHERE id = ?''',
                                  name_update)
                    
                print(f'''Author name changed to "{new_author}".''')

                conn.commit()
        
            # Update country of author.
            elif update_details == 3:
                new_country = input("Enter the new country of author:\n")

                country_update = (new_country, author_to_update)

                cursor.execute('''UPDATE author SET country = ?
                                  WHERE id = ?''',
                                  country_update)
                    
                print(f'''Country of author changed to "{new_country}".''')

                conn.commit()
            
            # Update nothing.
            elif update_details == 4:
                print("You have exited.")
                break

            else:
               print("Invalid entry! Please enter a number.")
                
        except ValueError:
            print("Invalid entry! Please enter a number.")


def delete_book():

    '''This function will delete a book that the user selects. They will enter
    the ID of the book they wish to delete and the program will show them
    the book they have selected, asking them if this is the book they want to 
    delete. They will be given the option to delete or not delete. If they 
    select delete the book will be deleted from the database.
    '''
    
    while True:
        try:
            book_to_delete = int(input('''Enter the 4 digit ID of the book you 
wish to delete:\n'''))
    
            if len(str(book_to_delete)) == 4:

                cursor.execute('''SELECT * FROM book WHERE id = ?''', 
                                  (book_to_delete,))
        
                result = cursor.fetchone()
    
                if result:
                    # Displays book they have selected to delete.
                    print(f'''You have entered the ID for "{result[1]}". 
Is this the book you wish to delete?''')
                    break

                else:
                    print("Book not in database.")

            else:
                print("Invalid entry! ID must be a 4 digit number.")

        except ValueError:
            print("Invalid entry! ID must be a 4 digit number.")

    while True:
        try:
            # User selects either 1 to delete or 2 to not delete.
            choice = int(input("Enter 1 for yes or 2 for no:\n"))
        
            if choice == 1:
                cursor.execute('''DELETE FROM book WHERE id = ?''',
                                  (book_to_delete,))
            
                # Deletion confirmation message.
                print(f'''"{result[1]}" has been deleted from the 
database.''')
                conn.commit()
                break
 
            elif choice == 2:
                # Message to confirm book was not deleted if 2 selected.
                print(f'''"{result[1]}" not deleted.''')
                break

            else:
                print("Invalid entry! Please enter either 1 or 2.")

        except ValueError:
            print("Invalid entry! Please enter either 1 or 2.")
                                   
        
def search_book():

    '''This function will search for a specific book that the user enters.
    They will enter the book ID and the corresponding book will be printed
    to the terminal. If they enter an ID that is not in the database, an 
    error message will be shown.
    '''
    
    while True:
        try:
            search = int(input('''Enter the 4 digit ID of the book you wish 
to search for:\n'''))
            
            if len(str(search)) == 4:
                cursor.execute('''SELECT * FROM book WHERE id = ?''',
                                  (search,))
    
                result = cursor.fetchone()
    
                if result:
                    # Prints search results in user friendly way.
                    print("Search results:")
                    print(
f'''-----------------------------------------------------------
ID: {result[0]}
Title: {result[1]}
AuthorID: {result[2]}
Quantity: {result[3]}
-----------------------------------------------------------''')
                    break

                else:
                    print("Book not in database.")

            else:
                print("Invalid entry! ID must be a 4 digit number.")
        
        except ValueError:
            print("Invalid entry! ID must be a 4 digit number.")


def view_all():

    '''This function will show all the book details of the books in the
     database. 
    '''

    # INNER JOIN to retrieve data from both tables.
    cursor.execute('''SELECT book.title, author.name, author.country 
                      FROM book
                      INNER JOIN author
                      ON book.authorID = author.id''' )
    
    results = cursor.fetchall()

    # Prints in a user friendly way.
    print("Details")
    for row in results:
        print(
f'''-----------------------------------------------------------
Title: {row[0]}
Author: {row[1]}
Country: {row[2]}
-----------------------------------------------------------''')
        
    conn.commit()


def backup(source_filename, dest_filename):

    '''In this function the shutil.copyfile() function from the shutil
    module is used to create a copy of the database file, named 
    "ebookstore_backup.db".
    '''
    
    shutil.copyfile(source_filename, dest_filename)

    print("Backup performed successfully!")
    print("Data saved to ebookstore_backup.db")


def restore(backup_filename, db_filename):

    '''In this function the shutil.copyfile() function will retore the database 
    by copying the backup file over the existing database file.
    '''

    if not os.path.exists(backup_filename):
        raise Exception(f"Backup file {backup_filename} does not exist.")
    
    shutil.copyfile(backup_filename, db_filename)
    
    print(f"Database {db_filename} restored from {backup_filename}.")


def create_book_table():

    '''This function will create the "book" table and populate it with
    the values below.
    '''
    
    try:
        # Creating table.
        cursor.execute('''CREATE TABLE IF NOT EXISTS book
                          (id INTEGER(4) PRIMARY KEY,
                          title TEXT NOT NULL,
                          authorID INTEGER(4) NOT NULL,
                          qty INTEGER NOT NULL,
                   
                          FOREIGN KEY(authorID) REFERENCES author(id) 
                          ON UPDATE CASCADE)''')
    
        # Values to populate the table with.
        books = [
            (3001, "A Tale of Two Cities", 1290, 30),
            (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
            (3003, "The Lion the Witch and the Wardrobe", 2356, 25),
            (3004, "The Lord of the Rings", 6380, 37),
            (3005, "Alice's Adventures in Wonderland", 5620, 12),
            (3006, "To Kill a Mockingbird", 7265, 32),
            (3007, "The Catcher in the Rye", 6354, 17)
]
    
        # Populating table.
        cursor.executemany('''INSERT IGNORE INTO book 
                              (id, title, authorID, qty)
                              VALUES (?, ?, ?, ?)''', books)
    
        conn.commit()

    except sqlite3.OperationalError:
        conn.rollback()


def create_author_table():

    '''This function will create the "author" table and populate it 
    with the values below.
    '''

    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS author
                          (id INTEGER(4) PRIMARY KEY,
                          name TEXT NOT NULL,
                          country TEXT NOT NULL)''')
    
        authors = [
            (1290, "Charles Dickens", "England"),
            (8937, "J.K. Rowling", "England"),
            (2356, "C.S. Lewis", "Ireland"),
            (6380, "J.R.R. Tolkien", "South Africa"),
            (5620, "Lewis Carroll", "England"),
            (7265, "Harper Lee", "USA"),
            (6354, "J.D. Salinger", "USA")
]
    
        cursor.executemany('''INSERT IGNORE INTO author
                              (id, name, country)
                              VALUES (?, ?, ?)''', authors)
    
        conn.commit()
    
    except sqlite3.OperationalError:
        conn.rollback()


#=======Main Menu=======

def main_menu():

    '''Menu created to carry out the above functions'''
    
    while True:
        try:
            user_choice = int(input(
'''\nHello! Below are the options available to you:
1: Enter book
2: Update book
3: Update author details 
4: Delete book
5: Search books
6: View details of all books
7: Backup database
8: Restore database
9: Exit

Please enter the number of the option you would like to select:\n'''))
        
            if user_choice == 1:
                add_book()

            elif user_choice == 2:
                update_book()

            elif user_choice == 3:
                author_update()

            elif user_choice == 4:
                delete_book()

            elif user_choice == 5:
                search_book()

            elif user_choice == 6:
                view_all()

            elif user_choice == 7:
                backup('ebookstore.db', 'ebookstore_backup.db')

            elif user_choice == 8:
                restore('ebookstore_backup.db', 'ebookstore.db')
        
            elif user_choice == 9:
                print("Goodbye!")
                exit()
        
            else:
                print("Invalid entry! Please try again.")
                continue
        
        except ValueError:
            print("Invalid entry! Please try again.")

# Call table and menu functions.
create_book_table()
create_author_table()
main_menu()

# Close.
conn.close()