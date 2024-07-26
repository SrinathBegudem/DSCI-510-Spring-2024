# Lab 6
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
class Vehicle:
    def __init__(self, vehicle_id, make, model, year):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Vehicle(vehicle_id='{self.vehicle_id}', make='{self.make}', model='{self.model}', year={self.year})"

    def __repr__(self):
        return self.__str__()

# invoke the function with relevant args of your choice
car = Vehicle("VIN123", "Toyota", "Camry", 2020)
print(car)



# ----------------- Question 2 -----------------
class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def add_book(self, book_title):
        self.borrowed_books.append(book_title)

    def remove_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)

    def count_books(self):
        return len(self.borrowed_books)

    def __str__(self):
        return f"LibraryMember(member_id='{self.member_id}', name='{self.name}', total_borrowed={self.count_books()})"

    def __repr__(self):
        return self.__str__()

# invoke the function with relevant args of your choice
member = LibraryMember("001", "Alice")
member.add_book("The Great Gatsby")
print(member)



# ----------------- Question 3 -----------------
class Product:
    def __init__(self, product_code, name, price, quantity_available):
        self.product_code = product_code
        self.name = name
        self.price = price
        self.quantity_available = quantity_available

    def update_price(self, new_price):
        self.price = new_price

    def add_stock(self, quantity):
        self.quantity_available += quantity

    def sell_product(self, quantity):
        if self.quantity_available >= quantity:
            self.quantity_available -= quantity
        else:
            print("Not enough stock to complete the sale")

    def __str__(self):
        return f"Product(product_code='{self.product_code}', name='{self.name}', price={self.price}, quantity_available={self.quantity_available})"

    def __repr__(self):
        return self.__str__()

# invoke the function with relevant args of your choice
product = Product("12345", "Coffee Mug", 12.99, 100)
product.sell_product(2)
print(product)

