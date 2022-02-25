import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This is the parent class of all pages"""
# It contains all the utilities for all pages


class BasePage:
    """Initiate the web driver"""
    def __init__(self, driver):
        self.driver = driver

    """This method helps to click on elements by locators"""
    def do_click(self,locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator)).click()
        time.sleep(1)

    """This method helps to send data to input fields by locators"""
    def do_send_keys(self,locator,value):
        textbox = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))

        """Checking whether the input box is empty or
        contains any value, if contains then it will clear the field"""
        try:
            textbox.clear()
            textbox.send_keys(value)
        except:
            textbox.send_keys(value)

        time.sleep(1)

    """This function helps to select items from dropdown list"""
    def do_select(self,locator, index):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator)).click()
        elements = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)))
        """I have just selected the values by index"""
        elements.select_by_index(index)
        time.sleep(1)

    """This function helps to hover over items
    and select the subitems which are arranged as drop down"""
    def do_hover(self, locator, sublocator):
        action = ActionChains(self.driver)
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        action.move_to_element(elem).perform()
        sub_elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(sublocator))
        action.move_to_element(sub_elem).click().perform()
        time.sleep(1)

    """This function helps to click the element 
    when it becomes free to click"""
    def do_clickable(self,locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()
        time.sleep(1)