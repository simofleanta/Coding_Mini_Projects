# Create a Time class and initialize it with hours and minutes.
# 1. Make a method add_time which should take two time object and add them.
# Example: (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# 2. Make a method display_time which should print the time.
# 3. Make a method display_minute which should display the total minutes in the Time.
# Example: (1 hr 2 min) should display 62 minute.
import datetime
from datetime import date

class Time:

    def __init__(self, hours, minutes):
        self.hours=hours
        self.minutes=minutes

        

    def add_time(self, t1, t2):
         return (t1*2+t2+0.5)+(t1+t2+0.2)


    def display_time(self):
        pass  # YOUR CODE GOES HERE, REMOVE PASS

    def display_minute(self):
        pass  # YOUR CODE GOES HERE, REMOVE PASS

#------------------------------------------------

def time(today):
    today = date.today()
    return today

print(time("Today's date:" ))











#https://codereview.stackexchange.com/questions/19502/python-time-class-definition-and-methods-use-of-init