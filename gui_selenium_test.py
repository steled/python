from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

CHROMEDRIVER_BIN = "C:/Program Files/Python36/selenium/webdriver/chrome/chromedriver.exe"

browser = webdriver.Chrome(CHROMEDRIVER_BIN)
root = Tk()

root.title("Nur ein Fenster")

Label(root, text="Username").grid(row=0, column=0)
username = Entry(root)
username.grid(row=0, column=1)

Label(root, text="Password").grid(row=1, column=0)
password = Entry(root, show="*")
password.grid(row=1, column=1)

def open():
#    messagebox.showinfo("Show Password", "Username: " + username.get() + "\nPassword: " + password.get())
    browser.get('https://www.facebook.com')
    browser.find_element_by_id('email').send_keys(username.get())
    #uname = browser.find_element_by_id('email')
    #uname.send_keys(username.get())
    browser.find_element_by_id('pass').send_keys(password.get())
    #pword = browser.find_element_by_id('pass')
    #pword.send_keys(password.get())
    browser.find_element_by_id('u_0_s').submit()
    #login = browser.find_element_by_id('u_0_s')
    #login.submit()
#    pw = StringVar()
#    Entry(root, textvariable=pw).grid(row=4, column=0)
#    pw.set(password.get())

def close():
    #logout = browser.find_element_by_id('userNavigationLabel')
    browser.find_element_by_id('userNavigationLabel').click()
    #logout.click()
    WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, 'show_me_how_logout_1')))
    #time.sleep(2)
    browser.find_element_by_id('show_me_how_logout_1').submit()
    WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, 'u_0_s')))
    #time.sleep(2)
    browser.quit()
    root.quit()

Button(root, text="OK", command=open).grid(row=2, column=0)
Button(root, text="Beenden", command=close).grid(row=2, column=1)
#Button(root, text="Beenden", command=root.quit).grid(row=2, column=1)

root.mainloop()
