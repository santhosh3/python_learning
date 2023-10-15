# x = 2
# try:
#      print(x/0)
# except NameError:
#      print("There is an error")
# except ZeroDivisionError:
#      print("Please do not divide by Zero.")
# else:
#      print('No errors!')
# finally:
#      print("I'm going to print with or without an error")

##################################################################

x = 2
try:
     if type(x) is not str:
          raise TypeError("Only strings are allowed")
except NameError:
     print("There is an error")
except ZeroDivisionError:
     print("Please do not divide by Zero.")
except Exception as error:
     print(error)
else:
     print('No errors!')
finally:
     print("I'm going to print with or without an error")


##########################################################

class JustNotCoolError(Exception):
     pass

x = 2
try:
     raise JustNotCoolError("This Just isn't cool,man")
except NameError:
     print("There is an error")
except Exception as error:
     print(error)
except ZeroDivisionError:
     print("Please do not divide by Zero.")
else:
     print('No errors!')
finally:
     print("I'm going to print with or without an error")