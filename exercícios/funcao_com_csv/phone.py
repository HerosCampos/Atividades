import csv
from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones