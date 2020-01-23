# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

import time
import Mail

def driverSetting():
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver=webdriver.Chrome(options=chrome_options)
    driverGet(driver)

def driverGet(driver):
    driver.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#biletAramaForm > div:nth-child(3) > p:nth-child(4)")))
    test1=driver.find_element_by_css_selector("#nereden")
    test1.clear()
    test1.send_keys("Arifiye")
    test2=driver.find_element_by_css_selector("#nereye")
    test2.clear()
    test2.send_keys("Esk")
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/ul[2]/li/a")))
    ActionChains(driver).move_to_element(element).perform()
    element.click()
    time.sleep(2)
    tarih=driver.find_element_by_css_selector("#trCalGid_input")
    tarih.clear()
    tarih.send_keys("25.01.2020")
    button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div/form/div[3]/p[3]/button/span")))
    driver.execute_script("arguments[0].click();", button)
    sayfaKontrol(driver)

def sayfaKontrol(driver):
    try:
        elem=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='mainTabView:gidisSeferTablosu:1:j_idt108:0:somVagonTipiGidis1_label']")))
        if elem != "":
            sayi = driver.find_element_by_css_selector('#mainTabView\:gidisSeferTablosu\:1\:j_idt108\:0\:somVagonTipiGidis1_label')
            if sayi.text[22] != '0':
                mail = Mail.Mail("mail@hotmail.com","Yer boşaldı "+sayi.text)
                mail.sendMail()
                print (sayi.text)
                exit()
            else:
                print("Yer Yok")
            driver.quit()
    except TimeoutException as ex:
        driverGet(driver)

if __name__=="__main__":
    while True:
        driverSetting()
        time.sleep(300)
