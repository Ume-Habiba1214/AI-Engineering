import os

print("Current folder:", os.getcwd())
print("This script is located at:", os.path.dirname(os.path.abspath(__file__)))

with open("my_info.txt","w") as file:
    file.write("Name: Abeeha \n")
    file.write("Country: Germany \n")
    file.write("Goal: Become AI Engineer \n")

with open("my_info.txt", "r") as file:
    print(file.read())