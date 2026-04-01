##### Q.9 : Input 5 subject marks from user and display grade(eg.First class,Second class ..)

# Take input
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

# Calculate percentage
percentage = (m1 + m2 + m3 + m4 + m5) / 5

# Check grade
if percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 40:
    print("Third Class")
else:
    print("Fail")

# Display percentage
print(f' The percentage is {percentage}%.')