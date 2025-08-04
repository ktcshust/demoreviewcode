from datetime import datetime

def calculate_duration(start_date, end_date):
    return (end_date - start_date).days

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")
