from datetime import datetime, timedelta

now = datetime.now()
print("Current datetime:", now)
print("Date only:", now.date())
print("Time only:", now.time())

future = now + timedelta(days=10, hours=2)
print("After 10 days and 2 hours:", future)

def format_date(dt: datetime):
    return dt.strftime("%d-%m-%Y %H:%M:%S")

print("Formatted:", format_date(now))
