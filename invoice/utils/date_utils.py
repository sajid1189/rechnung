from django.utils import timezone
from datetime import datetime, timedelta


def start_of_period_date():
    return datetime.now().replace(day=1).date()


def end_of_period_date():
    start = datetime.now().replace(day=1).date()
    current_month = datetime.now().month
    next_month = current_month + 1 if current_month != 12 else 1
    first_of_next_month = start.replace(day=1, month=next_month)
    return first_of_next_month - timedelta(days=1)
