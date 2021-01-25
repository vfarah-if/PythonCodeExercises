from tire_pressure.sensor import Sensor
from tire_pressure.alarm import Alarm
from unittest.mock import Mock


def test_alarm_is_off_by_default(alarm: Alarm):
    assert alarm.isAlarmOn == False


def test_low_pressure_activates_alarm():
    alarm = Alarm(sensor=stubSensor(10))

    alarm.check()

    assert alarm.isAlarmOn == True


def test_high_pressure_activates_alarm():
    alarm = Alarm(sensor=stubSensor(100))

    alarm.check()

    assert alarm.isAlarmOn == True


def test_valid_pressure_does_notactivates_alarm():
    alarm = Alarm(sensor=stubSensor(18))
    alarm.check()

    assert alarm.isAlarmOn == False


def stubSensor(pressure: int):
    result = Mock(Sensor)
    result.samplePressure.return_value = pressure
    return result
