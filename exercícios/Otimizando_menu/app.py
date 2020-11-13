import dados

USER_CHOICE = """
Enter:
 [ 1 ] to add a new book
 [ 2 ] to list all books
 [ 3 ] to mark a book as read
 [ 4 ] to delete a book
 [ 5 ] to quit

Your choice: """

def menu():
    dados.create_table()
    while True:
        user_input = input(USER_CHOICE)
        if user_input.isnumeric() == True:
            user_input = int(user_input)
            while user_input != 5:
                if user_input == 1:
                    prompt_add_book()
                elif user_input == 2:
                    list_books()
                elif user_input == 3:
                    prompt_read_book()
                elif user_input == 4:
                    prompt_delete_book()

                elif user_input.isnumeric() == False:
                    print('ERROR! Please, enter a valid number...')

                user_input = input(USER_CHOICE)
                if user_input.isnumeric() == True:
                    user_input = int(user_input)

            if user_input == 5:
                break
        elif user_input.isnumeric() == False:
            print('ERROR! Please, enter a valid number...')
                


def prompt_add_book():
    name = input('Enter the name of the book: ')
    author = input('Enter the author of the book: ')

    dados.add_book(name, author)


def list_books():
    books = dados.get_all_books()
    for book in books:
        print(book)


def prompt_read_book():
    name = input('Enter the name of the book that you have just read: ')

    dados.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of the book that you want to delete: ')

    dados.delete_book(name)




menu()
