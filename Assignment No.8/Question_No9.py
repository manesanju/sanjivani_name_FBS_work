#### Q.9 : Write a program to check if entered number is a palindrome or not.

def palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
        print(f'The {number} is palindrome.')
    else:
        print(f'The {number} is not palindrome.')

number = int(input('Enter a number: '))
palindrome(number)
