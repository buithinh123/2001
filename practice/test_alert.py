from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_open_practice_and_accept_alert( timeout=10):
    
    driver = webdriver.Chrome()
    driver.get("https://www.letskodeit.com/practice")

    # phóng to cửa sổ (với fallback nếu maximize không được hỗ trợ)
 
    driver.maximize_window()
    
    # chờ và click nút Alert
    alert_btn = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.ID, "alertbtn"))
    )
    alert_btn.click()
    sleep(3)
    # chờ alert xuất hiện rồi accept
    alert = WebDriverWait(driver, timeout).until(EC.alert_is_present())
    alert.accept()

    sleep(1)
    driver.quit()