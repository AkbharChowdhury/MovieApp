from classes.db import Database
from classes.movie import Movie
from classes.movie_genres import MovieGenres

db = Database()
movie_genre = MovieGenres(title='',
                          genre=MovieGenres.default_genre(),
                          movie_list=Movie.movie_list(db.show_movie_list2()))

movie_genre.genre='Children'
# for r in movie_genre.movie_list:
#     print(r.genre, r.title)
print(movie_genre.filter_list())
# print(movie_genre.movie_list)

exit(0)


def filter_list(
        products,
        name_contains=None,
        min_price=None,
        max_price=None,
        product_categories=None,
):
    filters = []
    if name_contains:
        filters.append(lambda p: name_contains.casefold() in p["name"].casefold())
    if min_price:
        filters.append(lambda p: p["price"] >= min_price)
    if max_price:
        filters.append(lambda p: p["price"] <= max_price)
    if product_categories:
        filters.append(lambda p: p["category"] in product_categories)
    try:
        return list((filter(lambda p: all(f(p) for f in filters), products)))

        # return next(filter(lambda p: all(f(p) for f in filters), products))
    except StopIteration:
        return None


products = [
    {"name": "Race car", "category": "Toys", "price": 120},
    {"name": "T-shirt", "category": "Clothing", "price": 20},
    {"name": "Tricycle", "category": "Toys", "price": 240},
    {"name": "LED bulb", "category": "Home", "price": 13},
    {"name": "Jeans", "category": "Clothing", "price": 80},
    {"name": "Jacket", "category": "Clothing", "price": 130},

]
items = []

products.append({"name": "Shoes", "category": "Clothing", "price": 80})
# print(get_first_match(products))
for item in filter_list(products, product_categories='Clothing'):
    print(item)
