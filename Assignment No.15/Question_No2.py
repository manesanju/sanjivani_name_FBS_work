#### Q.2 : Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:

    # Constructor
    def __init__(self, pid=0, pname="None", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    # Method to show product details
    def ShowBook(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    # Destructor
    def __del__(self):
        print("Product object destroyed")


# Creating object
p1 = Product(101, "Laptop", 50000, 2)

# Calling method
p1.ShowBook()