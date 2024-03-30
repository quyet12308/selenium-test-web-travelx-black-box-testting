import datetime
import pytz
import json


def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return t


def write_to_file_7(filename, result):
    content = {"time": gettime2(), "result": result}
    content_str = json.dumps(content, ensure_ascii=False)
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content_str + "\n")
