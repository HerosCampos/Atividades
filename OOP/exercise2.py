import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, "Price must be higer than or equal to 0"
        assert quantity >= 0, "Quantity must be higer than or equal to 0"

        # Assign to self object 
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity 

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("ex2.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get("name"),
                price = float(item.get("price")),
                quantity = int(item.get("quantity")),
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"



class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity) 
        self.broken_phones = broken_phones

    def __repr__(self):
        return f"Phone({self.name}, {self.price}, {self.quantity}, {self.broken_phones})"


samsung = Phone("Galaxy S9", 2000, 5, 1)
xaomi = Phone("Redmi S12", 1400, 9, 3)
teclado = Item("Teclado Microsoft", 140, 19)
print(Item.all)


#item1 = Item("Phone", 100, 1)
#item2 = Item("Laptop", 1000, 3)
#item3 = Item("Cable", 10, 5)
#item4 = Item("Mouse", 50, 5)
#item5 = Item("Keyboard", 75, 5)

#for i in Item.all:
#    print(i.name)

#print(item1)
#print(Item.all)

#Item.instantiate_from_csv()
#print(Item.all)

#print(Item.is_integer(3.4))
#print(Item.is_integer(3.0))
#print(Item.is_integer(3))




