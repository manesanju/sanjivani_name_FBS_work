from SY.SYMarks import SYMarks
from TY.TYMarks import TYMarks


class Student:

    def __init__(self, rollNo=0, name=""):
        self.rollNo = rollNo
        self.name = name

        # Containment
        self.sy = SYMarks()
        self.ty = TYMarks()

    def accept(self):
        self.rollNo = int(input("Enter Roll Number: "))
        self.name = input("Enter Name: ")

        self.sy.accept()
        self.ty.accept()

    def calculateGrade(self):

        # Average of SY Computer and TY Theory
        total = (self.sy.computer + self.ty.theory) / 2

        if total >= 70:
            grade = "A"
        elif total >= 60:
            grade = "B"
        elif total >= 50:
            grade = "C"
        elif total >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        return total, grade

    def display(self):

        total, grade = self.calculateGrade()

        print("\n----------- STUDENT RESULT -----------")
        print("Roll Number :", self.rollNo)
        print("Name        :", self.name)

        self.sy.display()
        self.ty.display()

        print("--------------------------------------")
        print("Average Marks :", total)
        print("Grade         :", grade)


# Main Program

s = Student()

s.accept()

s.display()