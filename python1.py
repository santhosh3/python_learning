import math


greeting = "Hello world"
print(greeting)

meaning = 13

# if else code
if meaning > 10:
     print('Right Cat!')
else:
     print('Not today')

# Ternary Operator code
print('Right Cat!') if meaning > 10 else print('Not today')


# data_types

# literal assignments
first = "santhosh"



print(type(first))
print(type(first) == str)
print(isinstance(first,str))

# constructor function
pizza = str("Pupperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza,str))


sentence = 'I\'m back at work! \tHey! \n\nWhere\'s this at\\location'
print(sentence)

print(first)
print(first.lower())
print(first.upper())
print(first)

print(first.title()) 
print(45)
print(first.replace('a','v'))
print(len(first))
second = "learning"+"   "
print(len(second)) # 11
print(len(second.strip())) # 8


# Build a menu

title = "menu".upper()
print(title.center(10, "="))
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$2".rjust(4))
print("MilkShake".ljust(16,".") + "$4".rjust(4))

print(first[1], 58)
print(first[-1], 59)
print(first[1:-1], 60)
print(first[1:], 61)
print(first[:-1], 62)

# return some boolean value
print(first.startswith("a"))
print(first.endswith("h"))

# booldata type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue,bool))

# integer type
price = 100
best_price = int(200)
print(type(price))
print(isinstance(best_price,int))

# float type
gpa = 3.28
y = float(2.88)
print(isinstance(gpa, float))

# complex values

comp_value = 5+3j
print(type(comp_value))
print(comp_value.imag)
print(comp_value.real)


# built in fun for python

print(abs(gpa))
print(round(gpa))
print(round(gpa,1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


# casting a string to a number

zipcode = "12001"
zip_value = int(zipcode)
print(type(zipcode),type(zip_value))
print(zipcode,zip_value)

# Error if you attempt to cast incorrect data
# code = int("fullfilled")
# print(code)