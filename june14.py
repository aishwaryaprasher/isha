import time
time.time()
#print(time.time())
print(time.gmtime())
print(time.asctime()) #passes the all 9 parameters of time
print(time.ctime()) #passes secs
print(time.localtime()) #local time


#importing built in module datetime

import datetime
from datetime import date
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(date.today())
print(date.fromtimestamp(999811989))

import os
print(os.name)
print(os.environ)


