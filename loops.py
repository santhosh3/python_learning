# while loop

value = 1

# while value < 10:
#      print(value)
#      if value == 5:
#           break
#      value += 1


# while value < 10:
#      value += 1
#      if value == 5:
#           continue
#      print(value)

# while value <= 10:
#      value += 1
#      if value == 5:
#           continue
#      print(value)
# else :
#      print("Value is now equal to " + str(value))

names = ["Dave", "Sara", "John"]

# for x in names:
#      print(x)

# for x in "Mississippi":
#      print(x)

# for x in names:
#      if x == 'Sara':
#           break
#      print(x)


# for x in range(10):
#      print(x)


# for x in range(5,10):
#      print(str(x) + '🐍' )


# for x in range(0,101,5):
#      print(str(x)+'🐌')
# else:
#      print("DONE")


names = ['akamaru','shikamaru','shino']
actions = ['acid', 'goast','insects']

# for name in names:
#      for action in actions:
#           print(name + " " + action + " . ")

for action in actions:
     for name in names:
          print(name + " " + action + " . ")
