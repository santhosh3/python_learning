def hello():
     print("Hello World")


hello()

def sum(num1=0,num2=0):
     if(type(num1) is not int or type(num2) is not int):
          return 0
     return num1+num2

total = sum(1,2)
print(total)

def multiple_items(*args):
     print(args)
     print(type(args))

multiple_items("DEVI","JOHN","SARA")

def multi_named_items(**args):
     print(args)
     print(type(args))

multi_named_items(first="DEVE",last="GRAY")