import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader
@pytest.fixture(scope="function")
def driver():
    # setup driver cho cac test script dung va set up 1 lan duy nhat
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    #url = "https://opensource-demo.orangehrmlive.com/"
    #driver.get(url)
    url = ConfigReader.get_base_url()
    driver.get(url)
    yield driver
    # phan teardown cho moi test script
    driver.quit()
    