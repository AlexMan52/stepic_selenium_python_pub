# time.sleep(3) - bad maintenance and scaling

# browser.implicitly_wait(5) - checking for every next element every 500ms until 5 secs

# explicit wait - with conditions. Need to import:
#   from selenium.webdriver.support.ui import WebDriverWait
#   from selenium.webdriver.support import expected_conditions as EC

# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions - link

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'
driver = webdriver.Chrome()
#driver.implicitly_wait(5)  -- #2

try:
    driver.get(link)
    #driver.find_element(By.ID, "button")

    #3:
    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    driver.find_element(By.ID, 'book').click()

    x = driver.find_element(By.ID, "input_value").text  # always apply .text to get not the element but the value
    result = math.log(abs(12 * math.sin(int(x))))
    field = driver.find_element(By.ID, "answer")
    field.send_keys(result)
    driver.find_element(By.ID, "solve").click()
    alert = driver.switch_to.alert
    print(alert.text)


finally:
    #time.sleep(3)  -- #1
    driver.quit()