from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




import time

import requests
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https://www.thesparksfoundationsingapore.org/")


print("\n \n************** Let's Check For The TestCases *********************\n")

########################## TestCase 1:Title ###############################
print("TestCase #1:")
if(driver.title):
    print("Title Verification Successful: ",driver.title)
else:
    print("Title Verification Failed!\n")
time.sleep(3)
print("")


########################## TestCase 2:Home button #########################
print("TestCase #2:")
try:
    # Wait for the element to be present
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "The Sparks Foundation"))
)
    
    print("Home link works!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")
time.sleep(3)

########################## TestCase 3:Check if navbar appears #########################
print("TestCase #3:")
try:
    element = driver.find_element(By.CLASS_NAME, 'navbar')

    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")
time.sleep(3)

######################## TestCase 4:Scrolling down ########################################
print("TestCase #4:")
for i in range(0,1500,200):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)
print("scrolled down")

###################### TestCase 5:scrolling up ######################################
print("TestCase #5:")
element = driver.find_element(By.CSS_SELECTOR, '#toTopHover')
element.click()



time.sleep(1)
print("scrolled up")
print("")


########################## TestCase 6:About Us Page #########################
print("TestCase #6:")
try:
    driver.find_element(By.PARTIAL_LINK_TEXT, 'About').click()

    time.sleep(3)

    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)


########################## TestCase 7:Policies and Code #########################
print('TestCase #7:')
try:
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Policies and Code').click()

    time.sleep(3)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Policies').click()

    time.sleep(3)
    print('Policy page exists. Success!\n')
except NoSuchElementException:
    print('Policy Page Does not exist. Failed!\n')
    time.sleep(3)


########################## TestCase 8:Workshop page #########################
print('TestCase #8:')
try:
    driver.find_element(By.PARTIAL_LINK_TEXT,'Programs').click()
    time.sleep(3)
    driver.find_element(By.PARTIAL_LINK_TEXT,'Workshops').click()
    time.sleep(3)
    driver.find_element(By.PARTIAL_LINK_TEXT,'LEARN MORE').click()
    time.sleep(3)
    print('Workshop Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')


########################## TestCase 9: Check If Logo Exists #########################
print('TestCase #9:')
try:
    driver.find_element(By.CSS_SELECTOR, '#home div div:nth-child(1) h1 a').click()

    print('Found Logo! Success!\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo found!\n')

time.sleep(4)
driver.switch_to.window(driver.window_handles[0])
print("switched to 1st Tab\n")
time.sleep(1.5)

########################## TestCase 10:Check the Form #########################
print("TestCase #10:")
try:
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Join Us').click()

    time.sleep(3)
    driver.find_element(By.PARTIAL_LINK_TEXT,'Why Join Us').click()
    time.sleep(3)
    print("Typing your name...")
    driver.find_element(By.CSS_SELECTOR, 'input[name="Name"]').send_keys('Suwathi')

    time.sleep(3)
    print("Typing your Email address...")
    driver.find_element(By.CSS_SELECTOR, 'input[name="Email"]').send_keys('Suwathi123@gmail.com')

    time.sleep(3)
    select =Select(driver.find_element(By.CSS_SELECTOR, '.form-control'))

    time.sleep(3)
    select.select_by_visible_text('Student')
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '.button-w3layouts').click()

    time.sleep(3)
    print("Form Verification Successful!\n")
    print("successfully the Automated testing of TSF website is done!\n")
    time.sleep(3)
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)
