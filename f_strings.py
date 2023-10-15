person = "Dave"
coins = 3

# old style of writing concatinating
print("\n" + person + " has " + str(coins) + " coins left. ")


# new Style
message = "\n%s has %s coins left." %(person,coins)
print(message)

message = "\n{} has {} coins left".format(person,coins)
print(message)

message = "\n{1} has {0} coins left".format(coins,person)
print(message)

message = "\n{person} has {coins} coins left".format(coins=coins,person=person)
print(message)

player = {
     'person' : 'santhosh',
     'coins' : 3
}

message = "\n{person} has {coins} coins left".format(**player)
print(message)

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person.lower()} has {2+3} coins left."
print(message)

message = f"\n{player['person']} has {player['coins']} coins left."
print(message)

num = 10
message = f"\n 2.25 times {num} is {2.25 * num:.2f}"
print(message)

for i in range(1,11):
     print(f" 2.25 times {i} is {2.25 * i:.2f}")

for i in range(1,11):
     print(f"{i} divided by 4.52 is {i/4.52:.2%}")

