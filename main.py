email = input("Enter your email = ")
check = email.endswith("@gmail.com", -10)
if check:
    print("Valid Email.\n")
else:
    print("Oops! Invalid Email Address.\nYour email address should end with @gmail.com\n")