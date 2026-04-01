##### Q.6 : Write a program to calculate profit or loss.

# Take input
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

# Check profit or loss
if sp > cp:
    profit = sp - cp
    print(f'The Profit is {profit}.')
elif cp > sp:
    loss = cp - sp
    print(f'The Loss is {loss}.')
else:
    print('No Profit No Loss')