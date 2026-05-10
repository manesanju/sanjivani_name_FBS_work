#### Q.9 : Write a program to calculate the m to the power n using recursion.

def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n - 1)

m = int(input("Enter base number (m): "))
n = int(input("Enter power (n): "))
result = power(m, n)
print(m, "to the power", n, "=", result)