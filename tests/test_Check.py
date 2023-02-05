import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage


"""def test_one():
    path = "C:/Users/ls217/PycharmProjects/PythonTestFramework/Driver/chromedriver latest.exe"
    driver = webdriver.Chrome(service=Service(executable_path=path))
    driver.get("https://hrms.orangetechnolab.com/Elsner/Login_Comm1.aspx")
    time.sleep(10)
    print("Hello Py_test")
"""


"""@pytest.fixture(params=HomePageData.test_HomePage_data)
def getData(request):
    return request.param

def test_formSubmission(getData):
    print("first name is "+getData["firstname"])
    print(type(getData))
    print(getData)"""

print("dfdf")

import pytest


@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


def test_data(data_set):
    print(type(data_set))
    pass

def test_test1():
    print("psss")

