#### Q.1 : Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Complex:

    # Constructor
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print("Complex Number Object Created")

    # Destructor
    def __del__(self):
        print("Complex Number Object Destroyed")

    # Overloading + Operator
    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return Complex(r, i)

    # Overloading - Operator
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return Complex(r, i)

    # Display Method
    def show(self):
        print(f"{self.real} + {self.imag}i")

# Create Objects
c1 = Complex(5, 3)
c2 = Complex(2, 4)

print("\nFirst Complex Number:")
c1.show()

print("\nSecond Complex Number:")
c2.show()

# Addition
c3 = c1 + c2
print("\nAddition of Complex Numbers:")
c3.show()

# Subtraction
c4 = c1 - c2
print("\nSubtraction of Complex Numbers:")
c4.show()