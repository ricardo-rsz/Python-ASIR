from datetime import datetime

mycurrentDate = datetime.now()

print("Current date and time: ", mycurrentDate)

print("Current year: ", mycurrentDate.year)
print("Current month: ", mycurrentDate.month)
print("Current day: ", mycurrentDate.day)

print("dd/mm/yyyy format: ", mycurrentDate.strftime("%d/%m/%y"))
print("hh:mm:ss format: ", mycurrentDate.strftime("%H/%M/%S"))

print("timestamp: ", int(mycurrentDate.timestamp()))


mycurrentTimestamp = int(mycurrentDate.timestamp())
print("Current date and time from timestamp: ", datetime.fromtimestamp(mycurrentTimestamp))