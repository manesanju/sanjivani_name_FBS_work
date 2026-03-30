##### Q.4 : Write a program to enter P, T, R and calculate simple Interest.

# Take input for Principle, time, and rate
P = float(input("Enter Principal (P): "))
T = float(input("Enter Time (T in years): "))
R = float(input("Enter Rate (R in %): "))

#Perform Operation
SI = (P * T * R) / 100

# Display result
print(f'The Simple Interest of {P} & {T} & {R} is {SI}.')