import os

if os.path.exists("username.txt") and os.path.exists("password.txt"):

    with open("username.txt", "r") as file:
        stored_username = file.read().strip()

    with open("password.txt", "r") as file:
        stored_password = file.read().strip()

    print(f"Welcome, {stored_username} Please Enter Your Password.")

    password = input("> ")

    if password == stored_password:
        print("Login Successfull!")

    else:
        print("Invalid Password.")

else:
    print("Enter Username")
    username = input("> ")

    print("Great! Now Create A Password")
    password = input("> ")

    with open("username.txt", "w") as file:
        file.write(username)

    with open("password.txt", "w") as file:
        file.write(password)
