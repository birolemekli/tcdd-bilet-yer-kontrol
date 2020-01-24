# -*- coding: utf-8 -*-
"""
@author: Birol Emekli
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException,UnexpectedAlertPresentException
import sys
import Mail

class Control:
    def __init__(self,driver,time,email):
        self.driver=driver
        self.time=time
        self.email=email


    def sayfaKontrol(self):
        try:
            elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mainTabView:gidisSeferTablosu:1:j_idt108:0:somVagonTipiGidis1_label']")))
            if elem != "":
                for row in range(1, 15):
                    try:
                        if self.time == self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/form/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/table/tbody/tr[{0}]/td[1]/span'.format(row)).text:
                            message=self.driver.find_element_by_xpath('//*[@id="mainTabView:gidisSeferTablosu:{0}:j_idt108:0:somVagonTipiGidis1_label"]'.format(row - 1)).text
                            if message[22] != '0':
                                Mail.Mail(self.email, message).sendMail()
                                print(message)
                                return "successful"
                            else:
                                print("Aradığınız seferde boş yer yok...")
                                self.driver.quit()
                                return
                    except:
                        print ("Saatinizde hata var...")
                        self.driver.quit()
                        sys.exit()

            else:
                print("Aradığınız seferde boş yer yoktur...")
        except (TimeoutException,NoSuchElementException) as ex:
            print ("TCDD sitesi yüklemede bir hata meydana geldi... Tekrar deneniyor...")
            self.driver.quit()
        except UnexpectedAlertPresentException as ex1:
            print("Güzergah bilgilerinde hata meydana geldi. Kontrol ederek tekrar deneyiniz. İstasyonları doğru girdiğinizden emin olunuz")
            self.driver.quit()
            exit()