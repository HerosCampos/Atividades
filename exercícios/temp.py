class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0 , f"Price {price} is not greater or equal than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

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

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 75, 5)
item5 = Item("Keyboard", 75, 5)

for i in Item.all:
    print(i.name)


print(Item.all)







# print("-" * 50)

# print("Applying 30% of discount")
# bbb = Item("bbb", 10, 3)
# bbb.pay_rate = 0.7
# bbb.apply_discount()
# print(bbb.price)
# print(bbb.calculate_total_price())

# print("-" * 50)

# print("Applying 20% of discount")
# ccc = Item("bbb", 10, 3)
# ccc.apply_discount()
# print(ccc.price)
# print(ccc.calculate_total_price())
