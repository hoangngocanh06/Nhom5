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
