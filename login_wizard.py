from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new Firefox WebDriver instance
browser = webdriver.Firefox()

# Open the Firefox browser (already done)

# Visit the specified webpage
url = "https://www.facebook.com"
browser.get(url)

# Input the username and password by Name attribute
username_input = browser.find_element(By.NAME, 'email')
password_input = browser.find_element(By.NAME, 'pass')

# Input your username and password here
username_input.send_keys('<email-username>')
password_input.send_keys('<password>')

# Locate and click the "Log in" button by NAME attribute
login_button = browser.find_element(By.NAME, 'login')
login_button.click()

# Keep the browser open until manually closed
while True:
    pass  # This loop will run indefinitely until manually terminated

# The browser will remain open until you manually close the script.
