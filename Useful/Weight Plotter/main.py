#now with added intervals between measurements
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

start_date_str = input("Enter the start date (YYYY-MM-DD): ")
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
weights = []
weight = float(input("Enter weight for start date:"))
weights.append(weight)

interval = int(input("Enter the number of days between measurements:"))
while True:
    try:
        weight = float(input("Enter weight for next date (enter 'done' to exit):"))
        if weight == 'done':
            break
        weights.append(weight)
    except ValueError:
        break

num_days = len(weights)
dates = [start_date + timedelta(days=interval*i) for i in range(num_days)]
date_labels = [date.strftime("%Y-%m-%d") for date in dates]
max_weight = max(weights)

y_min = float(input("Enter minimum value for y-axis:"))
y_max = float(input("Enter maximum value for y-axis:"))
if y_min < 0:
    y_min = 0
if y_max < max_weight:
    y_max = max_weight

plt.plot(dates, weights)
plt.xlabel("Date")
plt.ylabel("Weight (kg)")
plt.xticks(dates, date_labels, rotation=45)
plt.ylim(y_min, y_max)
plt.show()

