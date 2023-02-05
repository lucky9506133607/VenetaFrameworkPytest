from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender= (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):

        self.driver.find_element(*HomePage.shop).click()
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)


    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)


#optimized code
"""from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    form_elements = {
        'name': (By.CSS_SELECTOR, "[name='name']"),
        'email': (By.NAME, "email"),
        'check': (By.ID, "exampleCheck1"),
        'gender': (By.ID, "exampleFormControlSelect1"),
        'submit': (By.XPATH, "//input[@value='Submit']"),
        'success': (By.CSS_SELECTOR, "[class*='alert-success']")
    }

    def shopItems(self):
        self.driver.find_element(*self.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def get_element(self, element_name):
        return self.driver.find_element(*self.form_elements[element_name])"""

