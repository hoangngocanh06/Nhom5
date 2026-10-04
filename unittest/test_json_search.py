import copy
import unittest

import policy
from recursive_json_search import *
from test_data import *

SNMP_KEY = "SNMP-COMMUNITY-STRING-7f3a9c"    # giá trị apiKey trong test_data.py
MGMT_IP = "10.10.20.21"                      # giá trị managementIpAddress


class json_search_test(unittest.TestCase):
    '''test module to test search function in `recursive_json_search.py`'''

    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([] != json_search(key1, data, role="viewer"))

    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([] == json_search(key2, data, role="admin"))

    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1, data, role="viewer"), list)
        self.assertIsInstance(json_search(key1, data), list)

    # ---- security test ----

    def test_viewer_cannot_read_apikey(self):
        '''[SR-01] viewer không đọc được apiKey, admin thì đọc được'''
        viewer = json_search("apiKey", data, role="viewer")
        admin = json_search("apiKey", data, role="admin")
        self.assertEqual([], viewer)
        self.assertEqual([{"apiKey": SNMP_KEY}], admin)

    def test_policy_matrix(self):
        '''[SR-01] mọi cặp trường và role đều đúng như policy.py'''
        for field, allowed in policy.POLICY.items():
            for role in ("admin", "operator", "viewer"):
                with self.subTest(field=field, role=role):
                    result = json_search(field, data, role=role)
                    if role in allowed:
                        self.assertNotEqual([], result)
                    else:
                        self.assertEqual([], result)

    def test_bad_role_is_denied(self):
        '''[SR-02] thiếu role hoặc role lạ thì không trả về gì'''
        bad_roles = [None, "", "guest", "Admin", " admin", "adm",
                     ["admin"], 1, True]
        keys = list(policy.POLICY) + ["deviceDetails"]
        for role in bad_roles:
            for key in keys:
                with self.subTest(role=role, key=key):
                    self.assertEqual([], json_search(key, data, role=role))

    def test_parent_key_does_not_leak(self):
        '''[SR-04] tìm theo khóa cha không làm lộ trường nhạy cảm bên trong'''
        for parent in ("deviceDetails", "connectedDevice", "enrichmentInfo"):
            with self.subTest(parent=parent):
                viewer = str(json_search(parent, data, role="viewer"))
                operator = str(json_search(parent, data, role="operator"))
                self.assertIn("leaf2.abc.inc", viewer)
                self.assertNotIn(SNMP_KEY, viewer)
                self.assertNotIn(MGMT_IP, viewer)
                self.assertNotIn(SNMP_KEY, operator)
                self.assertIn(MGMT_IP, operator)

        # key nằm bên trong một trường bị cấm cũng không được tìm thấy
        hidden = {"apiKey": {"note": "bí mật"}}
        self.assertEqual([], json_search("note", hidden, role="viewer"))

    def test_odd_json_does_not_crash(self):
        '''[SR-05] JSON có null, số thực hoặc lồng quá sâu không làm sập hàm'''
        odd = {"a": [None, 1.5, True, "x", [], {}],
               "b": [[{"issueSummary": 2.5}]]}
        result = json_search("issueSummary", odd, role="viewer")
        self.assertEqual([{"issueSummary": 2.5}], result)

        for value in (None, 42, 3.14, "issueSummary"):
            result = json_search("issueSummary", value, role="viewer")
            self.assertEqual([], result)

        deep = node = {}
        for _ in range(5000):
            node["child"] = {}
            node = node["child"]
        with self.assertRaises(ValueError):
            json_search("issueSummary", deep, role="viewer")

    def test_result_is_a_copy(self):
        '''[SR-06] sửa kết quả trả về không làm đổi dữ liệu gốc'''
        before = copy.deepcopy(data)
        result = json_search("deviceDetails", data, role="admin")
        result[0]["deviceDetails"]["hostname"] = "bị sửa"
        self.assertEqual(before, data)

    def test_policy_change_at_runtime(self):
        '''[SR-06] sửa policy.POLICY lúc đang chạy không nới quyền'''
        policy.POLICY["apiKey"].append("viewer")
        try:
            self.assertEqual([], json_search("apiKey", data, role="viewer"))
        finally:
            policy.POLICY["apiKey"].remove("viewer")


if __name__ == '__main__':
    unittest.main()
