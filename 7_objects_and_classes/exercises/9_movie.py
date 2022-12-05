class Movie:
    __watched_movies = []

    def __init__(self, name, director, watched=False):
        self.name = name
        self.director = director
        self.watched = watched

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if self.name not in Movie.__watched_movies:
            Movie.__watched_movies.append(self.name)
            self.watched = True

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}." \
               f" Total watched movies: {len(Movie.__watched_movies)}"


first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
