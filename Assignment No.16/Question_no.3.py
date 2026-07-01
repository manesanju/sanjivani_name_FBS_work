#### Q.3 : Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:
    # Static Dictionary for Size-wise Price Increase
    size_increment = {
        "small": 0,
        "medium": 10,
        "large": 20,
        "xlarge": 30
    }

    # Constructor (Supports both parameterized and parameterless)
    def __init__(self, sid=0, sname="", stype="", price=0.0, size="small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size.lower()
        print("Shirt Object Created")

    # Destructor
    def __del__(self):
        print("Shirt Object Destroyed")

    # Show Shirt Details
    def showShirt(self):
        print("\n----- Shirt Details -----")
        print("Shirt ID   :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type       :", self.stype)
        print("Size       :", self.size)
        print("Original Price :", self.price)
        print("Final Price    :", self.calculatePrice())

    # Calculate Price According to Size
    def calculatePrice(self):
        increase = Shirt.size_increment.get(self.size, 0)
        final_price = self.price + (self.price * increase / 100)
        return final_price

# Parameterless Constructor
s1 = Shirt()

# Parameterized Constructors
s2 = Shirt(101, "Peter England", "Formal", 1000, "small")
s3 = Shirt(102, "Allen Solly", "Casual", 1000, "medium")
s4 = Shirt(103, "Louis Philippe", "Formal", 1000, "large")
s5 = Shirt(104, "Van Heusen", "Party Wear", 1000, "xlarge")

# Display Details
s1.showShirt()
s2.showShirt()
s3.showShirt()
s4.showShirt()
s5.showShirt()