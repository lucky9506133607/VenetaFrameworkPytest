from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass

class MainProduct_ReactPage:

    def __init__(self, driver):
        self.driver = driver

    mainpdroduct_xpath = {"mainproduct": "//div[1]/div[2]/ul[1]/li[1]"}
    main_product = (By.XPATH, mainpdroduct_xpath["mainproduct"])

    def getHoneycombproduct(self):
        BaseClass_obj = BaseClass
        BaseClass_obj.verifyLinkPresence(self, self.mainpdroduct_xpath["mainproduct"])
        return self.driver.find_element(*MainProduct_ReactPage.main_product)
    
    





