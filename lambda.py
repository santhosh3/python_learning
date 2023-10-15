

from functools import reduce


squared = lambda num : num*num
# def squared(num): return num*num

print(squared(2))

addTwo = lambda num : num+2
# def addTwo(num): return num+2

print(addTwo(3))

sum = lambda a,b : a+b
# def sum(a,b): return a+b

print(sum(3,5))


######################################################

def funcBuilder(x):
     return lambda num: num+x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

######################################################

# Higer Order Functions

# map

numbers = [3,7,12,17,20,21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

# filter

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

# Reduce

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc+curr, numbers)

print(total)

