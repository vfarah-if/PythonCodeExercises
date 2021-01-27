from datetime import date, timedelta

def days_ago(days: int) -> date:
    return date.today() - timedelta(days=days)
