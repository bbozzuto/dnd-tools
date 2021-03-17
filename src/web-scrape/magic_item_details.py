from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


class item_details():
    def __init__(self):
        # just load the belt of dwarven kind and try to get the details
        # Chrome(executable_path="/opt/WebDriver/bin/chromedriver")
        print("Starting Browser")
        self.driver = Chrome()
        self.driver.get("https://www.dndbeyond.com/magic-items/belt-of-dwarvenkind")

        self.details = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'item-info')]")))
        print(self.details)
        value = self.driver.find_element_by_xpath("//div[contains(@class, 'item-info')]").text
        print(value)
        print("Closing Browser")
        self.driver.quit()

def parse_item_details(text):
    values = {}
    comma_location = text.find(",")
    if comma_location > -1:
        values['Type']

if __name__ == "__main__":
    my_item = item_details()
