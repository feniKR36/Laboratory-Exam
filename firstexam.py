class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def update_quantity(self, quantity):
        self.quantity += quantity
    def get_total_price(self):
        return self.quantity * self.price
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, name, quantity, price):
        self.item = input("Enter item: ")
        self.quantity = int(input("Enter quantity: "))
        self.price = float(input("Enter price: "))
        for item in self.items:
            if item.name() == name():
                item.update_quantity(quantity)
                return
        new_item = Item(name, quantity, price)
        self.items.append(new_item)
    def update_quantity(self, name, quantity):
        for item in self.items:
            if item.name() == name():
                item.update_quantity(quantity)
                return
        print("Item not found")
    def display_items(self):
        print("\nInventory Items:")
        for item in self.items:
            print(f"Name: {item.name}")
            print(f"Quantity: {item.quantity}")
            print(f"Price: {item.price}")
            print(f"Total Price: {item.get_total_price()}")
            print("-" * 30)
    def calculate_total_inventory_value(self):
        total_value = 0
        for item in self.items:
            total_value += item.get_total_price()
        return total_value
