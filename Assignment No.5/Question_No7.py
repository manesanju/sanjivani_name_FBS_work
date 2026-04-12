##### Q.7 : Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

print("1. 1! + 2! + ... + n!")
print("2. N + N^2 + ... + N^N")
print("3. Geometric series (ratio 2)")
print("4. a + a^2/2 + ... + a^10/10")
print("5. x - x^2/3 + x^3/5 ...")

choice = int(input("Enter your choice (1-5): "))

# a)
if choice == 1:
    n = int(input("Enter n: "))
    sum = 0
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        sum += fact
    print("Sum =", sum)

# b)
elif choice == 2:
    n = int(input("Enter n: "))
    sum = 0
    for i in range(1, n + 1):
        sum += n ** i
    print("Sum =", sum)

# c)
elif choice == 3:
    n = int(input("Enter n: "))
    sum = 0
    for i in range(n):
        sum += 2 ** i
    print("Sum =", sum)

# d)
elif choice == 4:
    a = int(input("Enter a: "))
    sum = 0
    for i in range(1, 11):
        sum += (a ** i) / i
    print("Sum =", sum)

# e)
elif choice == 5:
    x = int(input("Enter x: "))
    n = int(input("Enter number of terms: "))
    sum = 0
    sign = 1
    den = 1

    for i in range(1, n + 1):
        sum += sign * (x ** i) / den
        sign *= -1
        den += 2

    print("Sum =", sum)

else:
    print("Invalid choice")