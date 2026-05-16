#### Q.4 : Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

def generate_dictionary(n):
    dictionary = {}

    for x in range(1, n + 1):
        dictionary[x] = x * x

    return dictionary

num = int(input("Enter the value of n: "))
result = generate_dictionary(num)
print("Generated Dictionary:", result)