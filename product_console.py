""""""

import json

from product import Product

FILENAME = "products.json"


def main():
    """Program for displaying products name and price from file."""
    products = load_products()
    for product in products:
        print(product)


def load_products():
    """Load products from json file."""
    products = []
    with open(FILENAME) as in_file:
        records = json.load(in_file)
        # print(repr(records))
    for record in records:
        products.append(Product(**record))
    return products


if __name__ == '__main__':
    main()
