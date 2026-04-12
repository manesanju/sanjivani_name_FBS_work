##### Q.2 : WAP to print all odd number until n

# while loop
num = int(input('Enter a number: '))

i = 1
while i <= num:
    print(i)
    i += 2

# for loop
num = int(input('Enter a number:'))
for i in range(1, num+1, 2):
    print(i)
