from models import Electric_Car


my_tesla = Electric_Car("Tesla", "Model S", 2022, 100)
print(my_tesla.get_info())
print(my_tesla.start_engines())
print(my_tesla.get_battery_info())
print(my_tesla.get_all_info())