from datetime import date, timedelta

def daysAgo(days: int) -> date:
    return date.today() - timedelta(days=days)
