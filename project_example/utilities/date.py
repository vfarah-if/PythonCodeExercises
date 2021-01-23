from datetime import date, timedelta

def daysAgo(days: int):
    return date.today() - timedelta(days=days)
