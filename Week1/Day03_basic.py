#Print numbers from 1 to 20.
print("Exercise 01")
for i in range(1, 21):
    print(i)

#Print even numbers from 2 to 20.
print("\n")
print("Exercise 02")
for i in range(2, 21, 2):
    print(i)

#Print odd numbers from 1 to 19.
print("\n")
print("Exercise 03")
for i in range(1, 20, 2):
    print(i)

#Print your name 10 times.
#We can use _ to tell other that we don`t need any variable here.
print("\n")
print("Exercise 04")
for _ in range(10):
    print("Ali")

#Print numbers from 20 to 1
print("\n")
print("Exercise 05")
i=20
while i>0:
    print(i)
    i-=1

#Ask the user for a number and print its table.
print("\n")
print("Exercise 06")
number=int(input("Enter the number for table: "))
for i in range(1, 11):
    print(f"{number} * {i} = {i*number}\n")

#Print the pattren in ascending order
print("\n")
print("Exercise 07")
for i in range(1, 6):
    print("*"*i)

#Print the pattren in descending order
# we can use for i in range(5, 0, -1):
print("\n")
print("Exercise 08")
i=5
while i>0:
    print("*"*i)
    i-=1

#Print all numbers from 1 to 50 except 25.
print("\n")
print("Exercise 09")
for i in range(1, 51):
    if i==25:
        continue
    print(i)

#Write a program that asks the user to enter a positive number and then calculates the sum of all numbers from 1 to that number
print("\n")
print("Exercise 10")
number=int(input("Enter the number: "))
total=0
if number>0:
    for i in range(1, number+1):
        total+=i
    print(f"Answer = {total}")
else:
    print("you enter invalid number. Enter only positive number from 1")


#Print the Pattren 
print("Bonus Challange")
j=9
for i in range(1, 10, 2):
    while j>0:
        print(" "*(j//2),"*"*i)
        j-=2
        break




print("Bonus Challange")
space_number=9
for i in range(1, 10, 2):
    print(" "*(space_number//2),"*"*i)
    space_number-=2
    


