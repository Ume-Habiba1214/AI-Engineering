#tuples  are immutable
#first last length of triplets
countries = ("Pakistan", "Germany", "Italy", "Japan", "Canada")
first_country=countries[0]
last_country=countries[-1]
length=len(countries)
print(first_country)
print(last_country)
print(length)


# print all country name
for country in countries:
    print(country)

#check the country
country_name=input("enter the name of country: ")
if country_name in countries:
    print("Found")
else: 
    print("not Found")


#print  check the vowels
text=input("Enter the text to check the vowels: ")
text=text.lower()
count=0
vowel=("a","e","i","o","u")
for letter in text:
    if letter in vowel:
        count+=1

print(count)