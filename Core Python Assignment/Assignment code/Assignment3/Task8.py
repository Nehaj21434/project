# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
user_id = "Neha"
password = "Neha2110"

# Step 1: Take inputs
u = input("Enter user ID: ")
p = input("Enter password: ")

# Step 2: Verify ID and password
if u == user_id and p == password:
    captcha = (len(user_id) * len(password) * 1234) % 10000
    print("Captcha:", captcha)

    # Step 3: Take captcha input (convert to int)
    user_captcha = int(input("Enter the captcha: "))

    # Step 4: Verify captcha
    if user_captcha == captcha:
        print("Login successful ✅")
    else:
        print("Login failed ❌")
else:
    print("Invalid User ID or Password ❌")
