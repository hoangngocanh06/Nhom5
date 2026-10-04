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


def json_search(key, input_object, role=None):
    if not isinstance(role, str) or role not in _VALID_ROLES:
        return []

    results = []

    def search(value, depth):
        _check_depth(depth)

        if isinstance(value, dict):
            for child_key, child_value in value.items():
                if not _role_can_read(child_key, role):
                    continue

                if child_key == key:
                    results.append({
                        child_key: _redacted_copy(child_value, role, depth + 1)
                    })

                search(child_value, depth + 1)
        elif isinstance(value, list):
            for item in value:
                search(item, depth + 1)

    search(input_object, 0)
    return results
