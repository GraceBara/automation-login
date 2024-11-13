'''
automation of login
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Take user id and password as input from the user
user_id = input('Enter User Id for your Suno Account: ')  
password = input('Enter the password: ')

print(user_id)
print(password)

# Path to your ChromeDriver
cd = 'C:\\webdrivers\\chromedriver.exe'

# Initialize the browser
browser = webdriver.Chrome(cd)
browser.get('https://www.suno.com/')  # Open Suno.com

# Locate the user id field and enter the user_id
user_box = browser.find_element(By.ID, "alfagracebara@gmail.com")  
user_box.send_keys(user_id)

# Locate the password field and enter the password
password_box = browser.find_element(By.ID, "gracebara04")  
password_box.send_keys(password)

# Locate and click the login button
login_box = browser.find_element(By.ID, "Sign In")  
login_box.click()

