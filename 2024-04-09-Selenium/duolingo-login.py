from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website for login
driver.get("https://www.duolingo.com/?isLoggingIn=true")

# Click on "Already have an account" button
alreadyHaveAccount = driver.find_element(By.XPATH, "//button[@data-test='have-account']")
alreadyHaveAccount.click()

# Find the username and password input fields
username_input = driver.find_element(By.ID, "web-ui1")
password_input = driver.find_element(By.ID, "web-ui2")

# Enter username and password
username_input.send_keys("your_username")
password_input.send_keys("your_password")

# Find and click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for a while
time.sleep(5)
