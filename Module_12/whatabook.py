import mysql.connector


config = {
    "user": "whatabook_user",
    "password": "R45fhIps45",
    "host": "localhost",
    "database": "whatabook",
}



def show_menu():
    print("Main Menu")

    print("1. View Books    2. View Store Locations    3. My Account    4. Exit Program")

    try:
        choice = int(input('<enter: 1 for book>: '))

        return choice
    except ValueError:
        
        
        print("Invalid Entry")

        

def show_books(cursor):
     
    cursor.execute("SELECT book_id, book_name, author, details from book")

    books = cursor.fetchall()

    print("BOOKS")

    
    for book in books:
        print("Book Name: {}  Author: {}  Details: {}".format(book[0], book[1], book[2]))

def show_locations(cursor):
    cursor.execute("SELECT store_id, locale from store")

    locations = cursor.fetchall()

    print("LOCATIONS")

    for location in locations:
        print("Locale: {}".format(location[1]))

def validate_user():
    
    user_id = int(input('Enter a customer id <Example 1 for user_id 1>: '))

    if user_id < 0 or user_id > 3:


            print("Invalid customer")
            


def show_account_menu():
    

    
        print("Customer Menu")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <Example enter: 1 for wishlist>: '))

        return account_option


print("Incorrect")

    

def show_wishlist(cursor, _user_id):
   

    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist = cursor.fetchall()

    print("Wishlist")

    for book in wishlist:
        print("        Book Name: {}        Author: {}".format(book[4], book[5]))

def show_books_to_add(cursor, _user_id):
    

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    cursor.execute(query)

    books_to_add = cursor.fetchall()

    print("Available Books")

    for book in books_to_add:
        print("        Book Id: {}        Book Name: {}".format(book[0], book[1]))

def add_book_to_wishlist(cursor, _user_id, _book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))



    db = mysql.connector.connect(**config) 

    cursor = db.cursor() 

    print("Welcome")

    user_selection = show_menu() 

    
    while user_selection != 4:

        
        if user_selection == 1:
            show_books(cursor)

        
        if user_selection == 2:
            show_locations(cursor)

        
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

           
            while account_option != 3:

               
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                
                if account_option == 2:

                    
                    show_books_to_add(cursor, my_user_id)

                   
                    book_id = int(input("Enter the id of the book you want to add: "))

                    
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() 

                    print("Book id: {} was added to your wishlist!".format(book_id))

                 
                if account_option < 0 or account_option > 3:
                    print("Incorrect")

                
                account_option = show_account_menu()

        
        if user_selection < 0 or user_selection > 4:
            print("Incorrect")

        
        user_selection = show_menu()

    print("Ended")



    
print("Invalid Username or Password")





     

