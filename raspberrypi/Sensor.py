class Sensor:
    time = None
    temperature = None
    pressure = None
    light = None
    obstacle = None

    def __init__(self, time, temperature, pressure, light, obstacle):
        self.time = time
        self.temperature = temperature
        self.pressure = pressure
        self.light = light
        self.obstacle = obstacle
