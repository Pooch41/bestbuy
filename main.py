import sys

import products
import store
from products import Product


def print_break_line():
    """Prints a pretty break line."""
    print("-" * 5)


def get_enum_list(store_object: store.Store) -> list[tuple[int, Product]]:
    """RECEIVES: Store Object
    Enumerates products from the store,
    RETURNS: Enumerated List of Products."""
    product_list = store_object.get_all_products()
    return list(enumerate(product_list, 1))


def print_item_list(store_object: store.Store):
    """RECEIVES: Store object
    Prints a formatted list of items."""
    product_list = store_object.get_all_products()
    for item in product_list:
        item.show()


def print_all_products_in_store(store_object: store.Store) -> None:
    """RECEIVES: Store object
    Prints formatted output for overview of store."""
    print_break_line()
    print("Items available: \n")
    print_item_list(store_object)
    print_break_line()


def print_total_quantity(store_object: store.Store) -> None:
    """RECEIVES: Store Object
    Prints total count."""
    print_break_line()
    print(f"Total items in store: {store_object.get_total_quantity()}")
    print_break_line()


def make_order(store_object: store.Store) -> None:
    """RECEIVES: Store Object
    Validates user requests for kind and quantity of good to purchase,
    prints out a total via functions in a formatted fashion."""
    print_break_line()
    product_dict = {}
    product_list = get_enum_list(store_object)
    for item in product_list:
        product_dict[str(item[0])] = item[1]
    item_selections = []
    item_quantities = []
    print_item_list(store_object)
    print("\nWhen you want to finish order, enter empty text.")
    while True:
        while True:
            user_input_product = input("Please enter product number: ")
            if user_input_product == "":
                break
            elif user_input_product in product_dict.keys():
                item_selections.append(product_dict[user_input_product])
                break
            else:
                print("Error! Invalid product number!")
                continue
        while True:
            try:
                user_input_quantity = input("Please enter product quantity: ")
                if user_input_product == "":
                    break
                quantity = int(user_input_quantity)
                if quantity > 0:
                    item_quantities.append(quantity)
                    break
                else:
                    print("Error! Enter a whole, positive number.")
            except ValueError:
                print("Error! Enter a whole, positive number.")

        if user_input_product == "" or user_input_quantity == "":
            break
    for item in item_selections:
        if item == "":
            item_selections.remove(item)
    for item in item_quantities:
        if item == "":
            item_quantities.remove(item)
    shopping_list = []
    if len(item_selections) == 0 or len(item_quantities) == 0:
        return
    else:
        for item in item_selections:
            shopping_list.append((item, item_quantities[item_selections.index(item)]))

    total = store_object.order(shopping_list)
    print("*" * 5)
    print(f"\nOrder complete! Your total is: {format(total, '.2f')}$")


def quit_cli(store_object=None) -> None:
    """Exits the program safely."""
    print("Exiting, thanks for shopping!")
    sys.exit(0)


DISPATCH = {
    "1": print_all_products_in_store,
    "2": print_total_quantity,
    "3": make_order,
    "4": quit_cli
}


def start(store_object: store.Store):
    """RECEIVES: Store object
    Displays menu, validates input, dispatches called function."""
    while True:
        print("""
            Store Menu
            ----------
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit
        """)
        user_input = input("\nPlease select an option: ")
        if user_input in DISPATCH.keys():
            DISPATCH[user_input](store_object)
        else:
            print("Please enter one of the numbers, seen next to commands.")


def main() -> None:
    """Sets default product list. Establishes Store Object."""
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == '__main__':
    main()
