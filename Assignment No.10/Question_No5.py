#### Q.5 : Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

def chkPresent():

    numbers = [10, 20, 30, 20, 40, 20, 50]

    num = int(input("Enter a number: "))

    count = 0

    for i in numbers:
        if i == num:
            count = count + 1

    if count > 0:
        print("Element is present in the list")
        print(f'It is present in {count} times.')
    else:
        print("Element is not present in the list")

chkPresent()