from datetime import date

def monthly_report():
    
    # Get your monthly report data here

    today = date.today()
    return { "reference_year": today.year, "reference_month": today.month }


def daily_report():
    
    # Get your monthly report data here

    today = date.today()
    return { "reference_year": today.year, "reference_month": today.month }