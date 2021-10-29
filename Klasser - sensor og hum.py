class sensor_class:
    def __init__(self):
        self.temperatur = 0
        self.humidity = 0
    def set_temperature(self, measured_val: int):
        self.temperatur = measured_val
    def set_humidity(self, measured_val: int):
        self.humidity = measured_val

print(sensor_class.description)
mysensor = sensor_class()
mysensor.set_temperature(23)
def my_func():
    print("Measured temp:", mysensor.temperature)
my_func()