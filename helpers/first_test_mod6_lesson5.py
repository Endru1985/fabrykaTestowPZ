#funkcje wspomagające

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from helpers.DataGenerator import DataGenerator

def hover_over_element(driver_instance, xpath):
    elem = driver_instance.find_element_by_xpatch(xpath)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()

def wait_for_visibility_of_element(driver_instance, xpath, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH,xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element(inv_driver_instance, xpath, time_to_wait=8):
    inv_element = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located(By.XPATH,xpath))
    return inv_element