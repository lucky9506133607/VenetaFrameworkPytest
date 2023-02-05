from selenium.webdriver.common.by import By
import pandas as pd


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        

    design_btn = (By.XPATH, "//*[@id='shopify-section-header']/header/div/div/div[2]/a")

    def getMainProduct(self):
        return self.driver.find_element(*MainPage.design_btn)





