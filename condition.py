import calendar
import datetime
now= datetime.datetime.now()
print("now time &date is ",now )
print("calender data is ",calendar.calendar(now.year))

city = input ("what is your city name?")
temp = int(input("what is the temperature"))
if temp >35:
    print("warnig! it is so hot")
elif temp >15:
    print("its normal ")
else:
    print("weather is cool")