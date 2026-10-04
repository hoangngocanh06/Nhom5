from policy import POLICY

__all__ = ["json_search"]

# Chép policy lúc import để sau này có sửa POLICY thì quyền cũng không đổi
RULES = {field: frozenset(roles) for field, roles in POLICY.items()}
ROLES = frozenset().union(*RULES.values())    # admin, operator, viewer
MAX_DEPTH = 100


def can_read(field, role):
    allowed = RULES.get(field)
    # trường không có trong policy thì role nào cũng đọc được
    return allowed is None or role in allowed


def check_depth(depth):
    if depth > MAX_DEPTH:
        raise ValueError("JSON lồng quá sâu")


def redact(value, role, depth):
    """Trả về bản sao của value, đã bỏ các trường con mà role không được đọc."""
    check_depth(depth)
    if isinstance(value, dict):
        return {k: redact(v, role, depth + 1)
                for k, v in value.items() if can_read(k, role)}
    if isinstance(value, list):
        return [redact(item, role, depth + 1) for item in value]
    return value


def search(key, node, role, ret_val, depth):
    check_depth(depth)
    if isinstance(node, dict):
        for k, v in node.items():
            if not can_read(k, role):
                continue    # bỏ qua luôn phần dữ liệu nằm bên trong trường bị cấm
            if k == key:
                ret_val.append({k: redact(v, role, depth + 1)})
            search(key, v, role, ret_val, depth + 1)
    elif isinstance(node, list):
        for item in node:
            search(key, item, role, ret_val, depth + 1)


def json_search(key, input_object, role=None):
    """Tìm key trong input_object, chỉ trả về giá trị mà role được phép đọc."""
    ret_val = []
    if not isinstance(role, str) or role not in ROLES:
        return ret_val    # thiếu role hoặc role lạ thì không trả gì
    if not can_read(key, role):
        return ret_val
    search(key, input_object, role, ret_val, 0)
    return ret_val


if __name__ == "__main__":
    from test_data import data

    for role in (None, "viewer", "operator", "admin"):
        print(f"role={role}")
        for field in ("issueSummary", "managementIpAddress", "apiKey"):
            print(f"  {field:<20} {json_search(field, data, role)}")
