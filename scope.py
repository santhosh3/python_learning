name = "ravi"
count = 1

def another():
     color = "Blue"
     global count
     count += 1
     print(count)

     def greeting(name):
          nonlocal color
          color = "Red"
          print(color)
          print(name)

     greeting("DEVE")

another()