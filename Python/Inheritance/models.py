class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    def start_engines(self):
        return "Engine started...."
    def get_all_info(self):
         return f"{self.year} {self.make} {self.model}"


class Electric_Car(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
    def start_engines(self):
        return "Electric engine started silently...."
    
    def get_battery_info(self):
        return f"This electric car has a battery capacity of {self.battery_capacity} kWh."
    def get_all_info(self):
        return f"{self.get_info()} - battery capacity: {self.battery_capacity} kWh"
    
class Engine:
    def __init__(self, power):
        self.power = power

    def get_power(self):
        return f"This engine produces: {self.power} HP"
    
class ElectricSystem:
    def __init__(self, voltage):
        self.voltage = voltage

    def get_voltage(self):
        return f"This electric system operates at: {self.voltage} V"