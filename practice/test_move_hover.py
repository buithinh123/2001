from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def test_hover_main_item2(timeout=10):
 
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.demoqa.com/menu")
        driver.implicitly_wait(20)

        # phóng to cửa sổ với fallback
        try:
            driver.maximize_window()
        except Exception:
            try:
                driver.set_window_size(1280, 800)
            except Exception:
                pass

        # chờ element hiển thị rồi hover
        locator = (By.XPATH, "//a[normalize-space()='Main Item 2']")
        el = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        ActionChains(driver).move_to_element(el).perform()

        # dừng 3s để quan sát
        sleep(3)
    finally:
        driver.quit()

