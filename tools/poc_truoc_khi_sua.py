import inspect
import os
import sys

sys.path.insert(0, os.getcwd())    # lấy code ở thư mục đang đứng

from recursive_json_search import json_search
from test_data import data

has_role = "role" in inspect.signature(json_search).parameters


def call(key, obj):
    # code YC4 chưa có tham số role, code YC5 thì gọi với tư cách viewer
    if has_role:
        return json_search(key, obj, role="viewer")
    return json_search(key, obj)


def show(label, func):
    try:
        result = func()
    except Exception as e:
        result = f"{type(e).__name__}: {e}"
    print(label, result)


deep = node = {}
for _ in range(5000):
    node["child"] = {}
    node = node["child"]

print("Hàm có tham số role:", has_role)
show("1) viewer đọc apiKey:", lambda: call("apiKey", data))
show("2) tìm deviceDetails có lộ apiKey?",
     lambda: "SNMP-COMMUNITY" in str(call("deviceDetails", data)))
show("3) mảng chứa null:", lambda: call("x", {"a": [None]}))
show("4) mảng chứa số thực:", lambda: call("x", {"a": [1.5]}))
show("5) JSON lồng 5000 cấp:", lambda: call("x", deep))
