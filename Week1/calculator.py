print("Calculator")
def multiply(first_num,sec_num):
    return first_num*sec_num
def plus(first_num,sec_num):
    return first_num+sec_num
def minus(first_num,sec_num):
    return first_num-sec_num
def divide(first_num,sec_num):
    if sec_num==0:
        return "cannot divide by zero"
    return first_num/sec_num




first_number=int(input("Enter the First number: "))
second_number=int(input("Enter the Second number: "))
print("choose the operator:")
print("/")
print("+")
print("-")
print("+")

operater=input("Enter the operator: ")
if operater=="*":
    multiply(first_number,second_number)
    print(multiply)
elif operater=="/":
    divide(first_number,second_number)
    print(divide)
elif operater=="-":
    minus(first_number,second_number)
    print(minus)
elif operater=="+":
    plus(first_number,second_number)
    print(plus)
else:
    print("You enter wrong operator")

