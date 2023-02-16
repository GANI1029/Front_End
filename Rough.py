from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up options for the Edge browser
options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_argument("headless")

# Set the path to the Edge driver executable
driver_path = 'C:\\path\\to\\msedgedriver.exe'

# Set up the Edge driver service
service = Service(driver_path)

# Set up the Edge driver
driver = webdriver.Edge(service=service, options=options)

# Open the URL in the browser
url = "https://www.example.com/login"
driver.get(url)

# Wait for the username input field to become visible
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
)

# Enter the username value
username_field.send_keys("myusername")

# Wait for the password input field to become visible
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
)

# Enter the password value
password_field.send_keys("mypassword")

# Submit the login form
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='submit']"))
)
login_button.click()

# Take a screenshot of the logged-in homepage
driver.save_screenshot("homepage.png")

# Close the browser
driver.quit()
