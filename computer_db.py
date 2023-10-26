from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Navigate to URL
driver.get("https://computer-database.gatling.io/computers")

#Add a new computer
driver.find_element(By.XPATH, "//a[@id='add']").click()
time.sleep(3)
driver.find_element(By.ID, "name").send_keys("Asus ROG FLOW X13")
time.sleep(3)
driver.find_element(By.ID, "introduced").send_keys("2023-10-25")
time.sleep(3)
driver.find_element(By.ID, "discontinued").send_keys("2023-11-10")
time.sleep(3)
driver.find_element(By.ID, "company").click()
time.sleep(3)
driver.find_element(By.XPATH, "//option[@value='1']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@value='Create this computer']").click()

#Search by Filter
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='searchbox']").send_keys("ACE")
time.sleep(3)
driver.find_element(By.XPATH, "// input[ @ id = 'searchsubmit']").click()
time.sleep(3)

#Quit the WebDriver
driver.close()
driver.quit()