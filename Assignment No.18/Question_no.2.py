#### Q.2 : Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:

    # Constructor
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        print("Distance Object Created")

    # Destructor
    def __del__(self):
        print("Distance Object Destroyed")

    # Overloading + Operator
    def __add__(self, other):
        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm

        # Normalize the values
        if cm >= 100:
            m += cm // 100
            cm = cm % 100

        if m >= 1000:
            km += m // 1000
            m = m % 1000

        return Distance(km, m, cm)

    # Overloading - Operator
    def __sub__(self, other):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = other.km * 100000 + other.m * 100 + other.cm

        diff = total1 - total2

        km = diff // 100000
        rem = diff % 100000

        m = rem // 100
        cm = rem % 100

        return Distance(km, m, cm)

    # Display Method
    def show(self):
        print(f"{self.km} km {self.m} m {self.cm} cm")

d1 = Distance(2, 500, 80)
d2 = Distance(1, 700, 50)

print("\nFirst Distance:")
d1.show()

print("\nSecond Distance:")
d2.show()

# Addition
d3 = d1 + d2
print("\nAddition of Distances:")
d3.show()

# Subtraction
d4 = d1 - d2
print("\nSubtraction of Distances:")
d4.show()