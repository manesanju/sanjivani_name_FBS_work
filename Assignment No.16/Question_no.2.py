#### Q.2 : Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    # Static Member
    discount = 10      # 10% discount

    # Constructor (Supports both parameterized and parameterless)
    def __init__(self, pid=0, pname="", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Product Object Created")

    # Destructor
    def __del__(self):
        print("Product Object Destroyed")

    # Show Product Details
    def showProduct(self):
        print("\n----- Product Details -----")
        print("Product ID   :", self.pid)
        print("Product Name :", self.pname)
        print("Price        :", self.price)
        print("Quantity     :", self.quantity)

    # Apply Discount
    def applyDiscount(self):
        discount_amount = self.price * Product.discount / 100
        final_price = self.price - discount_amount

        print("\n----- Discount Details -----")
        print("Discount (%) :", Product.discount)
        print("Discount Amount :", discount_amount)
        print("Final Price :", final_price)


# Parameterless Constructor
p1 = Product()

# Parameterized Constructor
p2 = Product(101, "Laptop", 60000, 2)

# Display Product Details
p1.showProduct()
p2.showProduct()

# Apply Discount
p2.applyDiscount()