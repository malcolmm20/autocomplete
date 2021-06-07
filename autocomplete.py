from datetime import datetime, date, time, tzinfo, timedelta, timezone
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as time2

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://app.acuityscheduling.com/schedule.php?owner=19458395')

class TZPST(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours = -7)
    def dst(self, dt):
        return timedelta(0)
    def tzname(self, dt):
        return self.name

print('Enter the appointment date and 24 hour time in the format of YYYY-MM-DD HH:MM')
input = input()
list = input.replace('-', ' ').replace(':', ' ').split(' ')
year = int(list[0])
month = int(list[1])
day = int(list[2])
d = date(year, month, day)
hour = int(list[3])
minute = int(list[4])
t = time(hour, minute)
dt = datetime.combine(d, t, tzinfo=TZPST())
unix_pst = int((dt - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds())
id = 'lbl_appt' + str(unix_pst)

time_btn = driver.find_element_by_id(id)
time_btn.click()

time2.sleep(1)
time_actions_list = driver.find_elements_by_tag_name('li')
time_actions_list[0].click()

time2.sleep(2)
first_name = driver.find_element_by_id('first-name')
first_name.clear()
first_name.send_keys('Malcolm')

last_name = driver.find_element_by_id('last-name')
last_name.clear()
last_name.send_keys('Mackenzie')

phone = driver.find_element_by_id('phone')
phone.send_keys('604-316-1107')

email = driver.find_element_by_id('email')
email.send_keys('malcolmmackenzie20@gmail.com')

submit = driver.find_element_by_xpath("//input[@type='submit']")
submit.click()