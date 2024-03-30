from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Mở trang web
driver.get("http://127.0.0.1:5503/pages/login.html")

# Tìm các phần tử trên trang đăng nhập
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Nhập dữ liệu đăng nhập
username_field.send_keys("000000")
password_field.send_keys("123456a")

# Nhấn nút đăng nhập
login_button.click()

# Đợi cho trang chuyển sau khi đăng nhập thành công
wait = WebDriverWait(driver, 20)
success_element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".success-message"))
)

# Kiểm tra xem đăng nhập có thành công hay không
if success_element:
    print("Đăng nhập thành công!")
else:
    print("Đăng nhập thất bại.")

# Đóng trình duyệt
driver.quit()
