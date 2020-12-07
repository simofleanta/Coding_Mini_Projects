import calendar
yy=2020
mm=11
dd=5
yy=int(input("enter year:"))
mm=int(input("enter month: "))
dd=int(input("enter day: "))
print("show calendar")
print(calendar.monthcalendar(yy,mm))

#-------------------------------------------------
def calendars(year,month):
    year=2020
    month=11
    
    return (calendar.calendar(year,month))

calendar=calendars(2020,11)
print(calendar)
    


