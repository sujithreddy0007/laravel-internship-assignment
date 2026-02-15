from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://127.0.0.1:8000/login")

wait = WebDriverWait(driver, 10)

# Wait until password field appears
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))

# Generate random credentials
random_email = f"user{random.randint(1000,9999)}@test.com"
random_password = f"pass{random.randint(1000,9999)}"

# Find email field (type text or email)
email_field = driver.find_element(By.XPATH, "//input[@type='text' or @type='email']")
password_field = driver.find_element(By.XPATH, "//input[@type='password']")

# Fill fields
email_field.send_keys(random_email)
password_field.send_keys(random_password)

time.sleep(3)

driver.quit()
