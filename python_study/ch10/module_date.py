import datetime

set_day = datetime.date(2019, 3, 1)
print(set_day)

print('{0}/{1}/{2}'.format(set_day.year, set_day.month, set_day.day))

day1 = datetime.date(2019, 4, 1)
day2 = datetime.date(2019, 7, 10)
diff_day = day2 - day1
print(diff_day)

print(type(day1))
print(type(diff_day))

print("** 지정된 두 날짜의 차이는 {}일입니다. **".format(diff_day.days))

print(datetime.date.today())

today = datetime.date.today()
special_day = datetime.date(2018, 12, 31)
print(special_day - today)

set_time = datetime.time(15, 30, 45)
print(set_time)

print('{0}:{1}:{2}'.format(set_time.hour, set_time.minute, set_time.second))

set_dt = datetime.datetime(2018, 10, 9, 10, 20 , 0)
print(set_dt)

print('날짜 {0}/{1}/{2}'.format(set_dt.year, set_dt.month, set_dt.day))
print('시각 {0}:{1}:{2}'.format(set_dt.hour, set_dt.minute, set_dt.second))

now = datetime.datetime.now()
print(now)

print("Date & Time : {:%Y-%m-%d, %H:%M:%S}".format(now))

print("Date: {:%Y,%m,%d}".format(now))
print("Time: {:%H/:%M/:%S}".format(now))

now = datetime.datetime.now()
set_dt = datetime.datetime(2017, 12, 1, 12, 30, 45)

print("현재 날짜 및 시각:", now)
print("차이:", set_dt - now)

from datetime import date, time, datetime
print(date(2019, 7, 1))

print(date.today())
print(time(15, 30, 45))
print(datetime(2020, 2, 14, 18, 10, 50))
print(datetime.now())







