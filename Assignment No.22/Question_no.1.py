#### Q.1 : Create a class Emp (eid,ename,basic)
# WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.

import pickle

# Employee Class
class Emp:
    def __init__(self, eid=0, ename="", basic=0):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def accept(self):
        self.eid = int(input("Enter Employee ID: "))
        self.ename = input("Enter Employee Name: ")
        self.basic = float(input("Enter Basic Salary: "))

    def display(self):
        print("ID :", self.eid)
        print("Name :", self.ename)
        print("Basic Salary :", self.basic)
        print("-------------------------")

filename = "emp.dat"

while True:

    print("\n1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    ch = int(input("Enter Choice: "))

    # Add Record
    if ch == 1:
        emp = Emp()
        emp.accept()

        f = open(filename, "ab")
        pickle.dump(emp, f)
        f.close()

        print("Record Added.")

    # Search Record
    elif ch == 2:
        eid = int(input("Enter Employee ID: "))
        found = False

        try:
            f = open(filename, "rb")
            while True:
                emp = pickle.load(f)
                if emp.eid == eid:
                    emp.display()
                    found = True
        except EOFError:
            f.close()

        if not found:
            print("Record Not Found.")

    # Delete Record
    elif ch == 3:
        eid = int(input("Enter Employee ID: "))

        f = open(filename, "rb")
        temp = open("temp.dat", "wb")

        try:
            while True:
                emp = pickle.load(f)
                if emp.eid != eid:
                    pickle.dump(emp, temp)
        except EOFError:
            pass

        f.close()
        temp.close()

        import os
        os.remove(filename)
        os.rename("temp.dat", filename)

        print("Record Deleted.")

    # Edit Record
    elif ch == 4:
        eid = int(input("Enter Employee ID: "))

        f = open(filename, "rb")
        temp = open("temp.dat", "wb")

        try:
            while True:
                emp = pickle.load(f)

                if emp.eid == eid:
                    print("Enter New Details")
                    emp.accept()

                pickle.dump(emp, temp)

        except EOFError:
            pass

        f.close()
        temp.close()

        import os
        os.remove(filename)
        os.rename("temp.dat", filename)

        print("Record Updated.")

    # Display Records
    elif ch == 5:
        try:
            f = open(filename, "rb")

            while True:
                emp = pickle.load(f)
                emp.display()

        except EOFError:
            f.close()

    # Exit
    elif ch == 6:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")