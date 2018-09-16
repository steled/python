import time

from selenium import webdriver

CHROMEDRIVER_BIN = "C:/Program Files/Python36/selenium/webdriver/chrome/chromedriver.exe"

browser = webdriver.Chrome(CHROMEDRIVER_BIN)

browser.get('http://www.google.de')
#browser.get('https://www.facebook.com')

search_box = browser.find_element_by_name('q') # Find the search box
#search_box = browser.find_element_by_id('loginbutton')
search_box.send_keys('ChromeDriver')
search_box.submit()

time.sleep(5) # Let the user actually see something!

browser.quit()
