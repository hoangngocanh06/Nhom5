# Agent log, phiên Codex 01a10926-b32a-7f02-905f-48b8638177c8

| Mục | Giá trị |
|---|---|
| File | rollout-2026-10-05T06-01-33-01a10926-b32a-7f02-905f-48b8638177c8.jsonl |
| Session | 01a10926-b32a-7f02-905f-48b8638177c8 |
| Thời gian | 2026-10-05 06:01:38 đến 06:21:07 |
| Thư mục | /home/chung-tra274/Nhom5 |
| Git lúc bắt đầu | ? @ ? |
| Mô hình | gpt-5.5, effort high |
| Approval policy | on-request |
| Sandbox | workspace-write |
| Mạng trong sandbox | False |
| Số prompt | 4 |
| Số lệnh agent chạy | 22 |
| Lệnh xin chạy ngoài sandbox | 0 |
| Số lần sửa file | 5 (/home/chung-tra274/Nhom5/git-intro/unittest/recursive_json_search.py, /home/chung-tra274/Nhom5/git-intro/unittest/test_json_search.py) |
| Token vào | 424371 |
| Token ra | 7900 |

Rollout không lưu các lần bấm Approve/Decline nên phần này ghi tay trong báo cáo.

## Diễn biến

### 06:01:39 Người dùng (prompt 1)

> # Context from my IDE setup:
> 
> ## Open tabs:
> - measure_memory.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/measure_memory.sh
> - measure_codesize.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/measure_codesize.sh
> - analyze.py: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/analyze.py
> - bench_evp.cpp: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/src/bench_evp.cpp
> - run.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/run.sh
> 
> ## My request:
> Work in the git repository ~/Nhom5/git-intro on branch `agent`, only inside
> unittest/. First read unittest/test_data.py, policy.py, threat-model.md and
> security-requirements.md.
> 
> 1. recursive_json_search.py: implement json_search(key, input_object, role=None)
>    with recursive search over nested dicts/lists, merging the results of every
>    level into one list. Enforce SR-01, SR-02, SR-04, SR-05, SR-06 using policy.py:
>    deny by default for missing, unknown or non-string roles; recursive redaction
>    of protected fields; no traversal into protected subtrees; null/float/bool
>    safe; depth > 100 raises ValueError; return copies; freeze the policy at
>    import. Do not modify policy.py or test_data.py.
> 2. test_json_search.py (unittest, class json_search_test, one-line docstrings):
>    keep test_search_found, test_search_not_found, test_is_a_list and add at
>    least 3 security tests whose docstrings start with the SR they verify,
>    e.g. "[SR-01] ...".
> 3. Run: cd unittest && python3 -m unittest -v test_json_search.py
>    and fix until all tests pass. Show git status, git diff --stat and a table
>    SR -> test.
> Rules: present your plan and wait for my approval before editing. Do not commit,
> push, switch branches, install packages or use the network.

### 06:01:50 Agent

> I’ll stay in `~/Nhom5/git-intro`, avoid network/package/branch/commit actions, and only inspect before you approve edits. I’m going to read the required files and confirm the repo state so the plan is grounded in the actual code.

### 06:01:50 Lệnh

```bash
$ git branch --show-current
```

### 06:01:50 Lệnh

```bash
$ git status --short
```

### 06:01:50 Lệnh

```bash
$ rg --files unittest
```

### 06:01:50 Lệnh

```bash
$ sed -n '1,240p' unittest/test_data.py
```

### 06:01:50 Lệnh

```bash
$ sed -n '1,240p' unittest/policy.py
```

### 06:01:50 Kết quả

```text
Chunk ID: 6fb8d0
Wall time: 0.0001 seconds
Process exited with code 0
Original token count: 2
Output:
agent
```

### 06:01:50 Kết quả

```text
Chunk ID: f4eb51
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 0
Output:
```

### 06:01:50 Kết quả

```text
Chunk ID: f6b4ba
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 41
Output:
unittest/test_json_search.py
unittest/recursive_json_search.py
unittest/test_data.py
unittest/security-requirements.md
unittest/policy.py
unittest/threat-model.md
```

### 06:01:50 Kết quả

```text
Chunk ID: be1168
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 1197
Output:
key1 = "issueSummary"
key2 = "XY&^$#*@!1234%^&"

data = {
  "id": "AWcvsjx864kVeDHDi2gB",
  "instanceId": "E-NETWORK-EVENT-AWcvsjx864kVeDHDi2gB-1542693469197",
  "category": "Warn",
  "status": "NEW",
  "timestamp": 1542693469197,
  "severity": "P1",
  "domain": "Availability",
  "source": "DNAC",
  "priority": "P1",
  "type": "Network",
  "title": "Device unreachable",
  "description": "This network device leaf2.abc.inc is unreachable from controller. The device role is ACCESS.",
  "actualServiceId": "10.10.20.82",
  "assignedTo": "",
  "enrichmentInfo": {
    "issueDetails": {
      "issue": [
        {
          "issueId": "AWcvsjx864kVeDHDi2gB",
          "issueSource": "Cisco DNA",
          "issueCategory": "Availability",
          "issueName": "snmp_device_down",
          "issueDescription": "This network device leaf2.abc.inc is unreachable from controller. The device role is ACCESS.",
          "issueEntity": "network_device",
          "issueEntityValue": "10.10.20.82",
          "issueSeverity": "HIGH",
          "issuePriority": "",
          "issueSummary": "Network Device 10.10.20.82 Is Unreachable From Controller",
          "issueTimestamp": 1542693469197,
          "suggestedActions": [
            {
... (bỏ bớt 82 dòng)
```

### 06:01:50 Kết quả

```text
Chunk ID: 64ba83
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 141
Output:
# policy.py
# Quy định vai trò (role) nào được phép đọc giá trị của một trường (key)
# cụ thể trong dữ liệu JSON trả về bởi json_search().
#
# Sinh viên dùng bảng này để viết security test ở Yêu cầu 6: gọi
# json_search(key, data, role=...) với một role KHÔNG nằm trong danh sách
# cho phép của key đó, và kỳ vọng kết quả trả về là rỗng.

POLICY = {
    "apiKey": ["admin"],
    "managementIpAddress": ["admin", "operator"],
    "issueSummary": ["admin", "operator", "viewer"],
}
```

### 06:01:57 Agent

> I’m on branch `agent` and the worktree is clean. I’ve read `test_data.py` and `policy.py`; next I’m reading the security docs plus the current implementation/tests, then I’ll give you the edit plan and stop for approval.

### 06:01:57 Lệnh

```bash
$ sed -n '1,260p' unittest/threat-model.md
```

### 06:01:57 Lệnh

```bash
$ sed -n '1,260p' unittest/security-requirements.md
```

### 06:01:57 Lệnh

```bash
$ sed -n '1,240p' unittest/recursive_json_search.py
```

### 06:01:57 Lệnh

```bash
$ sed -n '1,260p' unittest/test_json_search.py
```

### 06:01:57 Kết quả

```text
Chunk ID: cf2b5d
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 1270
Output:
# Threat model cho json_search()

## 1. Phạm vi

- Hàm `json_search(key, input_object, role=None)` trong `unittest/recursive_json_search.py`.
- Dữ liệu: JSON về sự cố mạng trong `test_data.py` (lấy từ Cisco DNA Center), trong đó có khóa
  SNMP và IP quản trị của thiết bị.
- Hàm được backend của dashboard gọi thay cho 3 role: admin, operator, viewer.
- Giả định:
  - role do server gán theo phiên đăng nhập, không lấy từ request của client.
  - input_object là JSON đã parse, cấu trúc không tin cậy được.
  - `policy.py` là nơi duy nhất quy định quyền; trường không có trong `policy.py` coi là không
    nhạy cảm.
- Ngoài phạm vi: đăng nhập, TLS, lưu log (thuộc tầng API).

## 2. DFD

```mermaid
flowchart TB
    subgraph TB1["TB1: phía người dùng (không tin cậy)"]
        U["Người dùng: admin, operator, viewer"]
    end
    subgraph BE["Backend"]
        API(["API / Dashboard, gán role theo phiên"])
        JS(["json_search(key, data, role)"])
        POL[("policy.py")]
    end
    subgraph TB2["TB2: vùng dữ liệu đặc quyền"]
        DATA[("Dữ liệu JSON có apiKey, IP quản trị")]
    end
    U -- request --> API
    API -- response --> U
    API -- "key, role" --> JS
    JS -- kết quả đã lọc --> API
    POL -- quyền theo trường --> JS
... (bỏ bớt 57 dòng)
```

### 06:01:57 Kết quả

```text
Chunk ID: 535e78
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 586
Output:
# Security requirements cho json_search()

Rút ra từ `threat-model.md`. Mỗi yêu cầu có mã SR để đối chiếu với security test trong
`test_json_search.py`.

| Mã | Yêu cầu | Threat | Kiểm chứng |
|---|---|---|---|
| SR-01 | Chỉ role có tên trong policy.py của trường X mới nhận được giá trị của X, role khác nhận [] | T-01 | test_viewer_cannot_read_apikey, test_policy_matrix |
| SR-02 | Mặc định từ chối: role phải là chuỗi trùng khớp admin, operator hoặc viewer (phân biệt hoa thường). Thiếu role hay role lạ thì trả [] với mọi key | T-03 | test_bad_role_is_denied |
| SR-03 | role phải lấy từ phiên đăng nhập phía server, không lấy từ tham số client gửi | T-04 | review tầng API |
| SR-04 | Giá trị trả về là dict hoặc list thì phải bỏ các trường con mà role không được đọc, và không duyệt vào bên trong trường bị cấm | T-02 | test_parent_key_does_not_leak |
| SR-05 | Không lỗi với JSON hợp lệ bất kỳ (null, số thực, bool, mảng rỗng). Lồng sâu quá 100 cấp thì báo ValueError | T-07 | test_odd_json_does_not_crash |
| SR-06 | Kết quả là bản sao, sửa kết quả không đổi dữ liệu gốc. Quyền được chép ra lúc import, sửa POLICY lúc chạy không có tác dụng | T-05, T-06 | test_result_is_a_copy, test_policy_change_at_runtime |
| SR-07 | Nên có ở tầng API: ghi log mỗi lần từ chối đọc trường nhạy cảm, không ghi giá trị bí mật | T-08 | ngoài phạm vi hàm |
| SR-08 | Agent chạy trong sandbox, không mạng, không tự commit, không sửa policy.py; chỉ nhận thay đổi sau khi xem diff và chạy bộ test riêng | T-09 | agent log, diff, kiểm chứng chéo |

## Tiêu chí chấp nhận

- SR-01: cho trước viewer đã đăng nhập; khi gọi `json_search("apiKey", data, role="viewer")`;
  thì kết quả là []. Gọi với admin thì vẫn nhận được giá trị.
- SR-04: cho trước viewer đã đăng nhập; khi tìm `deviceDetails`; thì kết quả vẫn có hostname
  nhưng không có apiKey và managementIpAddress.

Yêu cầu chức năng giữ như YC4: tìm đệ quy qua dict và list lồng nhau, gộp kết quả của mọi cấp
vào một list.
```

### 06:01:57 Kết quả

```text
Chunk ID: ed6301
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 9
Output:
# Fill the Python code in this file
```

### 06:01:57 Kết quả

```text
Chunk ID: 7453f4
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 9
Output:
# Fill the Python code in this file
```

### 06:02:09 Agent

> I’ve read the required files in `~/Nhom5/git-intro/unittest` and confirmed:
> 
> - Current branch: `agent`
> - Worktree: clean
> - `recursive_json_search.py` and `test_json_search.py` are placeholders
> - I will only edit files under `unittest/`
> 
> **Plan**
> 
> 1. Implement `recursive_json_search.py`
>    - Import and freeze `POLICY` at module import time.
>    - Validate `role`: only exact string roles `admin`, `operator`, `viewer` allowed.
>    - Deny by default for missing, unknown, or non-string roles.
>    - Recursively search dict/list structures and collect all matching values.
>    - Enforce protected-field policy:
>      - If searching a protected key, return results only when role is allowed.
>      - When returning dict/list values, deep-copy and recursively redact fields disallowed for that role.
>      - Do not traverse into protected subtrees when the current role cannot read that subtree key.
>    - Handle `None`, floats, bools, empty lists safely.
>    - Raise `ValueError` when nesting depth exceeds 100.
>    - Return copies so callers cannot mutate the original input.
> 
> 2. Implement `test_json_search.py`
>    - Use `unittest`.
>    - Class name: `json_search_test`.
>    - Keep required functional tests:
>      - `test_search_found`
>      - `test_search_not_found`
>      - `test_is_a_list`
>    - Add security tests with one-line docstrings starting with SR IDs, covering at least:
>      - `[SR-01]` unauthorized protected-field access denied
>      - `[SR-02]` missing/bad/non-string roles denied
>      - `[SR-04]` parent dict/list return does not leak protected children
>      - likely also `[SR-05]` and `[SR-06]` because the implementation requirements include them.
> 
> 3. Run exactly:
>    - `cd unittest && python3 -m unittest -v test_json_search.py`
> 
> 4. Fix until tests pass, then show:
>    - `git status`
>    - `git diff --stat`
>    - Table mapping `SR -> test`
> 
> I’ll wait for your approval before making any edits.

### 06:03:45 Người dùng (prompt 2)

> # Context from my IDE setup:
> 
> ## Open tabs:
> - measure_memory.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/measure_memory.sh
> - measure_codesize.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/measure_codesize.sh
> - analyze.py: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/analyze.py
> - bench_evp.cpp: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/src/bench_evp.cpp
> - run.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/run.sh
> 
> ## My request:
> Approved. Go ahead.

### 06:04:00 Agent

> Great, I’m going to make the two scoped edits now: the implementation first, then the unittest file with the functional tests plus SR-labeled security coverage.

### 06:04:00 Lệnh

```bash
$ pwd
```

### 06:04:00 Lệnh

```bash
$ nl -ba unittest/security-requirements.md
```

### 06:04:00 Lệnh

```bash
$ nl -ba unittest/threat-model.md
```

### 06:04:00 Kết quả

```text
Chunk ID: 3f0fa7
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 9
Output:
/home/chung-tra274/Nhom5/git-intro
```

### 06:04:00 Kết quả

```text
Chunk ID: 8d6268
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 630
Output:
     1	# Security requirements cho json_search()
     2	
     3	Rút ra từ `threat-model.md`. Mỗi yêu cầu có mã SR để đối chiếu với security test trong
     4	`test_json_search.py`.
     5	
     6	| Mã | Yêu cầu | Threat | Kiểm chứng |
     7	|---|---|---|---|
     8	| SR-01 | Chỉ role có tên trong policy.py của trường X mới nhận được giá trị của X, role khác nhận [] | T-01 | test_viewer_cannot_read_apikey, test_policy_matrix |
     9	| SR-02 | Mặc định từ chối: role phải là chuỗi trùng khớp admin, operator hoặc viewer (phân biệt hoa thường). Thiếu role hay role lạ thì trả [] với mọi key | T-03 | test_bad_role_is_denied |
    10	| SR-03 | role phải lấy từ phiên đăng nhập phía server, không lấy từ tham số client gửi | T-04 | review tầng API |
    11	| SR-04 | Giá trị trả về là dict hoặc list thì phải bỏ các trường con mà role không được đọc, và không duyệt vào bên trong trường bị cấm | T-02 | test_parent_key_does_not_leak |
    12	| SR-05 | Không lỗi với JSON hợp lệ bất kỳ (null, số thực, bool, mảng rỗng). Lồng sâu quá 100 cấp thì báo ValueError | T-07 | test_odd_json_does_not_crash |
    13	| SR-06 | Kết quả là bản sao, sửa kết quả không đổi dữ liệu gốc. Quyền được chép ra lúc import, sửa POLICY lúc chạy không có tác dụng | T-05, T-06 | test_result_is_a_copy, test_policy_change_at_runtime |
    14	| SR-07 | Nên có ở tầng API: ghi log mỗi lần từ chối đọc trường nhạy cảm, không ghi giá trị bí mật | T-08 | ngoài phạm vi hàm |
    15	| SR-08 | Agent chạy trong sandbox, không mạng, không tự commit, không sửa policy.py; chỉ nhận thay đổi sau khi xem diff và chạy bộ test riêng | T-09 | agent log, diff, kiểm chứng chéo |
    16	
    17	## Tiêu chí chấp nhận
    18	
    19	- SR-01: cho trước viewer đã đăng nhập; khi gọi `json_search("apiKey", data, role="viewer")`;
    20	  thì kết quả là []. Gọi với admin thì vẫn nhận được giá trị.
    21	- SR-04: cho trước viewer đã đăng nhập; khi tìm `deviceDetails`; thì kết quả vẫn có hostname
    22	  nhưng không có apiKey và managementIpAddress.
    23	
    24	Yêu cầu chức năng giữ như YC4: tìm đệ quy qua dict và list lồng nhau, gộp kết quả của mọi cấp
    25	vào một list.
```

### 06:04:00 Kết quả

```text
Chunk ID: e5971d
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 1431
Output:
     1	# Threat model cho json_search()
     2	
     3	## 1. Phạm vi
     4	
     5	- Hàm `json_search(key, input_object, role=None)` trong `unittest/recursive_json_search.py`.
     6	- Dữ liệu: JSON về sự cố mạng trong `test_data.py` (lấy từ Cisco DNA Center), trong đó có khóa
     7	  SNMP và IP quản trị của thiết bị.
     8	- Hàm được backend của dashboard gọi thay cho 3 role: admin, operator, viewer.
     9	- Giả định:
    10	  - role do server gán theo phiên đăng nhập, không lấy từ request của client.
    11	  - input_object là JSON đã parse, cấu trúc không tin cậy được.
    12	  - `policy.py` là nơi duy nhất quy định quyền; trường không có trong `policy.py` coi là không
    13	    nhạy cảm.
    14	- Ngoài phạm vi: đăng nhập, TLS, lưu log (thuộc tầng API).
    15	
    16	## 2. DFD
    17	
    18	```mermaid
    19	flowchart TB
    20	    subgraph TB1["TB1: phía người dùng (không tin cậy)"]
    21	        U["Người dùng: admin, operator, viewer"]
    22	    end
    23	    subgraph BE["Backend"]
    24	        API(["API / Dashboard, gán role theo phiên"])
    25	        JS(["json_search(key, data, role)"])
    26	        POL[("policy.py")]
    27	    end
    28	    subgraph TB2["TB2: vùng dữ liệu đặc quyền"]
    29	        DATA[("Dữ liệu JSON có apiKey, IP quản trị")]
    30	    end
    31	    U -- request --> API
    32	    API -- response --> U
    33	    API -- "key, role" --> JS
    34	    JS -- kết quả đã lọc --> API
    35	    POL -- quyền theo trường --> JS
... (bỏ bớt 57 dòng)
```

### 06:04:03 Agent

> The security docs clarify one important detail: unknown or missing roles must get nothing for every key, while valid roles may read unprotected fields. I’m encoding that as a small policy gate plus recursive copy/redaction helpers.

### 06:04:11 Sửa file (apply_patch)

```diff
*** Begin Patch
*** Update File: /home/chung-tra274/Nhom5/git-intro/unittest/recursive_json_search.py
@@
-# Fill the Python code in this file
+from policy import POLICY
+
+
+_POLICY = {key: frozenset(roles) for key, roles in POLICY.items()}
+_VALID_ROLES = frozenset({"admin", "operator", "viewer"})
+_MAX_DEPTH = 100
+
+
+def _check_depth(depth):
+    if depth > _MAX_DEPTH:
+        raise ValueError("JSON nesting depth exceeds 100")
+
+
+def _role_can_read(key, role):
+    allowed_roles = _POLICY.get(key)
+    return allowed_roles is None or role in allowed_roles
+
+
+def _redacted_copy(value, role, depth):
+    _check_depth(depth)
+
+    if isinstance(value, dict):
+        copied = {}
+        for child_key, child_value in value.items():
+            if not _role_can_read(child_key, role):
+                continue
+            copied[child_key] = _redacted_copy(child_value, role, depth + 1)
+        return copied
+
+    if isinstance(value, list):
+        return [_redacted_copy(item, role, depth + 1) for item in value]
+
+    return value
+
+
+def json_search(key, input_object, role=None):
+    if not isinstance(role, str) or role not in _VALID_ROLES:
+        return []
+
+    results = []
+
+    def search(value, depth):
+        _check_depth(depth)
+
+        if isinstance(value, dict):
+            for child_key, child_value in value.items():
+                if not _role_can_read(child_key, role):
+                    continue
+
+                if child_key == key:
+                    results.append(_redacted_copy(child_value, role, depth + 1))
+
+                search(child_value, depth + 1)
+        elif isinstance(value, list):
+            for item in value:
+                search(item, depth + 1)
+
+    search(input_object, 0)
+    return results
*** End Patch
```

### 06:04:11 Kết quả

```text
Exit code: 0
Wall time: 0 seconds
Output:
Success. Updated the following files:
M /home/chung-tra274/Nhom5/git-intro/unittest/recursive_json_search.py
```

### 06:04:23 Agent

> Implementation is in place. Now I’m adding the tests with the requested class name and concise docstrings, keeping the three functional test names and covering the policy, redaction, robustness, and copy/frozen-policy requirements.

### 06:04:40 Sửa file (apply_patch)

```diff
*** Begin Patch
*** Update File: /home/chung-tra274/Nhom5/git-intro/unittest/test_json_search.py
@@
-# Fill the Python code in this file
+import unittest
+
+import policy
+from recursive_json_search import json_search
+from test_data import data, key1, key2
+
+
+class json_search_test(unittest.TestCase):
+    def test_search_found(self):
+        """Finds an existing key for an allowed role."""
+        self.assertEqual(
+            json_search(key1, data, role="viewer"),
+            ["Network Device 10.10.20.82 Is Unreachable From Controller"],
+        )
+
+    def test_search_not_found(self):
+        """Returns an empty list when the key is absent."""
+        self.assertEqual(json_search(key2, data, role="admin"), [])
+
+    def test_is_a_list(self):
+        """Always returns a list."""
+        self.assertIsInstance(json_search(key1, data, role="viewer"), list)
+
+    def test_viewer_cannot_read_apikey(self):
+        """[SR-01] Denies protected fields to roles outside policy."""
+        self.assertEqual(json_search("apiKey", data, role="viewer"), [])
+        self.assertEqual(
+            json_search("apiKey", data, role="admin"),
+            ["SNMP-COMMUNITY-STRING-7f3a9c"],
+        )
+
+    def test_bad_role_is_denied(self):
+        """[SR-02] Denies missing, unknown, case-mismatched, and non-string roles."""
+        for bad_role in (None, "", "Admin", "guest", ["admin"]):
+            self.assertEqual(json_search("hostname", data, role=bad_role), [])
+
+    def test_parent_key_does_not_leak(self):
+        """[SR-04] Redacts protected children from returned parent values."""
+        result = json_search("deviceDetails", data, role="viewer")
+
+        self.assertEqual(len(result), 1)
+        self.assertEqual(result[0]["hostname"], "leaf2.abc.inc")
+        self.assertNotIn("apiKey", result[0])
+        self.assertNotIn("managementIpAddress", result[0])
+
+    def test_no_traversal_into_protected_subtree(self):
+        """[SR-04] Skips traversal inside protected subtrees denied to the role."""
+        odd_data = {"apiKey": {"hidden": "secret"}, "visible": {"hidden": "ok"}}
+
+        self.assertEqual(json_search("hidden", odd_data, role="viewer"), ["ok"])
+
+    def test_odd_json_does_not_crash(self):
+        """[SR-05] Handles null, float, bool, and empty list values safely."""
+        odd_data = {"items": [None, 1.25, True, [], {"target": False}]}
+
+        self.assertEqual(json_search("target", odd_data, role="operator"), [False])
+
+    def test_too_deep_json_raises(self):
+        """[SR-05] Raises ValueError when nesting depth exceeds 100."""
+        too_deep = value = {}
+        for _ in range(101):
+            value["next"] = {}
+            value = value["next"]
+
+        with self.assertRaises(ValueError):
+            json_search("missing", too_deep, role="admin")
+
+    def test_result_is_a_copy(self):
+        """[SR-06] Returns copies so callers cannot mutate source data."""
+        result = json_search("deviceDetails", data, role="admin")
+        result[0]["hostname"] = "changed.example"
+
+        original = json_search("hostname", data, role="admin")
+        self.assertEqual(original, ["leaf2.abc.inc"])
+
+    def test_policy_change_at_runtime(self):
... (bỏ bớt 11 dòng)
```

### 06:04:40 Kết quả

```text
Exit code: 0
Wall time: 0 seconds
Output:
Success. Updated the following files:
M /home/chung-tra274/Nhom5/git-intro/unittest/test_json_search.py
```

### 06:04:44 Agent

> The files are edited. I’m running the requested unittest command now, then I’ll tighten anything the tests reveal before collecting the final status and diff summary.

### 06:04:44 Lệnh

```bash
$ cd unittest && python3 -m unittest -v test_json_search.py
```

### 06:04:44 Kết quả

```text
Chunk ID: ab2887
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 440
Output:
test_bad_role_is_denied (test_json_search.json_search_test.test_bad_role_is_denied)
[SR-02] Denies missing, unknown, case-mismatched, and non-string roles. ... ok
test_is_a_list (test_json_search.json_search_test.test_is_a_list)
Always returns a list. ... ok
test_no_traversal_into_protected_subtree (test_json_search.json_search_test.test_no_traversal_into_protected_subtree)
[SR-04] Skips traversal inside protected subtrees denied to the role. ... ok
test_odd_json_does_not_crash (test_json_search.json_search_test.test_odd_json_does_not_crash)
[SR-05] Handles null, float, bool, and empty list values safely. ... ok
test_parent_key_does_not_leak (test_json_search.json_search_test.test_parent_key_does_not_leak)
[SR-04] Redacts protected children from returned parent values. ... ok
test_policy_change_at_runtime (test_json_search.json_search_test.test_policy_change_at_runtime)
[SR-06] Keeps import-time policy permissions frozen. ... ok
test_result_is_a_copy (test_json_search.json_search_test.test_result_is_a_copy)
[SR-06] Returns copies so callers cannot mutate source data. ... ok
test_search_found (test_json_search.json_search_test.test_search_found)
Finds an existing key for an allowed role. ... ok
test_search_not_found (test_json_search.json_search_test.test_search_not_found)
Returns an empty list when the key is absent. ... ok
test_too_deep_json_raises (test_json_search.json_search_test.test_too_deep_json_raises)
[SR-05] Raises ValueError when nesting depth exceeds 100. ... ok
test_viewer_cannot_read_apikey (test_json_search.json_search_test.test_viewer_cannot_read_apikey)
[SR-01] Denies protected fields to roles outside policy. ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.001s

OK
```

### 06:04:51 Agent

> All 11 tests passed on the first run. I’m doing the requested final checks now: status, diff stat, and a quick diff read so the closeout can point to exactly what changed.

### 06:04:51 Lệnh

```bash
$ git status --short
```

### 06:04:51 Lệnh

```bash
$ git diff --stat
```

### 06:04:51 Lệnh

```bash
$ git diff -- unittest/recursive_json_search.py unittest/test_json_search.py
```

### 06:04:51 Kết quả

```text
Chunk ID: 335afc
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 18
Output:
 M unittest/recursive_json_search.py
 M unittest/test_json_search.py
```

### 06:04:51 Kết quả

```text
Chunk ID: e952b1
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 50
Output:
 unittest/recursive_json_search.py | 60 ++++++++++++++++++++++++++-
 unittest/test_json_search.py      | 87 ++++++++++++++++++++++++++++++++++++++-
 2 files changed, 145 insertions(+), 2 deletions(-)
```

### 06:04:51 Kết quả

```text
Chunk ID: a0d996
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 1395
Output:
diff --git a/unittest/recursive_json_search.py b/unittest/recursive_json_search.py
index 8c1fa79..dd16d7a 100644
--- a/unittest/recursive_json_search.py
+++ b/unittest/recursive_json_search.py
@@ -1 +1,59 @@
-# Fill the Python code in this file
+from policy import POLICY
+
+
+_POLICY = {key: frozenset(roles) for key, roles in POLICY.items()}
+_VALID_ROLES = frozenset({"admin", "operator", "viewer"})
+_MAX_DEPTH = 100
+
+
+def _check_depth(depth):
+    if depth > _MAX_DEPTH:
+        raise ValueError("JSON nesting depth exceeds 100")
+
+
+def _role_can_read(key, role):
+    allowed_roles = _POLICY.get(key)
+    return allowed_roles is None or role in allowed_roles
+
+
+def _redacted_copy(value, role, depth):
+    _check_depth(depth)
+
+    if isinstance(value, dict):
+        copied = {}
+        for child_key, child_value in value.items():
+            if not _role_can_read(child_key, role):
+                continue
+            copied[child_key] = _redacted_copy(child_value, role, depth + 1)
+        return copied
+
... (bỏ bớt 122 dòng)
```

### 06:05:00 Agent

> Implemented in `~/Nhom5/git-intro` on branch `agent`, only under `unittest/`.
> 
> Changed:
> - [recursive_json_search.py](/home/chung-tra274/Nhom5/git-intro/unittest/recursive_json_search.py): recursive search, import-time frozen policy, default-deny role checks, redacted copies, protected subtree skip, depth guard.
> - [test_json_search.py](/home/chung-tra274/Nhom5/git-intro/unittest/test_json_search.py): kept the 3 required functional tests and added SR-labeled security tests.
> 
> Verification passed:
> 
> ```text
> cd unittest && python3 -m unittest -v test_json_search.py
> Ran 11 tests in 0.001s
> 
> OK
> ```
> 
> Git status:
> 
> ```text
>  M unittest/recursive_json_search.py
>  M unittest/test_json_search.py
> ```
> 
> Git diff stat:
> 
> ```text
>  unittest/recursive_json_search.py | 60 ++++++++++++++++++++++++++-
>  unittest/test_json_search.py      | 87 ++++++++++++++++++++++++++++++++++++++-
>  2 files changed, 145 insertions(+), 2 deletions(-)
> ```
> 
> | SR | Test |
> |---|---|
> | SR-01 | `test_viewer_cannot_read_apikey` |
> | SR-02 | `test_bad_role_is_denied` |
> | SR-04 | `test_parent_key_does_not_leak`, `test_no_traversal_into_protected_subtree` |
> | SR-05 | `test_odd_json_does_not_crash`, `test_too_deep_json_raises` |
> | SR-06 | `test_result_is_a_copy`, `test_policy_change_at_runtime` |

### 06:18:47 Người dùng (prompt 3)

> # Context from my IDE setup:
> 
> ## Open tabs:
> - measure_memory.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/measure_memory.sh
> - measure_codesize.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/measure_codesize.sh
> - analyze.py: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/analyze.py
> - bench_evp.cpp: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/src/bench_evp.cpp
> - run.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/run.sh
> 
> ## My request:
> Independent review found these requirements are not met:
> [SR-01] viewer không đọc được apiKey, admin thì đọc được ... FAIL
> [SR-05] JSON có null, số thực hoặc lồng quá sâu không làm sập hàm ... FAIL
> [SR-06] sửa kết quả trả về không làm đổi dữ liệu gốc ... ERROR
> json_search must keep the original return format: a list of {key: value}
> dicts, one per match, e.g. [{"apiKey": "..."}]. JSON nested deeper than
> 100 levels must raise ValueError.
> Fix recursive_json_search.py and update test_json_search.py to match.
> Same rules as before: present your plan, wait for my approval, no commit,
> no network, do not modify policy.py or test_data.py.

### 06:19:00 Agent

> Got it. I’ll wait before editing.
> 
> **Plan**
> 
> 1. Update `recursive_json_search.py`
>    - Preserve original return format: each match becomes `{matched_key: copied_value}`.
>    - Example: `json_search("apiKey", data, role="admin")` returns `[{"apiKey": "..."}]`.
>    - Keep default-deny role validation for `None`, unknown, case-mismatched, and non-string roles.
>    - Keep protected subtree behavior:
>      - Unauthorized protected key is not returned.
>      - Unauthorized protected subtree is not traversed.
>      - Returned parent dict/list values are recursively redacted.
>    - Keep import-time frozen policy.
>    - Ensure all returned values are copies.
>    - Ensure `None`, floats, bools, empty lists are safe.
>    - Ensure nesting deeper than 100 levels raises `ValueError`.
> 
> 2. Update `test_json_search.py`
>    - Change expected functional/security results to list-of-dicts format.
>    - Update SR-01 admin/viewer expectations for `apiKey`.
>    - Update SR-04 parent result assertions to read from `result[0]["deviceDetails"]`.
>    - Update SR-05 tests to explicitly check odd JSON does not crash and too-deep JSON raises `ValueError`.
>    - Update SR-06 mutation test to mutate through the `{key: value}` wrapper and verify source data is unchanged.
> 
> 3. Run:
>    - `cd unittest && python3 -m unittest -v test_json_search.py`
> 
> 4. Fix until passing, then show:
>    - `git status`
>    - `git diff --stat`
>    - SR -> test table
> 
> No commit, no network, no package install, no changes to `policy.py` or `test_data.py`.

### 06:20:09 Người dùng (prompt 4)

> # Context from my IDE setup:
> 
> ## Open tabs:
> - measure_memory.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/measure_memory.sh
> - measure_codesize.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/measure_codesize.sh
> - analyze.py: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/scripts/analyze.py
> - bench_evp.cpp: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/src/bench_evp.cpp
> - run.sh: /home/chung-tra274/Desktop/Crypto/NT219.Q21.ANTT-Cryptanalysis_on_Lattice_based_algorithms/run.sh
> 
> ## My request:
> Approved. Go ahead.

### 06:20:19 Agent

> I’ll adjust the implementation to wrap each match as `{key: value}` and then bring the assertions into that shape. I’m keeping the policy and fixture files untouched.

### 06:20:21 Sửa file (apply_patch)

```diff
*** Begin Patch
*** Update File: /home/chung-tra274/Nhom5/git-intro/unittest/recursive_json_search.py
@@
                 if not _role_can_read(child_key, role):
                     continue
 
                 if child_key == key:
-                    results.append(_redacted_copy(child_value, role, depth + 1))
+                    results.append({
+                        child_key: _redacted_copy(child_value, role, depth + 1)
+                    })
 
                 search(child_value, depth + 1)
*** End Patch
```

### 06:20:21 Kết quả

```text
Exit code: 0
Wall time: 0 seconds
Output:
Success. Updated the following files:
M /home/chung-tra274/Nhom5/git-intro/unittest/recursive_json_search.py
```

### 06:20:24 Agent

> The return wrapper is fixed in the implementation. Now I’m updating the tests so they verify the old public format directly instead of the bare-value format I had used.

### 06:20:32 Sửa file (apply_patch)

```diff
*** Begin Patch
*** Update File: /home/chung-tra274/Nhom5/git-intro/unittest/test_json_search.py
@@
         """Finds an existing key for an allowed role."""
         self.assertEqual(
             json_search(key1, data, role="viewer"),
-            ["Network Device 10.10.20.82 Is Unreachable From Controller"],
+            [{key1: "Network Device 10.10.20.82 Is Unreachable From Controller"}],
         )
@@
         self.assertEqual(json_search("apiKey", data, role="viewer"), [])
         self.assertEqual(
             json_search("apiKey", data, role="admin"),
-            ["SNMP-COMMUNITY-STRING-7f3a9c"],
+            [{"apiKey": "SNMP-COMMUNITY-STRING-7f3a9c"}],
         )
@@
         odd_data = {"apiKey": {"hidden": "secret"}, "visible": {"hidden": "ok"}}
 
-        self.assertEqual(json_search("hidden", odd_data, role="viewer"), ["ok"])
+        self.assertEqual(json_search("hidden", odd_data, role="viewer"), [{"hidden": "ok"}])
@@
         odd_data = {"items": [None, 1.25, True, [], {"target": False}]}
 
-        self.assertEqual(json_search("target", odd_data, role="operator"), [False])
+        self.assertEqual(json_search("target", odd_data, role="operator"), [{"target": False}])
@@
         """[SR-06] Returns copies so callers cannot mutate source data."""
         result = json_search("deviceDetails", data, role="admin")
-        result[0]["hostname"] = "changed.example"
+        result[0]["deviceDetails"]["hostname"] = "changed.example"
 
         original = json_search("hostname", data, role="admin")
-        self.assertEqual(original, ["leaf2.abc.inc"])
+        self.assertEqual(original, [{"hostname": "leaf2.abc.inc"}])
*** End Patch
```

### 06:20:32 Kết quả

```text
Exit code: 0
Wall time: 0 seconds
Output:
Success. Updated the following files:
M /home/chung-tra274/Nhom5/git-intro/unittest/test_json_search.py
```

### 06:20:37 Agent

> Most expectations are updated; I’m doing a quick scan for any assertions that still assume bare values before running the suite.

### 06:20:37 Lệnh

```bash
$ sed -n '1,220p' unittest/test_json_search.py
```

### 06:20:37 Lệnh

```bash
$ sed -n '1,180p' unittest/recursive_json_search.py
```

### 06:20:37 Kết quả

```text
Chunk ID: a17608
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 862
Output:
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
... (bỏ bớt 51 dòng)
```

### 06:20:37 Kết quả

```text
Chunk ID: e95f10
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 413
Output:
from policy import POLICY


_POLICY = {key: frozenset(roles) for key, roles in POLICY.items()}
_VALID_ROLES = frozenset({"admin", "operator", "viewer"})
_MAX_DEPTH = 100


def _check_depth(depth):
    if depth > _MAX_DEPTH:
        raise ValueError("JSON nesting depth exceeds 100")


def _role_can_read(key, role):
    allowed_roles = _POLICY.get(key)
    return allowed_roles is None or role in allowed_roles


def _redacted_copy(value, role, depth):
    _check_depth(depth)

    if isinstance(value, dict):
        copied = {}
        for child_key, child_value in value.items():
            if not _role_can_read(child_key, role):
                continue
            copied[child_key] = _redacted_copy(child_value, role, depth + 1)
        return copied

    if isinstance(value, list):
        return [_redacted_copy(item, role, depth + 1) for item in value]

    return value


... (bỏ bớt 26 dòng)
```

### 06:20:41 Agent

> I found one parent-result assertion still looking at the wrapper dict instead of its `deviceDetails` payload. I’m correcting that before the test run.

### 06:20:43 Sửa file (apply_patch)

```diff
*** Begin Patch
*** Update File: /home/chung-tra274/Nhom5/git-intro/unittest/test_json_search.py
@@
         result = json_search("deviceDetails", data, role="viewer")
+        device_details = result[0]["deviceDetails"]
 
         self.assertEqual(len(result), 1)
-        self.assertEqual(result[0]["hostname"], "leaf2.abc.inc")
-        self.assertNotIn("apiKey", result[0])
-        self.assertNotIn("managementIpAddress", result[0])
+        self.assertEqual(device_details["hostname"], "leaf2.abc.inc")
+        self.assertNotIn("apiKey", device_details)
+        self.assertNotIn("managementIpAddress", device_details)
*** End Patch
```

### 06:20:44 Kết quả

```text
Exit code: 0
Wall time: 0 seconds
Output:
Success. Updated the following files:
M /home/chung-tra274/Nhom5/git-intro/unittest/test_json_search.py
```

### 06:20:46 Agent

> The test file now matches the wrapper format throughout. I’m running the requested unittest command and will fix anything that still disagrees with the independent review expectations.

### 06:20:47 Lệnh

```bash
$ cd unittest && python3 -m unittest -v test_json_search.py
```

### 06:20:47 Kết quả

```text
Chunk ID: 272cd6
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 440
Output:
test_bad_role_is_denied (test_json_search.json_search_test.test_bad_role_is_denied)
[SR-02] Denies missing, unknown, case-mismatched, and non-string roles. ... ok
test_is_a_list (test_json_search.json_search_test.test_is_a_list)
Always returns a list. ... ok
test_no_traversal_into_protected_subtree (test_json_search.json_search_test.test_no_traversal_into_protected_subtree)
[SR-04] Skips traversal inside protected subtrees denied to the role. ... ok
test_odd_json_does_not_crash (test_json_search.json_search_test.test_odd_json_does_not_crash)
[SR-05] Handles null, float, bool, and empty list values safely. ... ok
test_parent_key_does_not_leak (test_json_search.json_search_test.test_parent_key_does_not_leak)
[SR-04] Redacts protected children from returned parent values. ... ok
test_policy_change_at_runtime (test_json_search.json_search_test.test_policy_change_at_runtime)
[SR-06] Keeps import-time policy permissions frozen. ... ok
test_result_is_a_copy (test_json_search.json_search_test.test_result_is_a_copy)
[SR-06] Returns copies so callers cannot mutate source data. ... ok
test_search_found (test_json_search.json_search_test.test_search_found)
Finds an existing key for an allowed role. ... ok
test_search_not_found (test_json_search.json_search_test.test_search_not_found)
Returns an empty list when the key is absent. ... ok
test_too_deep_json_raises (test_json_search.json_search_test.test_too_deep_json_raises)
[SR-05] Raises ValueError when nesting depth exceeds 100. ... ok
test_viewer_cannot_read_apikey (test_json_search.json_search_test.test_viewer_cannot_read_apikey)
[SR-01] Denies protected fields to roles outside policy. ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.001s

OK
```

### 06:21:00 Agent

> The requested test command passes with the corrected format. I’m collecting the final `git status`, `git diff --stat`, and a compact diff check now.

### 06:21:00 Lệnh

```bash
$ git status --short
```

### 06:21:00 Lệnh

```bash
$ git diff --stat
```

### 06:21:00 Lệnh

```bash
$ git diff -- unittest/recursive_json_search.py unittest/test_json_search.py
```

### 06:21:00 Kết quả

```text
Chunk ID: 5b4b43
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 18
Output:
 M unittest/recursive_json_search.py
 M unittest/test_json_search.py
```

### 06:21:00 Kết quả

```text
Chunk ID: 3715e3
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 50
Output:
 unittest/recursive_json_search.py | 62 ++++++++++++++++++++++++++-
 unittest/test_json_search.py      | 88 ++++++++++++++++++++++++++++++++++++++-
 2 files changed, 148 insertions(+), 2 deletions(-)
```

### 06:21:00 Kết quả

```text
Chunk ID: b0e905
Wall time: 0.0000 seconds
Process exited with code 0
Original token count: 1446
Output:
diff --git a/unittest/recursive_json_search.py b/unittest/recursive_json_search.py
index 8c1fa79..eaf5a42 100644
--- a/unittest/recursive_json_search.py
+++ b/unittest/recursive_json_search.py
@@ -1 +1,61 @@
-# Fill the Python code in this file
+from policy import POLICY
+
+
+_POLICY = {key: frozenset(roles) for key, roles in POLICY.items()}
+_VALID_ROLES = frozenset({"admin", "operator", "viewer"})
+_MAX_DEPTH = 100
+
+
+def _check_depth(depth):
+    if depth > _MAX_DEPTH:
+        raise ValueError("JSON nesting depth exceeds 100")
+
+
+def _role_can_read(key, role):
+    allowed_roles = _POLICY.get(key)
+    return allowed_roles is None or role in allowed_roles
+
+
+def _redacted_copy(value, role, depth):
+    _check_depth(depth)
+
+    if isinstance(value, dict):
+        copied = {}
+        for child_key, child_value in value.items():
+            if not _role_can_read(child_key, role):
+                continue
+            copied[child_key] = _redacted_copy(child_value, role, depth + 1)
+        return copied
+
... (bỏ bớt 125 dòng)
```

### 06:21:07 Agent

> Fixed the return format issue: `json_search()` now returns a list of `{key: value}` dicts, one per match, while preserving redaction, protected subtree skipping, frozen policy, copy behavior, and depth checks.
> 
> Test run:
> 
> ```text
> cd unittest && python3 -m unittest -v test_json_search.py
> Ran 11 tests in 0.001s
> 
> OK
> ```
> 
> Git status:
> 
> ```text
>  M unittest/recursive_json_search.py
>  M unittest/test_json_search.py
> ```
> 
> Git diff stat:
> 
> ```text
>  unittest/recursive_json_search.py | 62 ++++++++++++++++++++++++++-
>  unittest/test_json_search.py      | 88 ++++++++++++++++++++++++++++++++++++++-
>  2 files changed, 148 insertions(+), 2 deletions(-)
> ```
> 
> | SR | Test |
> |---|---|
> | SR-01 | `test_viewer_cannot_read_apikey` |
> | SR-02 | `test_bad_role_is_denied` |
> | SR-04 | `test_parent_key_does_not_leak`, `test_no_traversal_into_protected_subtree` |
> | SR-05 | `test_odd_json_does_not_crash`, `test_too_deep_json_raises` |
> | SR-06 | `test_result_is_a_copy`, `test_policy_change_at_runtime` |
