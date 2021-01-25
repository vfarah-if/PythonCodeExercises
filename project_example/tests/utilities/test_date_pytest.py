from datetime import date
from utilities.date import daysAgo

# @pytest.skip('actual.day failing for some odd reason')
def test_date_generated_is_correct():
    dayCount = 2
    today = date.today()
    expectedDay = today.day - dayCount

    actual = daysAgo(days=dayCount)

    assert actual.day == expectedDay
    assert actual.month == today.month
    assert actual.year == today.year
