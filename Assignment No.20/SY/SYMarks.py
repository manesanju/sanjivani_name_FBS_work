#### Q.1 : Write a program to
# 1. create a package “SY” which has class SYMARKS (Computer Total,
# MathsTotal, ElectronicsTotal).

# 2. Create another package “TY” which has a class TYMarks (Theory,
# Practical).

# 3. Create object of student class (Outside SY & TY package) having roll
# number, name, SYMakrs and TYMarks. Add the marksof SY and TY
# Computer subjects and calculate grade ("A" for >=70, "B" for >=60,
# "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result
# of the student in proper format.

class SYMarks:

    def __init__(self, computer=0, maths=0, electronics=0):
        self.computer = computer
        self.maths = maths
        self.electronics = electronics

    def accept(self):
        self.computer = float(input("Enter SY Computer Marks: "))
        self.maths = float(input("Enter SY Maths Marks: "))
        self.electronics = float(input("Enter SY Electronics Marks: "))

    def display(self):
        print("SY Computer Marks   :", self.computer)
        print("SY Maths Marks      :", self.maths)
        print("SY Electronics Marks:", self.electronics)