

def add_item(shopping):
    item=input("Enter Item: ")
    shopping.append(item)
    return shopping

def remove_item(shopping):
    item=input("Enter item to remove: ")
    if item in shopping:
        shopping.remove(item)
    else:
        print("Item not Found")
    return shopping

def show_items(shopping):
    print(shopping)

def main(shopping):
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show List")
    print("4. Exit")
    option=int(input("Choose the option number from Menu: "))
    if option==1:
        add_item(shopping)
    elif option==2:
        remove_item(shopping)
    elif option==3:
        show_items(shopping)
    elif option==4:
        print("Bye")
    else:
        print("Invalid Value")
    return shopping
shopping = []
shoppinglist= main(shopping)
decision= input(" Enter Y/N for yes or No :").lower()
if decision=="y":
    main(shoppinglist)
else:
    print(" Bye")