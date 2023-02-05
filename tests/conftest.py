import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        #driver = webdriver.Chrome(service=Service(executable_path="C:\\chromedriver.exe"))

        driver = webdriver.Chrome(service=Service(executable_path="C:/Users/ls217/PycharmProjects/PythonTestFramework/Driver/chromedriver latest.exe"))

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://venetablinds.com.au/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

