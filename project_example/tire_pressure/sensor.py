class Sensor:
    def __init__(self, pressure = 18):
      self._pressure = pressure

    def sample_pressure(self):
        return self._pressure;
