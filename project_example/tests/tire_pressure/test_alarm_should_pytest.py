from tire_pressure.sensor import Sensor
from tire_pressure.alarm import Alarm
from unittest.mock import Mock, patch


def test_alarm_is_off_by_default(alarm: Alarm):
    assert alarm.is_alarm_on is False


def test_low_pressure_activates_alarm():
    alarm = Alarm(sensor=mock_sensor(10))

    alarm.check()

    assert alarm.is_alarm_on is True


def test_high_pressure_activates_alarm():
    alarm = Alarm(sensor=mock_sensor(100))

    alarm.check()

    assert alarm.is_alarm_on is True


def test_call_sensor_sample_pressure():
    sensor_spy = mock_sensor(100)
    alarm = Alarm(sensor=sensor_spy)

    alarm.check()

    sensor_spy.sample_pressure.assert_called_once()


# REMARKS: Patch makes more sense if the constructor does not allow for sensor to be assigned


def test_high_pressure_activates_alarm_using_monkeypatch():
    # REMARKS refers to the modules in the patch param
    with patch("tire_pressure.alarm.Sensor") as sensorType:
        mock_instance = Mock(Sensor)
        mock_instance.sample_pressure.return_value = 22
        sensorType.return_value = mock_instance

        alarm = Alarm()
        alarm.check()

        assert alarm.is_alarm_on is True


@patch("tire_pressure.alarm.Sensor")
def test_low_pressure_activates_alarm_using_monkeypatch_decorator(sensor_type):
    print(sensor_type)
    mock_instance = Mock(Sensor)
    mock_instance.sample_pressure.return_value = 14
    sensor_type.return_value = mock_instance

    alarm = Alarm()
    alarm.check()

    assert alarm.is_alarm_on is True


def test_valid_pressure_does_not_activate_alarm():
    alarm = Alarm(sensor=mock_sensor(18))
    alarm.check()

    assert alarm.is_alarm_on is False


def mock_sensor(pressure: int):
    result = Mock(Sensor)
    result.sample_pressure.return_value = pressure
    return result
