# List Comprehension
numbers=[2,4,6,8]
double=[number*2 for number in numbers]
print(double)


#Filter
numbers=[1,2,3,4,5,6]
even=[number  for number in numbers if number%2==0 ]
print(even)

#Filter and Transformation
numbers=[1,2,3,4,5,6,7,8]
even_squares=[number**2 for number in numbers if number%2==0]
print(even_squares)

#Flattening
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
flatten_list=[number for row in matrix for number in row]
print(flatten_list)


#Dictionary comprehension
numbers=[1,2,3,4]
doubles={num: num**2 for num in numbers}
print(doubles)


#Set Comprehension 
numbers=[1,1,1,3,4,5,6,7,8,8,8,8,8,9]
squares={num**2 for num in numbers}
print(squares)