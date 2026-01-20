import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="function")
def driver():
    # setup driver cho cac test script dung va set up 1 lan duy nhat
    option = Options()
    option.add_argument("--headless")
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    driver.maximize_window()
 
    url = ConfigReader.get_base_url()
    driver.get(url)
    yield driver
    # phan teardown cho moi test script
    driver.quit()
    