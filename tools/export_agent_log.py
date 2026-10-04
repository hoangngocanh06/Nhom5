import argparse
import json
import pathlib
import re
from datetime import datetime

SHELL_TOOLS = ("exec_command", "shell", "shell_command", "local_shell")
PATCH_FILE = re.compile(r"^\*\*\* (?:Add|Update|Delete) File: (.+)$", re.M)


def newest_rollout():
    folder = pathlib.Path.home() / ".codex" / "sessions"
    files = sorted(folder.rglob("rollout-*.jsonl"), key=lambda f: f.stat().st_mtime)
    if not files:
        raise SystemExit(f"Không có file rollout nào trong {folder}")
    return files[-1]


def to_time(value):
    try:
        return datetime.fromisoformat(value).astimezone()
    except (TypeError, ValueError):
        return None


def text_of(content):
    if isinstance(content, str):
        return content
    return "\n".join(c.get("text", "") for c in content or [] if isinstance(c, dict))


def clip(text, limit=40):
    lines = text.rstrip().splitlines()
    if len(lines) > limit:
        lines = lines[:limit] + [f"... (bỏ bớt {len(lines) - limit} dòng)"]
    return "\n".join(lines)


def quote(text):
    return "\n".join("> " + line for line in text.splitlines()) or ">"


def export(path):
    meta, ctx, tokens = {}, {}, {}
    prompts = commands = escalated = patches = 0
    changed = set()
    start = end = None
    log = []

    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        kind, p = row.get("type"), row.get("payload") or {}
        t = to_time(row.get("timestamp"))
        if t:
            start, end = start or t, t
        head = f"### {t:%H:%M:%S} " if t else "### "

        if kind == "session_meta":
            meta = p
        elif kind == "turn_context":
            ctx = p
        elif kind == "event_msg" and p.get("type") == "token_count" and p.get("info"):
            tokens = p["info"].get("total_token_usage") or {}
        elif kind == "event_msg" and p.get("type") == "turn_aborted":
            log.append(head + "Turn bị hủy\n")
        elif kind != "response_item":
            continue

        elif p.get("type") == "message":
            text = text_of(p.get("content"))
            if p.get("role") == "user" and text and not text.lstrip().startswith("<"):
                prompts += 1
                log.append(f"{head}Người dùng (prompt {prompts})\n\n{quote(text)}\n")
            elif p.get("role") == "assistant" and text:
                log.append(f"{head}Agent\n\n{quote(text)}\n")

        elif p.get("type") == "reasoning":
            text = text_of(p.get("summary"))
            if text:
                log.append(f"{head}Agent (tóm tắt suy luận)\n\n{quote(text)}\n")

        elif p.get("type") == "function_call":
            args = json.loads(p.get("arguments") or "{}")
            if p.get("name") not in SHELL_TOOLS:
                body = clip(json.dumps(args, ensure_ascii=False, indent=1))
                log.append(f"{head}Công cụ {p.get('name')}\n\n```json\n{body}\n```\n")
                continue
            cmd = args.get("cmd") or args.get("command") or ""
            if isinstance(cmd, list):
                cmd = " ".join(cmd)
            commands += 1
            title = "Lệnh"
            if args.get("sandbox_permissions") == "require_escalated":
                escalated += 1
                title = "Lệnh xin chạy ngoài sandbox"
            reason = f"# lý do: {args['justification']}\n" if args.get("justification") else ""
            log.append(f"{head}{title}\n\n```bash\n{reason}$ {cmd}\n```\n")

        elif p.get("type") == "custom_tool_call" and p.get("name") == "apply_patch":
            patch = p.get("input", "")
            patches += 1
            changed.update(PATCH_FILE.findall(patch))
            log.append(f"{head}Sửa file (apply_patch)\n\n```diff\n{clip(patch, 80)}\n```\n")

        elif p.get("type") in ("function_call_output", "custom_tool_call_output"):
            out = p.get("output")
            out = text_of(out) if isinstance(out, list) else str(out or "")
            try:
                out = json.loads(out)["output"]    # bản Codex cũ bọc output trong JSON
            except (ValueError, KeyError, TypeError):
                pass
            log.append(f"{head}Kết quả\n\n```text\n{clip(str(out))}\n```\n")

    git = meta.get("git") or {}
    commit = str(git.get("commit_hash", "?"))[:7]
    sandbox = ctx.get("sandbox_policy") or {}
    when = f"{start:%Y-%m-%d %H:%M:%S} đến {end:%H:%M:%S}" if start else "?"
    rows = [
        ("File", path.name),
        ("Session", meta.get("id", "?")),
        ("Thời gian", when),
        ("Thư mục", meta.get("cwd", "?")),
        ("Git lúc bắt đầu", f"{git.get('branch', '?')} @ {commit}"),
        ("Mô hình", f"{ctx.get('model', '?')}, effort {ctx.get('effort', '?')}"),
        ("Approval policy", ctx.get("approval_policy", "?")),
        ("Sandbox", sandbox.get("type", "?")),
        ("Mạng trong sandbox", sandbox.get("network_access", False)),
        ("Số prompt", prompts),
        ("Số lệnh agent chạy", commands),
        ("Lệnh xin chạy ngoài sandbox", escalated),
        ("Số lần sửa file", f"{patches} ({', '.join(sorted(changed)) or '-'})"),
        ("Token vào", tokens.get("input_tokens", "?")),
        ("Token ra", tokens.get("output_tokens", "?")),
    ]
    out = [f"# Agent log, phiên Codex {meta.get('id', '')}", "",
           "| Mục | Giá trị |", "|---|---|"]
    out += [f"| {name} | {value} |" for name, value in rows]
    out += ["", "Rollout không lưu các lần bấm Approve/Decline nên phần này "
            "ghi tay trong báo cáo.", "", "## Diễn biến", ""]
    return "\n".join(out + log)


def main():
    parser = argparse.ArgumentParser(description="Xuất log phiên Codex ra Markdown")
    parser.add_argument("rollout", nargs="?", type=pathlib.Path)
    parser.add_argument("-o", "--output", type=pathlib.Path,
                        default=pathlib.Path("agent-log.md"))
    args = parser.parse_args()

    path = args.rollout or newest_rollout()
    args.output.write_text(export(path), encoding="utf-8")
    print(f"Đã xuất {path} -> {args.output}")


if __name__ == "__main__":
    main()
