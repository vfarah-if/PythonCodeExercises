from tire_pressure.sensor import Sensor
from tire_pressure.alarm import Alarm
from unittest.mock import Mock


def test_alarm_is_off_by_default(alarm: Alarm):
    assert alarm.isAlarmOn == False


class StubLowPressureSensor:
    def samplePressure(self):
        return 10


class StubHighPressureSensor:
    def samplePressure(self):
        return 100


class StubNormalPressureSensor:
    def samplePressure(self):
        return 18


def test_low_pressure_activates_alarm():
    # alarm = Alarm(sensor = StubLowPressureSensor())
    stubSensor = Mock(Sensor)
    stubSensor.samplePressure.return_value = 10
    alarm = Alarm(sensor=stubSensor)

    alarm.check()

    assert alarm.isAlarmOn == True


def test_high_pressure_activates_alarm():
    # alarm = Alarm(sensor=StubHighPressureSensor())
    stubSensor = Mock(Sensor)
    stubSensor.samplePressure.return_value = 100
    alarm = Alarm(sensor=stubSensor)

    alarm.check()

    assert alarm.isAlarmOn == True


def test_valid_pressure_does_notactivates_alarm():
    # alarm = Alarm(sensor=StubNormalPressureSensor())
    stubSensor = Mock(Sensor)
    stubSensor.samplePressure.return_value = 18
    alarm = Alarm(sensor=stubSensor)
    alarm.check()

    assert alarm.isAlarmOn == False
