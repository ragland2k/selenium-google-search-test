from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search box and enter a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Clootrack QA Internship")
search_box.send_keys(Keys.RETURN)

# Wait for results
time.sleep(3)

# Verify title contains search keyword
assert "Clootrack QA Internship" in driver.title

# Close the browser
driver.quit()
