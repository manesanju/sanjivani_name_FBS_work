#### Q.3 : Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

# Custom Range Generator

def myRange(start, stop, step):
    while start < stop:
        yield start
        start += step


# Main Program
start = int(input("Enter Start: "))
stop = int(input("Enter Stop: "))
step = int(input("Enter Step: "))

print("Generated Numbers:")

for num in myRange(start, stop, step):
    print(num, end=" ")