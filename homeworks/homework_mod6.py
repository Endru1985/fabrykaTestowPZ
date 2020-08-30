from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'https://fabrykatestow.pl'

driver.get(url)
driver.maximize_window()

link = driver.find_element_by_xpath('//*[@id="menu-item-506"]/a')
link.click()

scroll = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/section[8]/div/div/div/div/div/div/div/h2')
driver.execute_script('arguments[0].scrollIntoView();', scroll)

driver.save_screenshot('screenshot.png')


driver.quit()