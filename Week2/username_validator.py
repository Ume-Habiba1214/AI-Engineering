

def validate_username(username):
    if len(username)<5 or " " in username or not username[0].isalpha():
        print("Invalid username")
    else:
        print("Username accepted")








username=input("Enter Username: ")
validate_username(username)