import os
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas
from datetime import datetime
import dateutil.parser

chromedriver = "/Applications/chromedriver"  # chromedriver executable path
os.environ["webdriver.chrome.driver"] = chromedriver

# Start the session
session = requests.Session()

# Launch Selenium
driver = webdriver.Chrome(chromedriver)

# Try to get the desired page. Will redirect to login. This saves a ton of work!
driver.get("https://www.mapmyrun.com/routes/search")

# Pass login, get redirected to our desired page yay
elem = driver.find_element_by_name("email")
elem.send_keys("amandadavis2021@u.northwestern.edu")
elem = driver.find_element_by_name("password")
elem.send_keys("einersteiner")
elem.send_keys(Keys.RETURN)

# Need to wait for page to load, then adjust the inputs
# do better method below haha
time.sleep(5)

# Wait for page to load, then adjust the inputs
# timeout = 3
# try:
#     element_present = EC.presence_of_element_located((By.ID, 'main'))
#     WebDriverWait(driver, timeout).until(element_present)
# except TimeoutException:
#     print("Timed out waiting for page to load")
# finally:
#     print("Page loaded")

# # Change location to Chicago, IL [come back to this!]
# # Clear the placeholder
# driver.find_element_by_xpath('//*[@title="Clear value"]').click()
# # Find all the input elements on the page
# input_elements = driver.find_elements_by_css_selector('input')
# # Grab the second one
# elem = input_elements[1]
# # Fill in desired value
# elem.send_keys("Chicago, IL, USA" + Keys.TAB)

# Change to only running activities
driver.find_element_by_xpath("//select[@name='activityType']/option[text()='Run']").click()

# Remove 3 mile distance minimum
elem = driver.find_element_by_name("distanceMinimum")
elem.send_keys(Keys.BACK_SPACE, "0")

# Click search button (compound class, so select via css, replacing spaces with periods, don't forget 'button'!)
driver.find_element_by_css_selector("button.primary-xvWQU.button-2M08K.medium-3PyzS").click()

# Wait for page to load
time.sleep(10)

# Start grabbing the data
# Make soup :)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# Grab Distance, Name, City, & Date info from first 20 entries
run_table = pandas.read_html(str(soup.find_all('table')[0]))
# currently we have a list of dataframes, but we just want the one dataframe object
run_table = run_table[0]
# print(run_table[0])

time.sleep(5)

# Click 'next' button, continue with next 20 entries, repeat until desired date is reached
# xpath retrieved via inspection tool-- not great practice because small changes to HTML could throw this off
# Message: element click intercepted: Element <span>...</span> is not clickable at point (134, 601). Other element would receive the click: <div class="jss49">...</div>
# post used to figure out this ^ bug: https://stackoverflow.com/questions/11908249/debugging-element-is-not-clickable-at-point-error
next_button = driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div[1]/div[4]/a/span")
# possible better paths, try these later:
# next_button = driver.find_element_by_xpath("//span[text()='Next']")
# next_button = driver.find_element_by_xpath("//a[@class=‘pageLink-3961h’]/span")
# uncomment this if not using for loop! (below)
driver.execute_script("arguments[0].scrollIntoView()", next_button)
# next_button.click()

# Make sure new page loads
time.sleep(5)

# Loop to grab all our data

# initialize variables
num_rows = 0
current_date = datetime.date(datetime.now())
last_date = current_date

# loop through and get data
# while last_date.year == current_date.year:
#     next_button.click()
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     next_run_table = pandas.read_html(str(soup.find_all('table')[0]))
#     next_run_table = next_run_table[0]
#     run_table = run_table.append(next_run_table)
#     num_rows = len(run_table.index) - 1
#     last_date_string = run_table.iloc[num_rows][4]
#     # convert date string to datetime object
#     last_date = dateutil.parser.parse(last_date_string)
#     time.sleep(5)

# save the data
run_table.to_csv(r'runs_2020.csv', index=False)

# Close driver window
driver.quit()

