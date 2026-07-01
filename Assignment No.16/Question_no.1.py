#### Q.1 : Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:
    # Static variable
    count = 0

    # Constructor (Supports both parameterized and parameterless)
    def __init__(self, bid=0, bname="", price=0.0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

        # Increment object count
        Book.count += 1
        print("Book Object Created")

    # Destructor
    def __del__(self):
        print("Book Object Destroyed")

    # ShowBook Method
    def showBook(self):
        print("\n----- Book Details -----")
        print("Book ID   :", self.bid)
        print("Book Name :", self.bname)
        print("Price     :", self.price)
        print("Author    :", self.author)

    # Static Method to Display Object Count
    @staticmethod
    def showCount():
        print("\nTotal Book Objects Created :", Book.count)

# Parameterless Constructor
b1 = Book()

# Parameterized Constructor
b2 = Book(101, "Python Programming", 550, "Guido van Rossum")

# Display Book Details
b1.showBook()
b2.showBook()

# Display Total Objects Created
Book.showCount()