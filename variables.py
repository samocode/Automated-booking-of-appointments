import time
from datetime import date
import calendar

#login credentails for user account
user = ""
passw = ""

time_slots = [9, 10]  # booking 2 specific time slots, 4pm and 5:15pm

# using css locator 
get_username = '//*[@id="gl_aut_user_login"]/div[2]/form/div[1]/label/input'

# using css locator
get_password = '//*[@id="gl_aut_user_login"]/div[2]/form/div[2]/label/input'

# path to navigate to the weekly workout schedules
weekday = '//*[@id="js-class-schedule-weekdays-container"]/li[4]'


def wait():
    time.sleep(2)
    return

# function to return the specifc day of the week since time slots vary on weekends
def get_week_day():

    todayDate = date.today()
    if ((todayDate.weekday()-1) > -1):

        dayofweek = calendar.day_name[todayDate.weekday()-1]
    else:
        dayofweek = "Sunday"

    print(dayofweek)

    if((dayofweek == "Saturday") or (dayofweek == "Monday")):
        print("T")
        time_slots = [10, 11]
    else:
        time_slots = [9, 10]

    return time_slots

thisdict = {
    "0": "Sunday",
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday"
}


get_week_day()
