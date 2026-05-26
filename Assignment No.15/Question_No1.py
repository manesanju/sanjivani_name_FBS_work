#### Q.1 : Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:

    # Constructor
    def __init__(self, bid=0, bname="None", price=0, author="None"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    # Method to show book details
    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    # Destructor
    def __del__(self):
        print("Book object destroyed")


# Creating object
b1 = Book(101, "Python", 500, "ABC")

# Calling method
b1.ShowBook()