from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep


def test_forward(driver):
    sleep(3)
    print(f"first title is: {driver.title}")
    driver.get("https://google.com")
    sleep(3)
    print(f"second title is: {driver.title}")
    driver.back()
    sleep(3)
    print(f"third title is: {driver.title}")
    driver.forward()
    sleep(3)
    print(f"four title is: {driver.title}")