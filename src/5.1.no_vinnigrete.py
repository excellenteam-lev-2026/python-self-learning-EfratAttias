from datetime import datetime , timedelta
import random

def no_vinnigrete(start_date, end_date):
    sdate = datetime.strptime(start_date, "%Y-%m-%d")
    edate = datetime.strptime(end_date, "%Y-%m-%d")

    range_days = (edate - sdate).days
    
    random_days = random.randint(0, range_days)
    random_date = sdate + timedelta(days=random_days)
    
    return random_date

if __name__ == "__main__":
    random_day = no_vinnigrete("2001-01-01", "2026-01-01")
    print(f"Random date: {random_day}")