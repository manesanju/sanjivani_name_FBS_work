##### Q.11 : Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total = 0

for i in range(5):
    age = int(input("Enter age: "))
    amount = float(input("Enter ticket amount: "))

    if age < 12:
        amount = amount - (0.30 * amount)   # 30% discount
    elif age > 59:
        amount = amount - (0.50 * amount)   # 50% discount

    total = total + amount

print(f'Total Ticket Amount is {total}.')