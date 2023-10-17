# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt")
# print(f.read()) # this will read all things that are there in file
# print(f.read(4)) # this will gives only first 4 chars in file

# print(f.readline()) # this will read only first line of file

for line in f:
     print(line)  # this will gives all lines in file

f.close()

try:
     f = open("name.txt")
     print(f.read())
except:
     print("The file u want to read doesn't exist")
finally:
     f.close()

# Append - create the file if it doesn't exist

f = open("names.txt", "a")
f.write("SANTHOSH")
f.close()

f.open("names.txt")
print(f.read())
f.close()