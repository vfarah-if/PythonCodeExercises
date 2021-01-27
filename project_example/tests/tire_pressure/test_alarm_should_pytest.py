from tire_pressure.sensor import Sensor
from tire_pressure.alarm import Alarm
from unittest.mock import Mock, patch


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


def test_call_sensor_sample_pressure():
    sensorSpy = stubSensor(100)
    alarm = Alarm(sensor=sensorSpy)

    alarm.check()

    sensorSpy.samplePressure.assert_called_once()

# REMARKS: Patch makes more sense if the constructor does not allow for sensor to be assigned


def test_high_pressure_activates_alarm_using_monkeypatch():
    # REMARKS refers to the modules in the patch param
    with patch("tire_pressure.alarm.Sensor") as sensorType:
        sensorInstance = Mock()
        sensorInstance.samplePressure.return_value = 22
        sensorType.return_value = sensorInstance

        alarm = Alarm()
        alarm.check()

        assert alarm.isAlarmOn == True


@patch("tire_pressure.alarm.Sensor")
def test_low_pressure_activates_alarm_using_monkeypatch_decorator(sensorType):
    print(sensorType)
    sensorInstance = Mock()
    sensorInstance.samplePressure.return_value = 14
    sensorType.return_value = sensorInstance

    alarm = Alarm()
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
