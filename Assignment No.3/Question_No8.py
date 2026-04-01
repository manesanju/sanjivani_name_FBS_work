##### Q.8 : Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)

import random

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

        # Generate 4-digit number
        captcha = random.randint(1000, 9999)
        print("Enter this number:", captcha)

        # Take captcha input
        user_captcha = int(input("Enter the number: "))

        # Check captcha
        if user_captcha == captcha:
            print("Success! CAPTCHA matched")
        else:
            print("Failed! CAPTCHA not matched")

    else:
        print("Wrong Password")

else:
    print("Wrong User ID")