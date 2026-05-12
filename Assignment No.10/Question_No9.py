#### Q.9 : Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers += [num]

even_list = []
odd_list = []

for i in numbers:
    if i % 2 == 0:
        even_list += [i]
    else:
        odd_list += [i]

print(f'Original List is {numbers}.')
print(f'Even List is {even_list}.')
print(f'Odd List is {odd_list}.')