from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep

class TestForm:
    def test_login_form(self, driver):
        driver.get("https://the-internet.herokuapp.com/login")
        # chờ username và password hiển thị (timeout 10s)
        username = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        username.clear()
        username.send_keys("tomsmith")
        password.clear()
        password.send_keys("SuperSecretPassword!")
        # sử dụng submit() để gửi form
        password.submit()
        # chờ chuyển đến /secure và kiểm tra thông báo (timeout 10s)
        WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
        assert "/secure" in driver.current_url
        flash = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        ).text
        assert "You logged into a secure area!" in flash
