import unittest

import policy
from recursive_json_search import json_search
from test_data import data, key1, key2


class json_search_test(unittest.TestCase):
    def test_search_found(self):
        """Finds an existing key for an allowed role."""
        self.assertEqual(
            json_search(key1, data, role="viewer"),
            [{key1: "Network Device 10.10.20.82 Is Unreachable From Controller"}],
        )

    def test_search_not_found(self):
        """Returns an empty list when the key is absent."""
        self.assertEqual(json_search(key2, data, role="admin"), [])

    def test_is_a_list(self):
        """Always returns a list."""
        self.assertIsInstance(json_search(key1, data, role="viewer"), list)

    def test_viewer_cannot_read_apikey(self):
        """[SR-01] Denies protected fields to roles outside policy."""
        self.assertEqual(json_search("apiKey", data, role="viewer"), [])
        self.assertEqual(
            json_search("apiKey", data, role="admin"),
            [{"apiKey": "SNMP-COMMUNITY-STRING-7f3a9c"}],
        )

    def test_bad_role_is_denied(self):
        """[SR-02] Denies missing, unknown, case-mismatched, and non-string roles."""
        for bad_role in (None, "", "Admin", "guest", ["admin"]):
            self.assertEqual(json_search("hostname", data, role=bad_role), [])

    def test_parent_key_does_not_leak(self):
        """[SR-04] Redacts protected children from returned parent values."""
        result = json_search("deviceDetails", data, role="viewer")
        device_details = result[0]["deviceDetails"]

        self.assertEqual(len(result), 1)
        self.assertEqual(device_details["hostname"], "leaf2.abc.inc")
        self.assertNotIn("apiKey", device_details)
        self.assertNotIn("managementIpAddress", device_details)

    def test_no_traversal_into_protected_subtree(self):
        """[SR-04] Skips traversal inside protected subtrees denied to the role."""
        odd_data = {"apiKey": {"hidden": "secret"}, "visible": {"hidden": "ok"}}

        self.assertEqual(json_search("hidden", odd_data, role="viewer"), [{"hidden": "ok"}])

    def test_odd_json_does_not_crash(self):
        """[SR-05] Handles null, float, bool, and empty list values safely."""
        odd_data = {"items": [None, 1.25, True, [], {"target": False}]}

        self.assertEqual(json_search("target", odd_data, role="operator"), [{"target": False}])

    def test_too_deep_json_raises(self):
        """[SR-05] Raises ValueError when nesting depth exceeds 100."""
        too_deep = value = {}
        for _ in range(101):
            value["next"] = {}
            value = value["next"]

        with self.assertRaises(ValueError):
            json_search("missing", too_deep, role="admin")

    def test_result_is_a_copy(self):
        """[SR-06] Returns copies so callers cannot mutate source data."""
        result = json_search("deviceDetails", data, role="admin")
        result[0]["deviceDetails"]["hostname"] = "changed.example"

        original = json_search("hostname", data, role="admin")
        self.assertEqual(original, [{"hostname": "leaf2.abc.inc"}])

    def test_policy_change_at_runtime(self):
        """[SR-06] Keeps import-time policy permissions frozen."""
        policy.POLICY["apiKey"].append("viewer")
        try:
            self.assertEqual(json_search("apiKey", data, role="viewer"), [])
        finally:
            policy.POLICY["apiKey"].remove("viewer")


if __name__ == "__main__":
    unittest.main()
