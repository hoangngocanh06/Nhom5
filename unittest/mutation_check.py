"""Kiểm tra bộ test có bắt được lỗi không (mutation testing).

Mỗi mutant cài lại một lỗi vào bản sao của recursive_json_search.py trong thư
mục tạm rồi chạy bộ test. Có test fail là mutant "bị phát hiện", không test nào
fail là "còn sống" (bộ test bỏ sót lỗi đó). File trong repo không bị sửa.

    python3 mutation_check.py                   # chạy với test_json_search.py
    python3 mutation_check.py /tmp/tests.py     # chạy với bộ test khác
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
CODE = "recursive_json_search.py"

# mã, yêu cầu, lỗi được cài, đoạn code gốc, đoạn code sau khi cài lỗi
MUTANTS = [
    ("M0", "chức năng", "mất kết quả đệ quy (lỗi YC4)",
     "ret_val, depth + 1)", "[], depth + 1)"),
    ("M1", "SR-02", "thiếu role thì coi như admin",
     "    ret_val = []\n", "    ret_val = []\n    role = role or 'admin'\n"),
    ("M2", "SR-01", "bỏ kiểm tra quyền",
     "return allowed is None or role in allowed", "return True"),
    ("M3", "SR-04", "trả nguyên giá trị, không lọc",
     "ret_val.append({k: redact(v, role, depth + 1)})", "ret_val.append({k: v})"),
    ("M4", "SR-04", "vẫn duyệt vào trường bị cấm",
     "continue", "pass"),
    ("M5", "SR-05", "bỏ giới hạn độ sâu",
     "if depth > MAX_DEPTH:", "if False:"),
    ("M6", "SR-06", "đọc thẳng POLICY lúc chạy",
     "allowed = RULES.get(field)", "allowed = POLICY.get(field)"),
]


def run_tests(folder):
    cmd = [sys.executable, "-m", "unittest", "tests_to_check"]
    proc = subprocess.run(cmd, cwd=folder, capture_output=True, text=True,
                          timeout=300)
    failed = sorted(set(re.findall(r"^(?:FAIL|ERROR): (\w+)", proc.stderr, re.M)))
    return proc.returncode == 0, failed


def main():
    tests = HERE / "test_json_search.py"
    if len(sys.argv) > 1:
        tests = pathlib.Path(sys.argv[1]).resolve()

    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp, "base")
        shutil.copytree(HERE, base, ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copy(tests, base / "tests_to_check.py")

        ok, failed = run_tests(base)
        print("Bộ test:", tests)
        status = "đạt" if ok else "không đạt (" + ", ".join(failed) + ")"
        print("Trên code gốc:", status)

        killed = total = 0
        for mid, req, bug, old, new in MUTANTS:
            work = pathlib.Path(tmp, mid)
            shutil.copytree(base, work)
            source = (work / CODE).read_text(encoding="utf-8")
            if old not in source:
                print(f"{mid}  {req:<9} {bug:<30} bỏ qua, không thấy đoạn code")
                continue
            (work / CODE).write_text(source.replace(old, new), encoding="utf-8")

            ok, failed = run_tests(work)
            total += 1
            killed += not ok
            result = "còn sống" if ok else "bị phát hiện bởi " + ", ".join(failed)
            print(f"{mid}  {req:<9} {bug:<30} {result}")

        print(f"Mutation score: {killed}/{total}")


if __name__ == "__main__":
    main()
