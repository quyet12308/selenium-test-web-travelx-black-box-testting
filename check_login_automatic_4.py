from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(username, password, url):
    # Khởi tạo trình duyệt
    driver = webdriver.Chrome()

    # Mở trang web
    driver.get(url)

    # Tìm các phần tử trên trang đăng nhập
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Nhập dữ liệu đăng nhập
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Nhấn nút đăng nhập
    login_button.click()

    # Kiểm tra xem có lỗi đăng nhập hay không
    error_message = driver.find_element(By.ID, "login-error")
    error_text = error_message.text
    print("Error message:", error_text)  # In ra thông báo lỗi để kiểm tra
    result = ""
    print(error_text)
    if error_text == "":
        # Đợi cho alert hiển thị
        wait = WebDriverWait(driver, 20)
        alert = wait.until(EC.alert_is_present())

        # Lấy nội dung của alert
        alert_text = alert.text

        # Kiểm tra kết quả đăng nhập dựa trên nội dung của alert
        if "Logged in successfully" in alert_text:
            result = "Đăng nhập thành công!"
        else:
            result = f"Lỗi: {alert_text}"
        # Chấp nhận alert
        alert.accept()

    else:
        result = error_text
    # Đóng trình duyệt
    driver.quit()

    return result


# Sử dụng hàm test_login
url = "http://127.0.0.1:5503/pages/login.html"
username = "000000"
password = "123456a"
login_result = test_login(username, password, url)
print(login_result)
