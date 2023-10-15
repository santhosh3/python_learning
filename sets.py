nums = {1,2,3,4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)

print(type(nums))
print(len(nums))
# no duplicates allowed

# check if the value present in set
print(2 in nums)


# but u cannot refer to an element in the set with an index position or a key

# add an element in set
nums.add(22)
print(nums)

# Add elements from one set to another set
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples and dictionaries too.


# merge two sets to create new set
one = {1,2,3}
two = {3,4,5,6}

mynewSet = one.union(two)
print(mynewSet)

one.intersection_update(two)
print(one)          # 3

# opposite of intersection_update

one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)

