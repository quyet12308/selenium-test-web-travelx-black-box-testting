from check_login_automatic_4 import test_login
from write_logs import *

url = "http://127.0.0.1:5503/pages/login.html"
# username = "000000"
# password = "123456a"
# login_result = test_login(username, password, url)
# print(login_result)

test_cases = {
    "dang_nhap_thanh_cong": {"user_name": "000000", "password": "123456a"},
    "sai_mat_khau": {"user_name": "000000", "password": "123456aa"},
    "username_khong_du_6_ky_tu": {"user_name": "abc12", "password": "123456a"},
    "username_hon_6_ky_tu": {"user_name": "1234567", "password": "123456a"},
    "username_co_ky_tu_dac_biet": {"user_name": "@123#$%", "password": "123456a"},
    "password_khong_du_6_ky_tu": {"user_name": "000000", "password": "12345"},
    "password_hon_6_ky_tu": {"user_name": "000000", "password": "1234567aa"},
    "password_khong_bao_gom_chu": {"user_name": "000000", "password": "123456"},
    "password_khong_bao_gom_so": {"user_name": "000000", "password": "abcdef"},
    "password_bao_gom_ca_ky_tu_dac_biet": {
        "user_name": "000000",
        "password": "123456a@$",
    },
    "username_chua_dang_ky": {"user_name": "chuadangky", "password": "000000a"},
    "khong_co_user_name": {"user_name": "", "password": "123456a"},
    "password_rong": {"user_name": "000000", "password": ""},
}

# print(len(test_cases))
for i in test_cases:
    # print(i)
    test_case_data = test_cases[i]
    result_test_login = test_login(
        url=url,
        username=test_case_data["user_name"],
        password=test_case_data["password"],
    )
    print(result_test_login)
    write_to_file_7(
        filename="text_folders/check_login_automatic_with_selenium_version_4.txt",
        result=f"testcase: {i} , result : {result_test_login}",
    )


# test_case1 = test_cases["dang_nhap_thanh_cong"]
# print(test_case1)
