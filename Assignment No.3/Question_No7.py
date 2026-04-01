##### Q.7 : Write a program to check if user has entered correct userid and password.

# Correct credentials
correct_userid = "admin"
correct_password = "1234"

# Take input
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Check User ID
if userid == correct_userid:
    
    # Check Password
    if password == correct_password:
        print("Login Successful")
    else:
        print("Wrong Password")

else:
    print("Wrong User ID")