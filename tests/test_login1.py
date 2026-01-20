from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
class TestLogin:
    @pytest
    def test_login_pass(self, driver):
                
        login_page = LoginPage(driver) 
        #driver.get(ConfigReader.get_base_url())
        sleep(5)
        login_page.login_page(ConfigReader.get_username(), ConfigReader.get_password())
       
        sleep(5)
        assert driver.find_element(By.CSS_SELECTOR,".oxd-text--h6").text =="Dashboard"
        
