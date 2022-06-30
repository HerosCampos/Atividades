movies = list()


def add_movie():
    title = input("Enter the movie title: ")
    author = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'author': author,
        'year': year
    })


def show_movies():
    for m in movies:
        print(m['title'])


def find_movie():
    find_movie = input('Enter a movie you want to find: ')

    for m in movies:
        if find_movie.lower() == m['title'].lower():
            print('movie found')


user_option = {
    'a': add_movie,
    'l': show_movies,
    'f': find_movie
}


def menu():
    selection = input(f"SELECT AN OPTION:\nA - to add a movie\nL - to list the movies\nF - to find a movie\n  - Option: ")
    while selection.lower() != 'q':
        if selection in user_option:
            selected_function = user_option[selection] # this is called first class functions
            selected_function() # this is called first class functions
        else:
            print("Unknown command. Please try again.")

        selection = input(f"SELECT AN OPTION:\nA - to add a movie\nL - to list the movies\nF - to find a movie\n  - Option: ")


menu()

