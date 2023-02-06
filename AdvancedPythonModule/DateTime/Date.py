#first we need to import
import datetime
#time accept parameter, 2 am , past 20 minutes
mydatetime = datetime.time(2,20)

print(mydatetime.minute) # 20 #will give me minute
print(mydatetime.hour) # 2 #will give me hour
print(mydatetime)#02:20:00

mydatetime = datetime.time(2)

print(mydatetime.minute) # 0 #will give me minute
print(mydatetime.hour) # 2 #will give me hour
print(mydatetime)#02:00:0

print(mydatetime.microsecond)#0

print(type(mydatetime))#<class 'datetime.time'>


###  if I want to print current date,
today = datetime.date.today()
print(today) #2023-01-20, this is the format, first year, month and date

#if we want to grab year month or date seperately
print(today.year)#2023
print(today.month)#1
print(today.day)#20

# if we want to a different format
print(today.ctime()) # Fri Jan 20 00:00:00 2023


from datetime import datetime
#accept year month day hour, minute ,second
mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)#2021-10-03 14:20:01

# if we made a mistake with intake of year or any other input  we use replace
#no zero before month day hour minute or second when they are one digit
mydatetime =mydatetime.replace(2021,9,3,14,20,1)
print(mydatetime)#2021-09-03 14:20:01


from datetime import date
date1 = date(2021,11,3)
date2 = date(2020,11,3)
#to see the days differences between two dates
result = date1 - date2
print(type(result))#<class 'datetime.timedelta'>

print(result.days)#365

#to see the result difference with hour
#there is 10 hour difference with one year
datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

print(datetime1 - datetime2)#365 days, 10:00:00
# if we want to see each differences seperately
mydiff = datetime1 - datetime2
#just second
print(mydiff.seconds)#36000
# everything in second
print(mydiff.total_seconds())#31572000.0

