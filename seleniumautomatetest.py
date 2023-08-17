from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Set options to disable GPU acceleration to avoid some potential issues
service = Service(executable_path='C:\\Users\\SSLTP11315\\Pictures\\chromedriver.exe')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
#chrome_driver_path='C:\\Users\\SSLTP11315\\Pictures\\chromedriver.exe'

# Create a new instance of the Chrome driver using WebDriver Manager
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the target website
url = 'https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Feu.primevideo.com%2Fregion%2Feu%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_t%3Dsg5jQ1UuWN-dWQrLmTZtvUI0UlizovRYRye-1zyBWlnE-AAAAAQAAAABk3HpkcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ%26location%3D%2Fregion%2Feu%2F%3Fref_%253Datv_auth_pre&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&openid.assoc_handle=amzn_prime_video_sso_in&openid.mode=checkid_setup&siteState=261-0231247-6849967&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'  # Replace with the actual URL
driver.get(url)

# Find the form elements and fill them out using By.NAME
input_element = driver.find_element(By.NAME, 'email')  # Replace with actual element name
input_element.send_keys('bala@gmail.com')

password_element = driver.find_element(By.NAME, 'password')  # Replace with actual element name
password_element.send_keys('123456789')

# Submit the form
submit_button = driver.find_element(By.CLASS_NAME, 'a-button-input')  # Replace with actual button name
submit_button.click()

# Close the browser window
driver.close()
