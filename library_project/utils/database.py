

books = []

def add_book(name, author):
    books.append({"name": name, "author": author, "read": False})


def list_all_books():
    for book in books:
        print(book)

def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True

def delete_book(name):
    global books 
    books = [book for book in books if book['name'] != name] 
