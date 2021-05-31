import time
from selenium import webdriver

try:
    driver = webdriver.Chrome(executable_path='C:\\Users\\yuki\\Documents\\chromedriver.exe')
    driver.get('https://dev-gklp-thai-nimbus.kinto-mobility.jp/login')
    time.sleep(5)

finally:
    driver.quit()