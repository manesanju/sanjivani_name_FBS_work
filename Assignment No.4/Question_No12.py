##### Q.12 : Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

# while loop
num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# for loop
num = int(input("Enter a number: "))

digits = len(str(num))
sum = 0

for i in str(num):
    digit = int(i)
    sum += digit ** digits

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")