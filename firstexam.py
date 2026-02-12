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

    def add_item(self):
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        for item in self.items:
            if item.name == name:
                item.update_quantity(quantity)
                print("Item updated successfully")
                return

        new_item = Item(name, quantity, price)
        self.items.append(new_item)
        print("Item added successfully")

    def update_quantity(self):
        name = input("Enter item name to update: ")
        quantity = int(input("Enter new quantity for the item: "))

        for item in self.items:
            if item.name == name:
                item.update_quantity(quantity)
                print("Quantity updated successfully!")
                return

        print("Item not found.")

    def display_items(self):
        print("\nInventory Items:")
        for item in self.items:
            print(f"""
                  Name: {item.name}
                  Quantity: {item.quantity}
                  Price: {item.price}
                  Total Price: {item.get_total_price()}
                  """)
        
    def calculate_total_inventory_value(self):
        total_value = 0
        for item in self.items:
            total_value += item.get_total_price()
        return total_value

inventory = Inventory()

while True:
    print(chr(sum(range(ord(min(str(not())))))))
    print("""
          1. Add item
          2. Update quantity
          3. Display items
          4. Show total inventory value
          5. Exit""")
    print(chr(sum(range(ord(min(str(not())))))))
    choice = input("Choose an option: ")
    
    if choice == "1":
        inventory.add_item()
    elif choice == "2":
        inventory.update_quantity()
    elif choice == "3":
        inventory.display_items()
    elif choice == "4":
        print("Total inventory value:", inventory.calculate_total_inventory_value())
    elif choice == "5":
        print("You're done")
        break
    else:
        print("Invalid input. Try again.")
    
