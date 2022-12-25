#doesn't work yet
import matplotlib.pyplot as plt
import datetime
year = int(input("what year did you start"))
month = int(input("what month did you start"))
date = int(input("what date did you start"))
date = datetime.datetime(year,month,date)
amount = int(input("how many days did you record weight values?"))
for i in range(amount):
    date += str(datetime.timedelta(days=1))

x = [100,99,101,93,102,92,99]
y = [date]

plt.plot(x, y)

#plt.xlabel(input("What is being plotted on the Y axis?:"))
#plt.ylabel(input("What is being plotted on the X axis?:"))

#plt.title(input("What do you want your graph to be called?:"))

plt.show()
