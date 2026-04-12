##### Q.1 : Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

# while loop
correct_id = "admin"
correct_pass = "1234"

attempts = 0

while attempts < 3:
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_pass:
        print("Login Successful")
        break
    else:
        print("Incorrect ID or Password")
        attempts += 1

if attempts == 3:
    print("Too many attempts! Program terminated.")

# for loop
correct_id = "admin"
correct_pass = "1234"

for i in range(3):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_pass:
        print("Login Successful")
        break
    else:
        print("Incorrect ID or Password")

else:
    print("Too many attempts! Program terminated.")