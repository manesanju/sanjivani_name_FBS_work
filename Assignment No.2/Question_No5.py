##### Q.5 : WAP to calculate selling price of book based on cost price and discount.

# Take input
cp = float(input("Enter cost price of book: "))
discount = float(input("Enter discount: "))

# Calculate selling price
sp = cp - discount

# Display result
print(f'The selling price of a book with cost price {cp} and discount {discount} is {sp}.')