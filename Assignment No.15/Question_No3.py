#### Q.3 : Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:

    # Constructor
    def __init__(self, sid=0, sname="None", type="None", price=0, size="None"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    # Method to show shirt details
    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)

    # Destructor
    def __del__(self):
        print("Shirt object destroyed")


# Creating object
s1 = Shirt(1, "Cotton Shirt", "Formal", 1200, "Large")

# Calling method
s1.ShowBook()