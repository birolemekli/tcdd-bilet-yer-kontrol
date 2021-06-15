# -*- coding: utf-8 -*-
"""
@author: Birol Emekli
"""
import DriverSetting,DriverGet,Rota,Control,Help
import sys
import time

def driverSetting():
    return DriverSetting.DriverSetting().driverUP()

def driverGet(driver):
    DriverGet.DriverGet(driver).driverGet()

def rota(driver,first_location,last_location,date):
    Rota.Rota(driver, first_location, last_location, date).dataInput()

def control(driver,timee,email):
    response=Control.Control(driver,timee,email).sayfaKontrol()
    if response=="successful":
        driver.quit()
        sys.exit()

if __name__=="__main__":
    if str(sys.argv[1])=="--h":
        Help.Help()
    else:
        first_location = input("Biniş yerinizi giriniz. Ör:Ankara Gar\n")
        last_location = input("İniş yerinizi giriniz. Ör:İstanbul(Pendik)\n")
        date = input("Gideceğiniz günü giriniz. Ör:18.07.2021\n")
        timee = input("Saati giriniz. Ör:15:00\n")
        email= str(sys.argv[1])
        while True:
            driver=driverSetting()
            driverGet(driver)
            rota(driver,first_location,last_location,date)
            control(driver,timee,email)
            time.sleep(300)
