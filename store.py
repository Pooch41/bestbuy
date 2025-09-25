import products

def validate_inventory(product, inventory):
    while True:
        if product in inventory:
            return product
        else:
            print("No product in inventory found. Products in inventory: ")
            for item in inventory:
                print(f"Type '{item}' for '{item.name}'")
            product = input("Enter desired product: ")

class Store:
    def __init__(self, list_of_products: list) -> None:
        self.inventory = list_of_products

    def add_product(self, new_product: products.Product) -> None:
        self.inventory.append(new_product)


    def remove_product(self, product_to_remove: products.Product) -> None:
        product_to_remove = validate_inventory(product_to_remove)
        self.inventory.remove(product_to_remove)

    def get_total_quantity(self) -> int:
        return sum(product.quantity for product in self.inventory)

    def get_all_products(self) -> list[products.Product]:
        return [product for product in self.inventory if product.is_active()]

    def order(self, shopping_list: list[tuple[products.Product, int]]) -> float:
        total = 0
        for item in shopping_list:
            product = validate_inventory(item[0], self.inventory)
            to_buy = product.buy(item[1])
            if to_buy is not None:
                total += to_buy
            else:
                print(f"{product.name} is out of stock! Skipping. Please contact staff "
                      f"for more information. We apologise for the inconvenience.")
        return total