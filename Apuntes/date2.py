from datetime import datetime

today = datetime.now()

exam = datetime(2026,10,28)

if exam > today:
    diffdate = exam - today
    print(f"The exam is in {diffdate} days")
elif exam == today:
    print("The exam is today")
else:
    print(f"The exam was {abs}")

