#### Q.7 : Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.

numbers = [num for num in range(1, 1001)
           if any(num % i == 0 for i in range(2, 10))]

print(numbers)