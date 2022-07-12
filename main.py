# -*- coding: utf-8 -*-
"""
@author: Birol Emekli
"""
import DriverSetting,DriverGet,Rota,Control,Help
import sys
import time
date=[]
timee=[]
n=0
def driverSetting():
    return DriverSetting.DriverSetting().driverUP()

def driverGet(driver):
    DriverGet.DriverGet(driver).driverGet()

def rota(driver,first_location,last_location,date):
    Rota.Rota(driver, first_location, last_location, date).dataInput()

def control(driver,timee,email):
    response=Control.Control(driver,timee,email).sayfaKontrol(timee)
    if response=="successful":
       #driver.quit()
       # sys.exit()
       print("bulundu")
       return True
    return False
if __name__=="__main__":
    email= input("lutfen eposta adresinizi giriniz:")
    first_location = input("Biniş yerinizi giriniz. Ör:Ankara Gar \n ")
    last_location = input("İniş yerinizi giriniz. Ör:İstanbul(Söğütlü Ç.)\n")
    n = int(input(" Kaç adet seferde bilet aramak istiyorsunuz? \n"))
    
    for i in range(n):
        print(f"{i+1} . sefer icin:")
        date.append(input("Gideceğiniz günü giriniz. Ör:18.07.2021 \n"))
        timee.append(input("Saati giriniz. Ör:15:00\n"))
    
    isFound = False
    while isFound == False:
    	for i in range(n):
            print( "\n\n"+date[i] + " tarihli " +timee[i] +" treni kontrol ediliyor")
            driver=driverSetting()
            driver.set_window_size(1, 1)
            driver.minimize_window()
            driverGet(driver)
            
            rota(driver,first_location,last_location,date[i])
            isFound=control(driver,timee[i],email)
            driver.quit()
            time.sleep(1)


