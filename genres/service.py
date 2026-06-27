from genres.repository import GenreRepository

class GenreService:
    
    def __init__(self):
        self.genre_repository = GenreRepository()

    def get_genres(self):
        return self.genre_repository.get_genres()
    
    def get_genres_name(self):
        genres = self.genre_repository.get_genres() or []
        genre_names = list()
        for genre in genres:
            genre_names.append(genre.get('name'))
        return genre_names
    
    def create_genre(self, name):
        genre = dict(
            name=name,
        )
        return self.genre_repository.create_genre(genre)