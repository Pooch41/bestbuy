def validate_name(name: str) -> str:
    """Validates that name is not empty."""
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
    """Validates that price is not zero or under."""
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
    """Validates that quantity is not below zero."""
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
        """Sets object as inactive."""
        self.is_activated = False
        print(f"{self.name} has been deactivated.")

    def activate(self) -> None:
        """Sets object as active."""
        self.is_activated = True
        print(f"{self.name} has been activated.")

    def get_quantity(self) -> int:
        """Gets quantity of object."""
        return self.quantity

    def is_active(self) -> bool:
        """Gets activity status of object."""
        return self.is_activated

    def set_quantity(self, quantity: int) -> None:
        """RECEIVES: Quantity
        Sets the difference between quantity currently, minus quantity provided.
        Disables if quantity 0. Does not go below 0."""
        self.quantity = validate_quantity(self.name, quantity)
        if self.quantity == 0:
            print(f"{self.name} is out of stock!")
            self.deactivate()
        elif not self.is_active and self.quantity > 0:
            self.activate()

    def show(self) -> None:
        """Prints status."""
        print(f"\t-> {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """RECEIVES: Quantity
        Subtracts quantity from total,
        RETURNS: price of purchase."""
        quantity = validate_quantity(self.name, quantity)
        if (self.get_quantity() - quantity) < 0:
            print(f"Insufficient product! {self} name in stock {self.get_quantity()}")
            return None
        else:
            new_quantity = self.get_quantity() - quantity
            self.set_quantity(new_quantity)
            return self.price * quantity
