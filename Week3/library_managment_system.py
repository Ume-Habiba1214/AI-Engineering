import library_functions

author=input("Enter the name of Author: ")
title=input("Enter the Title of Book: ")
library_functions.display_details(author,title)



try:
    price=int(input("Enter the price of a book: "))
    quantity=int(input("Enter the number of copies: "))
    total_cost=library_functions.calculate_cost(price,quantity)
    print(f"The price of {quantity} copies : {total_cost}")
except ValueError:
    print("Please enter valid values ")

finally:
    print("Thank you for using the system ")