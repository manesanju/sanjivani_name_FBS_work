#### Q.10 : Write a program to check if entered year is a leap year or not.

def leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f'The {year} is leap year.')
    else:
        print(f'The {year} is not a leap year.')

year = int(input("Enter year: "))
leap_year(year)