import csv
from item import Item
from phone import Phone


item1 = Item("MyItem", 750)
item1.name = "OtherItem"
print(item1.name)











# phone1 = Phone("Samsung", 900, 8, 1)
# print(phone1.calculate_total_price())

# print(Item.all)
# print(Phone.all)

# Item.instantiate_from_csv()
# print(Item.all)

# for i in Item.all:
#     print(i.name)

# print(Item.all)

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
