#####Q.5 : Write a program to enter P, T, R and calculate Compound Interest.

# Take input for Principle, time, and rate
P = int(input("Enter Principal (P): "))
T = int(input("Enter Time (T in years): "))
R = int(input("Enter Rate (R in %): "))

#Perform Operation
CI = P * ( 1+R/100 ) ** T - P

# Display result
print(f'The Compound Interest of {P} & {T} & {R} is {CI}.')