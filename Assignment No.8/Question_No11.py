#### Q.11 : WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

# Function to count digits
def count_digits(num):
    count = 0
    temp = num
    while temp > 0:
        count = count + 1
        temp = temp // 10

    return count

# Function to check Armstrong number
def armstrong(num):
    digits = count_digits(num)
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10
    if total == num:
        print(f'The {number} is Armstrong number.')
    else:
        print(f'The {number} is not an Armstrong number.')

number = int(input("Enter a number: "))
armstrong(number)