from selenium import webdriver

import time

driver = webdriver.Chrome('H:/programowanie/Kurs_testy_automatyczne/pythonProject/fabrykaTestowPZ/chromedriver.exe')

url = 'https://google.pl'

driver.get(url)

#driver.get('https://google.pl')

serch_box = driver.find_element_by_name('q')

serch_box.send_keys('selenium python')

serch_box.submit()

time.sleep(5)

driver.quit()

driver.close()

#<input type='text' name='password_input' id='some_id' />

#element = driver.find_element_by_name('password_input')
#element1 = driver.find_element_by_name('some_id')
#elemnet2 = driver.find_element_by_xpath('//input[@id="some_id"]')