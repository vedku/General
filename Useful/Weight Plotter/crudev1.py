#rotate dates
# +- values on y axis
import matplotlib.pyplot as plt
import datetime

year = int(input("What year did you start?:"))
month = int(input("What month did you start?:"))
day = int(input("What date did you start?:"))
starting_date = datetime.datetime(year,month,day)
amount = int(input("For how many days have you been recording data?"))
weights = [100,99,101,93,102,92,99]
dates = [starting_date]
for i in range(amount-1):
    dates.append(dates[-1] + datetime.timedelta(days=1))

plt.plot(dates, weights)
plt.show()
