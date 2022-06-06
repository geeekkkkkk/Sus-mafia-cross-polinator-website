from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome("/home/shivam/Downloads/chromedriver")
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

username = driver.find_element_by_id("username")
username.send_keys("")
pword = driver.find_element_by_id("password")
pword.send_keys("")		
driver.find_element_by_xpath("//button[@type='submit']").click()

profile_url = "https://www.linkedin.com/in/shivam-batra-s18213b/"

driver.get(profile_url)

start = time.time()

initialScroll = 0
finalScroll = 1000

while True:
	driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
	initialScroll = finalScroll
	finalScroll += 1000
	time.sleep(3)

	end = time.time()
	if round(end - start) > 20:
		break
















