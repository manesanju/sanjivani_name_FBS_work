##### Q.2 : Write a program to input any alphabet and check whether it is vowel or consonant.

# Take input
ch = input("Enter an alphabet: ")

# Check condition
if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print(f'It is a Vowel {ch}.')
else:
    print(f'It is a Consonant {ch}.')