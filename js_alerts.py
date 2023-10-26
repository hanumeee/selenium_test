import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

#Browser Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the URL
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#Alert
driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button").click()
wait = WebDriverWait(driver, 10)
alert = wait.until(EC.alert_is_present())
time.sleep(3)
text = alert.text
print(text)
alert.accept()
time.sleep(5)

#Confirm Box
wait = WebDriverWait(driver, 10)
driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button").click()
wait.until(EC.alert_is_present())
alert2 = driver.switch_to.alert
time.sleep(3)
text2 = alert2.text
print(text2)
alert2.accept()
time.sleep(5)

#Prompt Box
wait = WebDriverWait(driver, 10)
driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(3) > button").click()
wait.until(EC.alert_is_present())
alert3 = driver.switch_to.alert
alert3.send_keys("Warning message")
time.sleep(3)
alert3.accept()
time.sleep(5)

# The Result
result_text = driver.find_element(By.ID, "result").text
print(result_text)

# Quit the WebDriver
driver.quit()
