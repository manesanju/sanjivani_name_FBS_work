#### Q.1 : Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:

# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.

# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.

# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.

# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.

class InvalidOperator(Exception):
    pass


try:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    op = input("Enter Operator (+, -, *, /): ")

    if op == "+":
        print("Result =", num1 + num2)

    elif op == "-":
        print("Result =", num1 - num2)

    elif op == "*":
        print("Result =", num1 * num2)

    elif op == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by Zero is not allowed.")
        print("Result =", num1 / num2)

    else:
        raise InvalidOperator("Invalid Operator!")

except ValueError:
    print("Error: Invalid Number Entered.")

except InvalidOperator as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

except Exception as e:
    print(e)