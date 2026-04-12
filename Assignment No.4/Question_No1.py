##### Q.1 : WAP to print all even number until n

# while loop
num = int(input('Enter a number: '))

i = 2
while i <= num:
    print(i)
    i += 2


# for loop
num = int(input('Enter a number:'))
for i in range(2, num+1, 2):
    print(i)

