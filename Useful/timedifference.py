import datetime

print("Enter values in the format YYYY/M/D")

s_year = int(input('Enter the year which your project started:'))
s_month = int(input('Enter the month which your project started:'))
s_day = int(input('Enter the day which your project started:'))
start_date = datetime.date(s_year, s_month, s_day)

e_year = int(input('Enter the year which your project ended:'))
e_month = int(input('Enter the month which your project ended:'))
e_day = int(input('Enter the day which your project ended:'))
end_date = datetime.date(e_year, e_month, e_day)

year_diff = e_year - s_year
month_diff = e_month - s_month
day_diff = e_day - s_day
print("Your project lasted", year_diff, "year(s),", month_diff, "month(s), and", day_diff, "day(s).")
