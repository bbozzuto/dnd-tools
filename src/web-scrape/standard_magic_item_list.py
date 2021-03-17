from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

class standard_magic_item_list():
    def __init__(self):
        """ load the main D&D log on page and give the user 30 seconds to log on, then go to the magic item page for
        Xanathar's guide"""
        print("Starting Browser")
        self.driver = Chrome()
        self.driver.get("https://www.dndbeyond.com")
        time.sleep(30)
        self.driver.get("https://www.dndbeyond.com/sources/xgte/magic-item-tables")



if __name__ == "__main__":
    list = standard_magic_item_list()


