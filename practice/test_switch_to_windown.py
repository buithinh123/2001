from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep

def test_open_and_switch_to_new_window(timeout=10):
    """
    Mở url, click nút 'Open Window', switch sang cửa sổ mới và maximize cửa sổ đó.
    Trả về handle của cửa sổ mới.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.letskodeit.com/practice")

    # lưu handles trước khi mở cửa sổ mới
    before_handles = list(driver.window_handles)

    # chờ và click nút "Open Window"
    open_btn = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.ID, "openwindow"))
    )
    open_btn.click()

    # chờ cửa sổ mới được mở
    WebDriverWait(driver, timeout).until(EC.new_window_is_opened(before_handles))

    # tìm handle mới và chuyển sang cửa sổ đó
    new_handles = [h for h in driver.window_handles if h not in before_handles]
    if not new_handles:
        raise AssertionError("Không tìm thấy cửa sổ mới sau khi click 'Open Window'")
    new_handle = new_handles[0]
    driver.switch_to.window(new_handle)

    # phóng to cửa sổ; fallback nếu driver không hỗ trợ maximize
    try:
        driver.maximize_window()
    except Exception:
        try:
            driver.set_window_size(1280, 800)
        except Exception:
            pass

    # chờ trang load xong
    WebDriverWait(driver, timeout).until(lambda d: d.execute_script("return document.readyState") == "complete")
    sleep(5)