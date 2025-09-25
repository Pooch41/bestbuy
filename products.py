def validate_name(name: str) -> str:
    while True:
        try:
            valid_name = name
            if len(valid_name) < 1:
                raise ValueError
            break
        except ValueError:
            print("Error - Please enter a name (Empty names are not valid)!")
            name = input("Enter a new name: ")
    return valid_name


def validate_price(name: str, price: float) -> float:
    while True:
        try:
            valid_price = round(float(price), 2)
            if valid_price < 0.01:
                raise ValueError
            break
        except ValueError:
            print(f"Error - Please enter a valid {name} price "
                  "(Prices must be a number greater or equal to 0.01)!")
            price = round(float(input("Enter a new price: ")))
    return valid_price


def validate_quantity(name: str, quantity: int) -> int:
    while True:
        try:
            valid_quantity = int(quantity)
            if valid_quantity < 0:
                raise ValueError
            break
        except ValueError:
            print(f"Error - Please enter valid {name} quantity (Quantities must be zero or above.")
            quantity = int(input("Enter a new quantity"))
    return valid_quantity


class Product:
    def __init__(self, name: str, price: float, quantity) -> None:
        self.name = validate_name(name)
        self.price = validate_price(self.name, price)
        self.quantity = validate_quantity(self.name, quantity)
        self.is_activated = True

    def deactivate(self) -> None:
        self.is_activated = False
        print(f"{self.name} has been deactivated.")

    def activate(self) -> None:
        self.is_activated = True
        print(f"{self.name} has been activated.")

    def get_quantity(self) -> int:
        return self.quantity

    def is_active(self) -> bool:
        return self.is_activated

    def set_quantity(self, quantity: int) -> None:
        self.quantity = validate_quantity(self.name, quantity)
        if self.quantity == 0:
            print(f"{self.name} is out of stock!")
            self.deactivate()
        elif not self.is_active and self.quantity > 0:
            self.activate()

    def show(self) -> None:
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        quantity = validate_quantity(self.name, quantity)
        if (self.get_quantity() - quantity) < 0:
            print(f"Insufficient product! {self} name in stock {self.get_quantity()}")
            return None
        else:
            new_quantity = self.get_quantity() - quantity
            self.set_quantity(new_quantity)
            return self.price * quantity
