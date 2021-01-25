class Sensor:
    def __init__(self, pressure = 18):
      self._pressure = pressure

    def samplePressure(self):
        return self._pressure;
