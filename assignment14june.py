#Assignment7
#ques1
print("It may be an integer. or a floating point number (to represent fractions of seconds).The Epoch is system-defined; on Unix, it is generally January 1st, 1970. The actual value can be retrieved by calling gmtime(0).The other representation is a tuple of 9 integers giving local time")

#ques2
import time
print(time.asctime(time.localtime()))

#ques3
import datetime
a='1970-02-11'
d=(datetime.datetime.strptime(a,"%Y-%m-%d"))
print(d.month)

#ques4
from datetime import date
import calendar
my_date =date.today()
print(calendar.day_name[my_date.weekday()])

#ques5
x="11-01-2021"
d=datetime.datetime.strptime(x,"%d-%m-%Y")
print(d.day)

#ques6
import time
print(time.localtime()) #local time

#ques7
import math
num=int(input("enter the no"))
print(math.factorial(num))

#ques8
a=int(input("enter no1"))
b=int(input("enter no2"))
print(math.gcd(a,b))

#ques9
import os
print(os.getcwd())
print(os.environ)
