# /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from variables import user, passw, get_password, get_username, get_week_day, weekday, wait, time_slots

weekdayList = get_week_day()

for x in weekdayList:
    print(x)


PATH = r"C:\Users\User\Documents\booking\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

ig = "https://www.instagram.com/"
gl = "https://www.goodlifefitness.com/home.html"
driver.get(gl)

button = driver.find_element_by_class_name("c-header__login-text")

wait()
button.click()
wait()

#  Enter member ID, barcode or email address
username = driver.find_element_by_xpath(get_username)

wait()
username.send_keys(user)

#  Enter password
password = driver.find_element_by_xpath(get_password)
wait()
password.send_keys(passw)
wait()

robot = driver.find_elements_by_xpath(
    '//*[@id="rc-anchor-container"]/div[3]/div[1]/div/div')
wait()
robot.click()
wait()

# login
# Pressed the return to key to submit the login form
button = driver.find_element_by_xpath(
    '//*[@id="gl_aut_user_login"]/div[2]/form/div[6]/button')
wait()


button = driver.find_element_by_xpath(
    '//*[@id="nav"]/ul/li[3]/div/a')
wait()
button.click()
wait()


# navigated to workout booking page
viewschedule = driver.get(
    'https://www.goodlifefitness.com/book-workout.html#no-redirect')
wait()

# resized the window to allow access to all elements
driver.set_window_size(1920, 1080)
wait()

# clicking the lastest day displayed on the calender
element = driver.find_element_by_xpath(weekday)
wait()
element.click()
wait()

# Select list item corresponding to booking time i.e (li[7]=> 4:30pm slot)
for x in weekdayList:

    string = '//*[@id="day-number-7"]/li[' + \
        str(x)+']/div[2]/div/div[2]/div[1]/button'

    print(string)
    book = driver.find_element_by_xpath(string)

    wait()

    book.click()
    wait()

    # Agree to the terms and conditions
    checkbock = driver.find_element_by_xpath(
        '//*[@id="js-workout-booking-agreement-input"]')
    wait()
    checkbock.click()
    wait()

    # Find the web element for the button and click confirm button to book your workout.
    confirm = driver.find_element_by_xpath(
        '//*[@id="class-modal-container"]/div[4]/div/button[1]')
    wait()
    confirm.click()
    wait()

    close = driver.find_element_by_css_selector(
        '#js-classes-schedule > div:nth-child(4) > div.c-modal.c-schedule-calendar__class-details-modal.js-class-modal.u-transition-visible > div > div.modal-submition-close.js-class-action-modal-submition-close.u-is-block > button')
    close.click()

    wait()

# //*[@id = "day-number-7"]/li[8]/div[2]/div/div[2]/div[1]/button 3.30

# close the web browser
driver.quit()
