# Задание №1
class Transport:
   def __init__(self, name, max_speed, mileage):

      self.name = name
      self.max_speed = max_speed
      self.mileage = mileage

   def seating_capacity(self, capacity):
      return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"



Autobus = Transport("Renault Logan", 180, 12)
print(f"Название автомобиля: {Autobus.name} Скорость: {Autobus.max_speed} Пробег: {Autobus.mileage}")


# Задание №2
class Autobus(Transport):
   def seating_capacity(self, capacity=50):
      return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"


Bus = Autobus("Renault Logan", 180, 12)
print(Bus.seating_capacity())
 


