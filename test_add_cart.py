from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")

# login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# add to cart
wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

# CHỜ badge xuất hiện
badge = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
)

assert badge.text == "1"

input("Add to cart done - Enter to close")
driver.quit()