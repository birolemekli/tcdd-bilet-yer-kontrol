# -*- coding: utf-8 -*-
"""
@author: Birol Emekli
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

import time
class Rota:
    def __init__(self,driver,first_location,last_location,date):
        self.driver=driver
        self.first_location=first_location
        self.last_location=last_location
        self.date=date

    def dataInput(self):
        try:
            text1 = self.driver.find_element_by_css_selector("#nereden")
            text1.clear()
            text1.send_keys(self.first_location)
            time.sleep(0.3)
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/ul[1]/li/a")))
            ActionChains(self.driver).move_to_element(element).perform()
            element.click()
            text2 = self.driver.find_element_by_css_selector("#nereye")
            text2.clear()
            text2.send_keys(self.last_location)
            time.sleep(0.3)

            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/ul[2]/li/a")))
            ActionChains(self.driver).move_to_element(element).perform()
            element.click()
            time.sleep(0.3)
            date = self.driver.find_element_by_css_selector("#trCalGid_input")
            date.clear()
            date.send_keys(self.date)
            time.sleep(0.5)
            button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div/form/div[3]/p[3]/button/span")))

            self.driver.execute_script("arguments[0].click();", button)
        except:
            print ("Güzergah bilgilerinde hata meydana geldi. Kontrol ederek tekrar deneyiniz. İstasyonları doğru girdiğinizden emin olunuz")
            self.driver.quit()
            exit()