#####Q.8 : Write a program to convert days into years, weeks and days.

# Take input
days = int(input("Enter number of days: "))

# Calculate years, weeks, and remaining days
years = days // 365
print(years)
remaining_days = days % 365
print(remaining_days)

weeks = remaining_days // 7
print(weeks)
days_left = remaining_days % 7
print(days_left)

# Display result
print(f'{days} days = {years} years, {weeks} weeks and {days_left} days.')