class TYMarks:

    def __init__(self, theory=0, practical=0):
        self.theory = theory
        self.practical = practical

    def accept(self):
        self.theory = float(input("Enter TY Theory Marks: "))
        self.practical = float(input("Enter TY Practical Marks: "))

    def display(self):
        print("TY Theory Marks   :", self.theory)
        print("TY Practical Marks:", self.practical)