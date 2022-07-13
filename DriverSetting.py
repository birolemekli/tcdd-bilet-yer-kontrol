# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DriverSetting:
    def driverUP(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        #driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver
