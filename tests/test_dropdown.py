from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from selenium.webdriver.support.ui import Select

def test_dropdown(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = driver.find_element(By.ID, "dropdown")
    select = Select(dropdown)
    select.select_by_visible_text("Option 1")
    
    sleep(5)
    select.select_by_value("2")
    sleep(5)
    select.select_by_index(1)
    sleep(5)
    
    