#Sets
# print the set
set_of_number={10,20,30,20,40,10,50}
print(set_of_number)


# ask user to add 5 unique color store then in set
unique_color_set=set()
while(len(unique_color_set)<5):
    color=input("Enter the unique color: ")
    if color in unique_color_set:
        print("You Enter the duplicate")
    else:
        unique_color_set.add(color)
print(unique_color_set)


# do unioun, intersection, minus,  symmetric difference
english = {"Ali", "Sara", "Ahmed", "John"}
math = {"Ahmed", "John", "David"}
print(f"Students with both subjects: {english&math}")
print(f"Students taking only English:  {english-math}")
print(f"Students taking either subjects: {english|math}")
print(f"Students taking exectly one subject: {english^math}")



# print unique letters in the word
#letter_set = set(word) we can do this in one line 
word="Programming"
letter_set=set()
for letter in word:
    letter_set.add(letter)
print(letter_set)


# ask user to Enter 10 numbers
number_set=set()
for i in range(10):
    number=int(input("Enter the number: "))
    number_set.add(number)
print(number_set)
print(f"The length of unique numbers is {len(number_set)}")
print(f" Largest number is {max(number_set)}")
print(f" Smallest number is {min(number_set)}")



# compare the hobbies of two persons 

person1 = {"Reading", "Coding", "Gaming", "Travel"}
person2 = {"Gaming", "Cooking", "Reading", "Music"}
print(f" Shared hobbies    {person1&person2}")
print(f" Hobbies only person 1 has {person1-person2}")
print(f" Hobbies only person 2 has  {person2-person1}")
print(f" All  hobbies combined  {person1|person2}")






