from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DriverGet:
    def __init__(self,driver,url="https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf"):
        self.url=url
        self.driver=driver

    def driverGet(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#biletAramaForm > div:nth-child(3) > p:nth-child(4)")))

