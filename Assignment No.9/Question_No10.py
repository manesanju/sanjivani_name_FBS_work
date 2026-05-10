#### Q.10 : Write a program to reverse a number using recursion.

def reverse(n, rev=0):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit
    return reverse(n // 10, rev)

num = int(input("Enter a number: "))
result = reverse(num)
print(f'The reversed number of {num} -> {result}.')