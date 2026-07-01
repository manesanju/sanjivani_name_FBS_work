#### Q.2 : Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method

# Base Class
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

    # Calculate Rank
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

    # Override __str__
    def __str__(self):
        return (f"Student ID : {self.studentId}\n"
                f"Name : {self.name}\n"
                f"Age : {self.age}\n"
                f"Percentage : {self.percentage}\n"
                f"Rank : {self.calculateRank()}")


# Derived Class
class EnggStudent(Student):

    # Parameterized Constructor
    def __init__(self, studentId=0, name="", age=0, percentage=0.0,
                 branch="", internalMarks=0):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    # Accept Method
    def accept(self):
        super().accept()
        self.branch = input("Enter Branch: ")
        self.internalMarks = int(input("Enter Internal Marks: "))

    # Display Method
    def display(self):
        super().display()
        print("Branch :", self.branch)
        print("Internal Marks :", self.internalMarks)
        print("Rank :", self.calculateRank())

    # Override CalculateRank
    def calculateRank(self):
        total = (self.percentage + self.internalMarks) / 2

        if total >= 90:
            return "Rank A"
        elif total >= 75:
            return "Rank B"
        elif total >= 60:
            return "Rank C"
        elif total >= 40:
            return "Rank D"
        else:
            return "Fail"

    # Override __str__
    def __str__(self):
        return (f"Student ID : {self.studentId}\n"
                f"Name : {self.name}\n"
                f"Age : {self.age}\n"
                f"Percentage : {self.percentage}\n"
                f"Branch : {self.branch}\n"
                f"Internal Marks : {self.internalMarks}\n"
                f"Rank : {self.calculateRank()}")

# Parameterized Constructor
e1 = EnggStudent(101, "Sanjivani", 20, 85, "Computer", 92)

print("Engineering Student Details (__str__)")
print(e1)

print("\n--------------------------------")

# Accept User Input
e2 = EnggStudent()
e2.accept()

print("\nEngineering Student Details (display)")
e2.display()