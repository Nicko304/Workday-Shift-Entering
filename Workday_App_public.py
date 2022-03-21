import selectors
import time
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

day = input("Please enter a date in the current payment period in the following format: WEEKDAY, NUMBER, MONTH YEAR (Ex: Tue, 22, March 2022). Only enter the first three letters for WEEKDAY: ")
start_time = input("Please enter the starting time of your shift (Ex: 4:19 PM): ")
end_time = input("Please enter the ending time of your shift (Ex: 4:20 PM): ")

#/////////// REQUIRED SETUP ///////////
driver = webdriver.Chrome("__________________________") # Fill in with appropriate path to your chromedriver file
# driver = webdriver.Chrome("C:\\Users\\Nicholas Schumacher\\Desktop\\WebDrivers\\chromedriver.exe") # Example with my computer (Windows)

#/////////// OPTIONAL SETUP ///////////
user_xpath = ' //*[@id="username"]'
pass_xpath = ' //*[@id="password"]'
signin_xpath = '//*[@id="loginform"]/div/button'
# OPTIONAL! You can have the program enter your credentials with the preferred route (you will still need to complete DUO 2FA yourself).
# Make sure to get rid of or comment on the three lines after the optional setup (there's conflicting variables).
# Route 1:
#### user = input("Enter in your username: ")
#### passcode = getpass("Enter your password: ") # Hides password on screen
# ------
# Route 2:
# user = "_____________"
# passcode = "_______________"
# ------
# Required for either route (just uncomment it):
# driver.find_element_by_xpath(user_xpath).send_keys(user)
# driver.find_element_by_xpath(pass_xpath).send_keys(passcode)
# driver.find_element_by_xpath(signin_xpath).click()

#/////////// SETUP COMPLETE ///////////


start = time.time()
SSO_Workday = 'https://wd5.myworkday.com/usc/d/home.htmld'


driver.maximize_window()
driver.get(SSO_Workday)
time.sleep(2)


wait = WebDriverWait(driver, 50)

# Clicks "Skip" button before going to the homepage.
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-automation-id="linkButton"]'))).click()

# Clicks "Time" button on Workday homepage
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Time"]'))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='My Calendar']"))).click()

time.sleep(3) # Part needs delay to prevent glitches

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Week']"))).click()
time.sleep(2) # Part needs delay to prevent glitches
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-automation-label="Day"]'))).click() # KEEP (WORKS) ALt Route than Actions ("Week" dropdown)

# Pick a desired day
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Change month and year"]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='" + day + "']"))).click()

# Open "Enter Time" menu
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@style = 'height: 100%; width: 100%; position: absolute; left: 0px; top: 0px;']"))).click()

# Input TIME IN and TIME OUT
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-automation-id='standaloneTimeWidget']"))).click()
time_in = driver.find_element_by_xpath("//input[@class='gwt-TextBox WLW2 WFX2']")
time_in.send_keys(start_time)
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='WGT']"))).click() # Allow entered time to auto-format
time.sleep(2) # Part needs delay to prevent glitches (Workday would delete the next input without it)
time_out = driver.find_element_by_xpath("//ul[@class='WAGG WJGG']//li[3]//input[@class='gwt-TextBox WLW2 WFX2']")
time_out.send_keys(end_time)
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='WGT']"))).click() # Allow entered time to auto-format
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='OK']"))).click()
