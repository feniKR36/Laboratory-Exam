class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print("\nBorrowed successfully. Please return it in the alloted time.")
        else:
            print("\nBook unavailable")

    def return_book(self):
        if not self.available:
            self.available = True
            print("\nBook returned.")
        else:
            print("\nBook available")

    def is_available(self):
        if self.available:
            return "Available"
        else:
            return "Not Available"
    def display_info(self):
        print("\nBook Information")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.year)
        print("Status:", self.is_available())
title = input("Enter book title: ")
author = input("Enter author name: ")
year = input("Enter publication year: ")
book1 = Book(title, author, year)
print("\nChoose an option:")
print("1 - Borrow Book")
print("2 - Return Book")
print("3 - Display Book Information")
choice = input("Enter your choice (1-3): ")

if choice == "1":
    book1.borrow_book()
elif choice == "2":
    book1.return_book()
elif choice == "3":
    book1.display_info()
else:
    print("\nInvalid choice.")
