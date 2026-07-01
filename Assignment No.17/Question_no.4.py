#### Q.4 : Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method

# Student Class
class Student:

    # Parameterized Constructor
    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    # Override __str__()
    def __str__(self):
        return (f"ID: {self.studentId}, "
                f"Name: {self.name}, "
                f"Age: {self.age}, "
                f"Percentage: {self.percentage}")


# College Class
class College:

    # Parameterized Constructor
    def __init__(self, noOfStudents):
        self.noOfStudents = noOfStudents
        self.students = []

    # Add Student
    def addStudent(self, student):
        if len(self.students) < self.noOfStudents:
            self.students.append(student)
            print("Student Added Successfully.")
        else:
            print("College is Full.")

    # Get Student by ID
    def getStudent(self, studentId):
        for student in self.students:
            if student.studentId == studentId:
                return student
        return None

    # Remove Student by ID
    def removeStudent(self, studentId):
        for student in self.students:
            if student.studentId == studentId:
                self.students.remove(student)
                print("Student Removed Successfully.")
                return
        print("Student Not Found.")

    # Override __str__()
    def __str__(self):
        result = "\n----- College Students -----\n"
        if len(self.students) == 0:
            result += "No Students Available"
        else:
            for student in self.students:
                result += str(student) + "\n"
        return result

# Create College with Capacity 3
college = College(3)

# Create Student Objects
s1 = Student(101, "Rahul", 20, 85)
s2 = Student(102, "Priya", 21, 90)
s3 = Student(103, "Amit", 22, 75)

# Add Students
college.addStudent(s1)
college.addStudent(s2)
college.addStudent(s3)

# Display College Details
print(college)

# Get Student
student = college.getStudent(102)
if student:
    print("Student Found:")
    print(student)
else:
    print("Student Not Found.")

# Remove Student
college.removeStudent(101)

# Display Updated List
print(college)