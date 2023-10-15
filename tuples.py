# Tuples

# in Tuples we are not able to change the values manupulation is not possible

mytuple = tuple(('uzumaki','nara','yuga'))

anotherTuple = (1,4,2,3,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anotherTuple))

# in order to manupulate we need to convert into list

newList = list(mytuple)
newList.append('uchiha')
newtuple = tuple(newList)
print(newtuple)

(one,*two,three) = anotherTuple
print(one)
print(two)
print(three)

print(anotherTuple.count(2))