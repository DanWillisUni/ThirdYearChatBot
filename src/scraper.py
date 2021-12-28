from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time as t
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

s = Service('../resources/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://www.thetrainline.com")
trainline_page = driver.current_window_handle


def scrape_for_cheapets_ticket():
    return None


t.sleep(0.5)    # sleep to allow page to load in
# accept cookies on the page
driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

# what is the starting station
driver.find_element(By.ID, 'from.search').send_keys('Milton Keynes Central')

# what is the destination
driver.find_element(By.ID, 'to.search').send_keys('Norwich')


one_way = driver.find_element(By.ID, 'single')

returning = driver.find_element(By.ID, 'return')
returning.click()

"""
one way
"""
# date changing not working for outbound just yet
out_date = driver.find_element(By.ID, 'page.journeySearchForm.outbound.title')
out_date.click()
out_date.clear()
out_date.send_keys('150122')

# choosing leave by or arrive by time
out_leave_or_arrive = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/div[2]/div[4]/div/div/div[1]/section/form/div[3]/fieldset[1]/div[3]/div/select'))
out_depart_after = out_leave_or_arrive.select_by_value('departAfter')
out_leave_by = out_leave_or_arrive.select_by_value('arriveBefore')
out_leave_or_arrive.select_by_value('arriveBefore') # test

# select the hour of time
out_hour = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/div[2]/div[4]/div/div/div[1]/section/form/div[3]/fieldset[1]/div[4]/div[1]/select'))
out_hour.select_by_value('22')

# select minutes of time
out_min = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/div[2]/div[4]/div/div/div[1]/section/form/div[3]/fieldset[1]/div[4]/div[2]/select'))
out_min.select_by_value('45')



"""
return
"""
# inbound date
in_date = driver.find_element(By.ID, 'page.journeySearchForm.inbound.title')
in_date.click()
in_date.send_keys('150122')

# choosing leave by or arrive by time
in_leave_or_arrive = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/div[2]/div[4]/div/div/div[1]/section/form/div[3]/fieldset[2]/div[3]/div/select'))
in_depart_after = in_leave_or_arrive.select_by_value('departAfter')
in_leave_by = in_leave_or_arrive.select_by_value('arriveBefore')
in_leave_or_arrive.select_by_value('arriveBefore') # test

# select the hour of time
in_hour = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/div[2]/div[4]/div/div/div[1]/section/form/div[3]/fieldset[2]/div[4]/div[1]/select'))
in_hour.select_by_value('20')

# select minutes of time
in_min = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/div[2]/div[4]/div/div/div[1]/section/form/div[3]/fieldset[2]/div[4]/div[2]/select'))
in_min.select_by_value('45')

# enter number of adults and children in journey
driver.find_element(By.ID, 'passenger-summary-btn').click()
adults = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/div[2]/div[4]/div/div/div[1]/section/form/div[4]/div/div/div/div[1]/div/div/select'))
adults.select_by_value('3')
children = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/div[2]/div[4]/div/div/div[1]/section/form/div[4]/div/div/div/div[2]/div[1]/div/select'))
children.select_by_value('2')
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/div[2]/div[4]/div/div/div[1]/section/form/div[4]/div/div/button').click()


t.sleep(0.5)  # sleep to make sure all data has been entered
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/div[2]/div[4]/div/div/div[1]/section/form/div[5]/button').click()   # submit travel details to find cheapest price


# accept popup
t.sleep(3)
# print(driver.page_source.encode("utf-8"))
driver.find_element(By.CLASS_NAME, '_hsf37jx').click()

cheapest_ticket = driver.find_element(By.CSS_SELECTOR, "[aria-label='the cheapest fare']").text
print(cheapest_ticket)
print(driver.current_url)

t.sleep(500)
driver.quit()

"""
Testing
"""