from utils import database


USER_CHOICE = """
Enter:
  - 'a' to add a new book
  - 'l' to list all books
  - 'r' to mark a book as read
  - 'd' to delete a book
  - 'q' to quit

Your choice: """


def prompt_add_book():
    book_name = input('Enter the name of the book: ')
    author = input("Enter the name of the author: ")
    database.add_book(book_name, author)


def prompt_list_all_books(): 
    books = database.list_all_books()
    for book in books:
        read = "YES" if book['read'] else "NO"
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_mark_book_as_read():
    book_name = input("What book would you like to mark as read: ")
    database.mark_book_as_read(book_name)


def prompt_delete_book():
    book_name = input("What book would you like to mark as read: ")
    database.delete_book(book_name)



def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE).strip().lower()[0]
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            prompt_list_all_books()
        elif user_input == 'r':
            prompt_mark_book_as_read()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Wrong option, try again...")        
        user_input = input(USER_CHOICE).strip().lower()[0]


menu()
