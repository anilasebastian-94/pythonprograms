lst=[2,3,4,5,6]
#map: map(function,iterable/list)
#squares of all numbers: map
# def square(num):
#     return num**2
# squares=list(map(square,lst))
# print(squares)
squares=list(map(lambda num:num**2,lst))
print(squares)
#cubes of all numbers:
# cube=lambda num:num**3
cubes=list(map(lambda num:num**3,lst))
print(cubes)
#print even numbers: filter
#total of numbers in list: reduce
#lowest number in list:reduce