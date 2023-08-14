class Transport(object):
   name = ""
   max_speed = 0
   mileage = 0

   def __init__(self, name, max_speed, mileage):
      self.name = name
      self.max_speed = max_speed
      self.mileage = mileage
 
class Autobus(Transport):

    capacity = 50
   
    def __init__(self,  name, max_speed, mileage):
      super().__init__(name, max_speed, mileage)
    
    def seating_capacity(self, capacity = 50):
       return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

a = Autobus("Renaul Logan", 180, 12)

print(f"Название автомобиля: {a.name} Скорость: {a.max_speed} Пробег: {a.mileage}")

print(a.seating_capacity(100))