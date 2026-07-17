#Print first and last character of  text
text = "Artificial Intelligence"
First_character=text[0]
last_character=text[-1]
length=len(text)
print(f"First character: {First_character}")
print(f"Last character: {last_character}")
print(f"length: {length}")


#print the name
name=input("Enter the name: ")
lowercase_name=name.lower()
uppercase_name=name.upper()
capitalize_name=name.capitalize()
title_name=name.title()
print(lowercase_name)
print(uppercase_name)
print(capitalize_name)
print(title_name)

#password validation
password=input("Enter password: ")
if " " in password:
    print("Invalid password")
else: 
    print("Password accepted")