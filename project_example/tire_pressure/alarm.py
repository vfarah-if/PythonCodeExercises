from tire_pressure.sensor import Sensor


class Alarm:
    def __init__(self, sensor=None) -> None:
        self._lowPressureThreshold = 17
        self._highPressureThreshold = 21
        self._sensor = sensor or Sensor()
        self._isAlarmOn = False

    @property
    def isAlarmOn(self):
        return self._isAlarmOn
    
    def check(self):
        pressure = self._sensor.samplePressure()
        if pressure < self._lowPressureThreshold or pressure > self._highPressureThreshold:
            self._isAlarmOn = True
