# Dictinories

band = {
     "vocals" : "Plant",
     "guitar" : "page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access Items
print(band['vocals'])
print(band.get('guitar'))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of keys/values pairs as tuples
print(band.items())

# verify key exists
print("guitar" in band)
# not work print(print(True) if(band["guitar"]) else print(False))

print("triangle" in band)

# change the values
band["vocals"] = "Coverdals"
band.update({"vocals": "updating"})

# in order to add new values then
band.update({"name" : "aleska"})
band["testing"] = "done"

print(band)


# Remove items in dictionarie
# need to give key name then it will remove the item

print(band.pop('vocals')) 
print(band)


# this will remove the last item in the dist
print(band.popitem())
print(band)

# Delete and clear

# one of the way to remove item
del band["guitar"]
print(band)

# this will clear all and give empty dict
band.clear()
print(band)

# this will delete band obj also
del band


# copy dict

band3 = band2  # create a reference not a copy if u change band3 band2 also change

# this is using copy method-1
band3 = band2.copy()
band3["drums"] = "DAVE"

print(band3)
print(band2)

# method-2 using the dist() constructor function
band4 = dict(band3)
band4["a"] = "b"

print(band3)
print(band4)


# nested dictionaries

member1 = {
     "name" : "Plant",
     "instrument" : "vocals"
}

member2 = {
     "name" : "Page",
     "instrument" : "guitar"
}

band = {
     "member1" : member1,
     "member2" : member2
}

print(band)
print(band["member1"]["name"])