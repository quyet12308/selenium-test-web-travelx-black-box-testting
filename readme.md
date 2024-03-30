# Dự án test hộp đen cho web travelx bằng selenium

## Đầu tiên nếu chưa có dự án travelx thì có thể lấy nó ở đây:
[Link backend](https://github.com/quyet12308/travelx_backend_micro_services)
[Link frontend](https://github.com/quyet12308/fontend-travelx-microservices)

## Sau khi có dự án rồi thì khởi chạy dự án theo các hướng dẫn của backend và fontend

## Chạy dự án blackbox testing
```cmd
python check_login_automatic_with_testcases.py
```

## Note cấu trúc dự án 
- write_logs.py chứa các hàm để ghi lại log khi chạy quá trình test 
- check_login_automatic_with_testcases.py chứa file chính để test dự án (với chức năng login)
    - Trong file này co test_cases là các trường hợp kiểm thử được xây dựng sẵn 
    - url là địa chỉ đến web muốn kiểm thử
    - thuộc tính filename của hàm write_to_file_7 là nơi lưu chữ log của quá trình test
- text_folders là nơi lưu chữ log của quá trình test . 