#### Q.1 : Write a program to calculate the percentage of student based on marks of any 5 subjects.

# Take input for 5 subjects
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))

# Calculate total marks
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculate percentage
percentage = (total / 500) * 100

# Display result
print("Total Marks =", total)
print(f'Percentage of {sub1} & {sub2} & {sub3} & {sub4} & {sub5} is {percentage}.')
