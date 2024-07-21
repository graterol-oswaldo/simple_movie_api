from schemas.movie import Movie
from random import choices
from string import ascii_letters, digits


data: list[dict] = [
    {
        "id": 1,
        "title": "Inception",
        "overview": "A skilled thief is given a chance to erase his criminal record by infiltrating dreams and planting an idea into the target's subconscious.",
        "year": 2010,
        "rating": 7.2,
        "category": "Science Fiction"
    },
    {
        "id": 2,
        "title": "The Shawshank Redemption",
        "overview": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "year": 1994,
        "rating": 9.8,
        "category": "Drama"
    },
     {
        "id": 3,
        "title": "The Godfather",
        "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "year": 1972,
        "rating": 9.5,
        "category": "Crime"
    }   
]


movies: list[dict] = [Movie(**item).model_dump() for item in data]


def generate_random_string(lenght: int) -> str:
    characters: str = ascii_letters + digits
    return ''.join(choices(characters, k=lenght))
