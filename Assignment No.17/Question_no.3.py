#### Q.3 : Create a class MedicalStudent inherited from Student with following:
# i. Data members :Specialization
# ii. MarksOfInternship
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
class MedicalStudent(Student):

    # Parameterized Constructor
    def __init__(self, studentId=0, name="", age=0, percentage=0.0,
                 specialization="", marksOfInternship=0):
        super().__init__(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    # Accept Method
    def accept(self):
        super().accept()
        self.specialization = input("Enter Specialization: ")
        self.marksOfInternship = int(input("Enter Internship Marks: "))

    # Display Method
    def display(self):
        super().display()
        print("Specialization :", self.specialization)
        print("Internship Marks :", self.marksOfInternship)
        print("Rank :", self.calculateRank())

    # Override CalculateRank
    def calculateRank(self):
        total = (self.percentage + self.marksOfInternship) / 2

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
                f"Specialization : {self.specialization}\n"
                f"Internship Marks : {self.marksOfInternship}\n"
                f"Rank : {self.calculateRank()}")

# Parameterized Constructor
m1 = MedicalStudent(201, "Priya", 22, 88, "Cardiology", 95)

print("Medical Student Details (__str__)")
print(m1)

print("\n--------------------------------")

# Accept User Input
m2 = MedicalStudent()
m2.accept()

print("\nMedical Student Details (display)")
m2.display()