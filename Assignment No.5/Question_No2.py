##### Q.2 : Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

# while loop
n = int(input("Enter number of students: "))

i = 1
total_percentage = 0

while i <= n:
    print(f"\nEnter marks for Student {i}:")
    
    j = 1
    total = 0
    
    while j <= 5:
        marks = int(input(f"Subject {j}: "))
        total += marks
        j += 1
    
    percentage = total / 5
    total_percentage += percentage
    
    print(f"Percentage of Student {i} = {percentage}%")
    
    i += 1

avg = total_percentage / n
print(f"\nAverage Percentage of all students = {avg}%")


# for loop
n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):
    print(f"\nEnter marks for Student {i}:")
    
    total = 0
    for j in range(1, 6):
        marks = int(input(f"Subject {j}: "))
        total += marks
    
    percentage = total / 5
    total_percentage += percentage
    
    print(f"Percentage of Student {i} = {percentage}%")

avg = total_percentage / n
print(f"\nAverage Percentage of all students = {avg}%")