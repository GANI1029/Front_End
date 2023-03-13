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
######################---------------
from PerfectoLabUtils import PerfectoLabUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set your Perfecto Lab credentials here
user = "{your_username}"
password = "{your_password}"
host = "{your_cloud_url}"

# Set up the webdriver to run the tests
capabilities = {
    'platformName': 'iOS',
    'securityToken': '{}:{}'.format(user, password),
    'model': '{your_ios_device_model}',
    'browserName': 'mobileOS',
    'version': '{your_ios_version}',
    'automationName': 'XCUITest',
}

# Connect to the Perfecto Lab
driver = webdriver.Remote('https://' + host + '/nexperience/perfectomobile/wd/hub', capabilities)

# Navigate to the Messages app
driver.get('sms:')
# Wait for the Messages app to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "table")))

# Find the list of messages and print their contents
messages = driver.find_elements_by_xpath('//table[@id="table"]//div[@class="item-main-content"]/div[@class="message-text"]')
for message in messages:
    print(message.text)

# Close the driver
driver.quit()

