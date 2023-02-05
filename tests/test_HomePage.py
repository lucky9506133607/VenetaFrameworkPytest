import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

#from TestData.HomePageData import HomePageData

from pageObjects.MainPage import MainPage
from pageObjects.mainproduct_ReactPage import MainProduct_ReactPage
from pageObjects.selectmaterial_ReactPage import selectmaterial_ReactPage
from pageObjects.subproduct_ReactPage import subproduct_ReactPage
from pageObjects.colour_ReactPage import colour_ReactPage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_chooseProduct(self):      #load fixture using getData parameter
        homepage= MainPage(self.driver)
        homepage.getMainProduct().click()

        mainproduct_obj = MainProduct_ReactPage(self.driver)
        mainproduct_obj.getHoneycombproduct().click()
        self.scrollbar("continue")

        subproduct_obj = subproduct_ReactPage(self.driver)
        Honeycomb_product_count = len(subproduct_obj.countSubProducts())
        print("total count =" + str(Honeycomb_product_count))

        if Honeycomb_product_count <= 6:
            for i in range(1, Honeycomb_product_count+1):
                print("for loop Working "+str(i))
                subproduct_obj.get_SubProduct(i).click()
                print(subproduct_obj.get_SubProductName(i).get_attribute("data-target-list-handle"))
                self.scrollbar("continue")

                #continua with here and also compare with skype file






        time.sleep(5)

        self.driver.refresh()

    #@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    """@pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param"""



