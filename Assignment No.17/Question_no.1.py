#### Q.1 : Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method

class Student:

    # Parameterized Constructor
    def __init__(self, studentId=0, name="", age=0, percentage=0.0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    # Accept Method
    def accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Student Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    # Display Method
    def display(self):
        print("\n----- Student Details -----")
        print("Student ID :", self.studentId)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Percentage :", self.percentage)

    # Calculate Rank Method
    def calculateRank(self):
        if self.percentage >= 90:
            return "Rank A"
        elif self.percentage >= 75:
            return "Rank B"
        elif self.percentage >= 60:
            return "Rank C"
        elif self.percentage >= 40:
            return "Rank D"
        else:
            return "Fail"

    # Override __str__ Method
    def __str__(self):
        return (f"Student ID: {self.studentId}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Percentage: {self.percentage}\n"
                f"Rank: {self.calculateRank()}")

# Create object using parameterized constructor
s1 = Student(101, "Sanjivani", 20, 88.5)

print("Student Details using __str__():")
print(s1)

# Create another object and accept details from user
s2 = Student()
s2.accept()

print("\nStudent Details using display():")
s2.display()

print("Rank :", s2.calculateRank())