#Write a Python program to calculate the number of days between two dates.
import datetime
fdate=input('enter first date(y/m/d):')
sdate=input('enter second date(y/m/d):')
first_date_list=fdate.split('/')
second_date_list=sdate.split('/')
date1=datetime.date(int(first_date_list[0]),
	int(first_date_list[1]),
	int(first_date_list[2]))
date2=datetime.date(int(second_date_list[0]),
	int(second_date_list[1]),
	int(second_date_list[2]))
if date1>date2:
	diff=(date1-date2).days
else:
	diff=(date2-date1).days
print(diff)