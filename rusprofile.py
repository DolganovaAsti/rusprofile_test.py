import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service(r"C:\Users\chern\PycharmProjects\python_selenium\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
base_url = 'https://www.rusprofile.ru/'
driver.get(base_url)
button = driver.find_element(By.ID, "menu-personal-trigger")
button.click()

 # Задержка, чтобы дать странице время для обработки клика
time.sleep(2)

 # Ввод значения в поле ввода
input_email = driver.find_element(By.XPATH, "//*[@id='v-root']/div/div[1]/div[3]/div[2]/div/input")
input_email.send_keys("QA@yandex.ru")
time.sleep(1)
input_password = driver.find_element(By.XPATH, "//*[@id='v-root']/div/div[1]/div[3]/div[3]/div/input")
input_password.send_keys("123456")
time.sleep(1)
show_password_button = driver.find_element(By.XPATH, "//*[@id='v-root']/div/div[1]/div[3]/div[3]/div/button")
show_password_button.click()
time.sleep(1)
log_in_button = driver.find_element(By.XPATH, "//*[@id='v-root']/div/div[1]/div[3]/div[4]/button")
log_in_button.click()
time.sleep(1)
registration_button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[3]/div[6]/a")
registration_button.click()
time.sleep(3)
input_user_name = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[3]/div[2]/div/input")
input_user_name.send_keys("Анастасия")
time.sleep(1)
input_password = driver.find_element(By.XPATH, "//*[@id='v-root']/div/div[1]/div[3]/div[4]/div[1]/input")
input_password.send_keys("123456QA")
time.sleep(1)
show_password_button = driver.find_element(By.XPATH, "//*[@id='v-root']/div/div[1]/div[3]/div[4]/div[1]/button")
show_password_button.click()
time.sleep(1)
checkbox = driver.find_element(By.XPATH, '//input[@class="checkbox"]')
checkbox.click()
time.sleep(3)


