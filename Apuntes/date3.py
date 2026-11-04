from datetime import datetime

hourNow = datetime.now()
hourExam = datetime(2026,10,21,12,30,00)

diffHours = hourExam - hourNow

print(f'The exam is in {diffHours}')