# Star printing function

print("Exercise 01")
def print_star():
    print("**********")

print_star()
print_star()
print_star()
print()



#Function that print your name
print("Exercise 02")
def print_name(name):
    print(f"{name}")

print_name("ali")
print()

#print square
print("Exercise 03")
def print_square(number):
    print(number*number)

print_square(5)
print_square(4)
print()

#Function that calculate distance
print("Exercise 04 ")
def calculate_discount(price, discount_percent):
    discounted_amount=(price*discount_percent)/100
    return price-discounted_amount

discounted_price=calculate_discount(100, 20)
print(discounted_price)
print()


#Function that  find the largest number
print("Exercise 05 ")
def find_largest(a, b, c):
    if a<=b and c<=b:
        return b
    if b<=a and c<=a:
        return a
    else:
        return c

largest_number=find_largest(12,7,18)
print(largest_number)
print()

#Function that  find the prime number
print("Exercise 06 ")
def is_prime(number):
    prime=False
    if number>1:
        i=2
        while i<number:
            if number%i==0:
             return prime
            i+=1
        prime=True
    return prime
print(is_prime(13))