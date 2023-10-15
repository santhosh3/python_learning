class Vehicle:
     def __init__(self,make,model):
          self.make = make
          self.model = model

     def moves(self):
          print("Moves along..")
     
     def get_make_model(self):
          print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle("Tesla","Model 3")

my_car.get_make_model()
my_car.moves()

class Airplane(Vehicle):
     def __init__(self,make,model,faa_id):
          super().__init__(make,model)
          self.faa_id = faa_id

     def moves(self):
          print("Flies along..")

class Truck(Vehicle):
     def moves(self):
          print("Rumbles along..")


cessa = Airplane('Cessna','Skyhawk','A-12345')

cessa.get_make_model()
cessa.moves()

print('\n\n')

for v in (my_car,cessa):

     v.get_make_model()
     v.moves()