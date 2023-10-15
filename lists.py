users = ['Naruto','Shikamaru','Gara']

data = ['Hinata', 34, True]

emptyList = []

print("Naruto" in users)
# this will say weather element is present in users list or not

print(users[0])
# this will print 0th index element in List

print(users[-2])
# this will print last but -2 index element in List

print(users.index('Gara'))
#  this is something like print index of element like indexOf in JS

print(users[0:2])
#  this will print index between 0 to 2

print(users[1:])
#  this is something like slice in JS this will print all including starting index

print(len(data))
#  this will print the length of the list or array

users.append('choji')
# this is also push in JS
print(users)

users += ['Eno']
# this is something like push in JS
print(users)

users.extend(['Rocklee','Akamaru']) 
# add values at end of the list
print(users)


users.extend(data)
# this is some thing like concat 2 lists
print(users)

users.insert(0,'saskay')
print(users)

users[2:2] = ['Neji','tenten']
# this will add these 2 values in list at index 2
print(users)

users[1:3] = ['kakashi','obito']
# this will replace 2 and 3 index with kakashi and obito
print(users)

users.remove('Eno')
# this will removes user provided
print(users)

users.pop()
users.pop()
# this will delete the last item in the list
print(users)

del users[0]
print(users)

data.clear()
# this will remove the data list

users.sort()
print(users)

users[0:1] = ['dada']
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums, reverse=True))


# this makes the copy of nums
numsCopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(type(nums))

myList = list([1,"santhost",True])
print(myList)
