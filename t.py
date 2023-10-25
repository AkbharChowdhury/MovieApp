def get_first_match(
        products,
        name_contains=None,
        min_price=None,
        max_price=None,
        product_categories=None,
):
    filters = []
    if name_contains:
        filters.append(lambda p: name_contains in p["name"])
    if min_price:
        filters.append(lambda p: p["price"] >= min_price)
    if max_price:
        filters.append(lambda p: p["price"] <= max_price)
    if product_categories:
        filters.append(lambda p: p["category"] in product_categories)
    try:
        # return next(filter(lambda p: all(f(p) for f in filters), products))
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
]
# print(get_first_match(products))
print(get_first_match(products, min_price=120))
