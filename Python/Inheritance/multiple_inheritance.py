from models import Engine, ElectricSystem
from main import Car

class HybridCar(ElectricSystem, Engine, Car):
    def __init__(self, make, model, year, fuel_type, power, voltage):
        Car.__init__(self, make, model, year, fuel_type)
        Engine.__init__(self, power)
        ElectricSystem.__init__(self, voltage)

    def get_hybrid_info(self):
        return f"This is a hybrid car with {self.power} HP and {self.voltage} V system"
my_hybrid = HybridCar("Toyota", "Prius", 2022, "Hybrid", 121, 300 )
# print(my_hybrid.get_hybrid_info())
print(my_hybrid.get_all_info())
# print(my_hybrid.start_engines())