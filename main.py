from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Mở trình duyệt và truy cập vào trang web
driver.get("http://127.0.0.1:5503/pages/login.html")

# Tìm và điền thông tin đăng nhập
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

username_input.send_keys("000000")
password_input.send_keys("123456a")

# Nhấp vào nút đăng nhập
login_button.click()

# Kiểm tra xem có lỗi đăng nhập hay không
error_message = driver.find_element(By.ID, "login-error")
error_text = error_message.text
print("Error message:", error_text)  # In ra thông báo lỗi để kiểm tra

# Đóng trình duyệt
driver.quit()
