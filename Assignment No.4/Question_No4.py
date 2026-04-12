##### Q.4 : WAP to print factorial of a number .

## while loop
n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i += 1

print(f"Factorial of {n} is {fact}.")


## for loop
# Input from user
n = int(input('Enter a number:'))

fact = 1

# Using for loop
for i in range(1, n + 1):
    fact = fact * i

# Output
print(f'Factorial of {n} is {fact}.')