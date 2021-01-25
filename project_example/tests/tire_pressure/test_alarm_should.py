from tire_pressure.alarm import Alarm


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
    alarm = Alarm(sensor = StubLowPressureSensor())

    alarm.check()

    assert alarm.isAlarmOn == True


def test_high_pressure_activates_alarm():
    alarm = Alarm(sensor = StubHighPressureSensor())

    alarm.check()

    assert alarm.isAlarmOn == True

def test_valid_pressure_does_notactivates_alarm():
    alarm = Alarm(sensor = StubNormalPressureSensor())

    alarm.check()

    assert alarm.isAlarmOn == False