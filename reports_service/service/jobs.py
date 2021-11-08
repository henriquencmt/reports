import os

import db

from mail import send_report
from ppt import make_daily_ppt, make_monthly_ppt
from reports import monthly_report, daily_report
from xl import make_daily_xl


def monthly_job():
    data = monthly_report()
    db.create_report('monthly', data)
    
    if db.mailing_list_emails():
        make_monthly_ppt(data)
        send_report()


def daily_job():
    data = daily_report()
    db.create_report('daily', data)
    
    if db.mailing_list_emails():
        make_daily_ppt(data)
        make_daily_xl(data)
        send_report()