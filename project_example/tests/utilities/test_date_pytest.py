from datetime import date
from utilities.date import days_ago


# @pytest.skip('actual.day failing for some odd reason')
def test_date_generated_is_correct():
    day_count = 2
    today = date.today()
    expected_day = today.day - day_count

    actual = days_ago(days=day_count)

    assert actual.day == expected_day
    assert actual.month == today.month
    assert actual.year == today.year
