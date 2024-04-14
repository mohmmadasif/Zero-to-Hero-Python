#Write a program to display a calendar

import calendar

year = int(input("Enter your desired year:"))
month = int(input("Enter you deisred month:"))

cal = calendar.month(year,month)
print(cal)