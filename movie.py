menu = "\nenter 'a' to add a movie, 'l' to see your movies,'f' to find movie,q to quit "
movies = []


def add_movie():
    title = input("enter movie title")
    director = input("enter name of director")
    year = input("enter the release year of the movie")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })


def show_movie():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"movie name is {movie['title']}")
    print(f"director of movie  is {movie['director']}")
    print(f"movie is released in year {movie['year']}")


def find_movies():
    search_title = input("enter movie of your choice ")

    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)


user_options = {
    "a": add_movie,
    "l": show_movie,
    "f": find_movies
}


def menu_selection():
    selection = input(menu)
    while selection != "q":
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("unknown statement")

        selection = input(menu)


menu_selection()
