from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep

def test_hiden(driver):
    driver.get("https://www.letskodeit.com/practice")
    hiden_button = driver.find_element(By.ID, "hide-textbox")
    show_button= driver.find_element(By.ID, "show-textbox")
    displayed_textbox = driver.find_element(By.ID, "displayed-text")
    #sleep(5)
    displayed_textbox.send_keys("HAHAHAHA")# gui hahahaha vao textbox
    sleep(4)
    hiden_button.click()                    # click hide de an textbox
    driver.execute_script("arguments[0].value='hello word'", displayed_textbox ) # nhap gia tri chuoi moi
    sleep(4)
    show_button.click()                     # click show de hien textbox
    sleep(4)
    displayed_textbox.screenshot("displayed textbox.png")
    driver.save_screenshot("man hinh.png")
    
    