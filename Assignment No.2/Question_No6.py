##### Q.6 : WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

# Take input
basic = float(input("Enter basic salary: "))

# Calculate allowances
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

# Total salary
total_salary = basic + da + ta + hra

# Display result
print(f'The total salary with basic {basic} is {total_salary}')