# Write a program to prompt user to enter userid and password.
#  If Id and password is incorrect give him chance to re-enter the credentials.
#  Let him try 3 times.
# After that program to terminate.


# correct userid and password first enter
correct_userid = "Neha"
correct_password = "Neha1234"

# 3 attempt to enter tha id and password.
for attempt in range(1, 4):  # loop runs 3 times.
    user_id = input("Enter the User Id: ")
    password = input("Enter the password: ")

    if user_id == correct_userid and password == correct_password:
        print("Login successful")
        break
    else:
        print("Invalid Usre Id or password")
        print("Attempt left:", 3 - attempt)
else:
    print("To many falide attempt. praogram terminate")
