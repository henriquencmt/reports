"""
Inspired by flask-extensions code
https://https://github.com/flask-extensions/flaskextensions.com/blob/master/fexservice/fexservice/cli.py
"""

import sched
import time

from datetime import datetime, timedelta
from typing import Callable

from jobs import daily_job, monthly_job
from settings import (
    DAILY_HOUR, DAILY_MINUTE, DAILY_PRIORITY,
    MONTHLY_HOUR, MONTHLY_MINUTE, MONTHLY_PRIORITY
)


scheduler = sched.scheduler(time.time)


def get_next_daily_execution():
    today = datetime.today()
    tomorrow = today + timedelta(days=1)
    return datetime(
        year=tomorrow.year,
        month=tomorrow.month,
        day=tomorrow.day,
        hour=DAILY_HOUR,
        minute=DAILY_MINUTE
    )


def get_next_monthly_execution():
    today = datetime.today()
    next_month = today + timedelta(days=31)
    return datetime(
        year=next_month.year,
        month=next_month.month,
        day=1,
        hour=MONTHLY_HOUR,
        minute=MONTHLY_MINUTE
    )


def daily_enqueue(action: Callable, job: Callable):
    next_execution = get_next_daily_execution()
    return scheduler.enterabs(
        next_execution.timestamp(), priority=DAILY_PRIORITY, action=action, argument=(job,)
    )


def monthly_enqueue(action: Callable, job: Callable):
    next_execution = get_next_monthly_execution()
    return scheduler.enterabs(
        next_execution.timestamp(), priority=MONTHLY_PRIORITY, action=action, argument=(job,)
    )


def task_daily_job(job: Callable):
    job()
    id = daily_enqueue(task_daily_job, job)
    print(f"[*] Daily next execution ({datetime.fromtimestamp(id.time).strftime('%Y-%m-%d')}): {id}")


def task_monthly_job(job: Callable):
    job()
    id = monthly_enqueue(task_monthly_job, job)
    print(f"[*] Monthly next execution ({datetime.fromtimestamp(id.time).strftime('%Y-%m-%d')}): {id}")


def main():
    task_daily_job(daily_job)
    task_monthly_job(monthly_job)
    scheduler.run(blocking=True)

if __name__ == '__main__':
    main()