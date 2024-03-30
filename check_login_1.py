from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Mở trình duyệt và truy cập vào trang web
driver.get("http://127.0.0.1:5503/pages/login.html")

# Điền thông tin đăng nhập
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("000000")
password_input.send_keys("123456a")

# Thực hiện đăng nhập bằng cách gửi form
login_form = driver.find_element(By.ID, "login-form")
login_form.submit()

# Kiểm tra xem đăng nhập có thành công hay không
welcome_message = driver.find_element(By.XPATH, "//h2[contains(text(),'Chào mừng')]")
assert welcome_message.is_displayed()

# Đóng trình duyệt
driver.quit()
