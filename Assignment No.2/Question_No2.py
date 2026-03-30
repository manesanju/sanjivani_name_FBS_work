##### Q.2 : Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

# Take input
c = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
f = (c * 9/5) + 32        #rearranged to C/5=(F−32)/9

# Display result
print(f'The temperature of {c}°C in Fahrenheit is {f}°F.')