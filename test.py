
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_youtube = 'https://www.youtube.com/watch?v=b0z_dp5-luQ'

with Edge() as driver:
    driver.get(url_youtube)
    wait = WebDriverWait(driver, 7)
