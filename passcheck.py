import os

# Prompt user to create a new password
password = input("Please create a new password: ")

# Check if password exists in specified text file
file_path = "password_file.txt"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        if password in f.read():
            print("The password has been found inside a password breach. Please change it using the recommendations")
        else:
            print("Password Accepted")
else:
    print("File not found")
