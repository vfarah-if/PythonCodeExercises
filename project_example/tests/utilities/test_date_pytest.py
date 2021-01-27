from datetime import date
from utilities.date import days_ago

# @pytest.skip('actual.day failing for some odd reason')
def test_date_generated_is_correct():
    dayCount = 2
    today = date.today()
    expectedDay = today.day - dayCount

    actual = days_ago(days=dayCount)

    assert actual.day == expectedDay
    assert actual.month == today.month
    assert actual.year == today.year
