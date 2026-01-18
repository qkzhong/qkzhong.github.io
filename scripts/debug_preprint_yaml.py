import json
import time
from pathlib import Path


LOG_PATH = Path("/Users/zhong/qkzhong.github.io/.cursor/debug.log")
TARGET = Path("/Users/zhong/qkzhong.github.io/content/publication/preprint/index.md")


def log(message, data, hypothesis_id):
    entry = {
        "sessionId": "debug-session",
        "runId": "pre-fix",
        "hypothesisId": hypothesis_id,
        "location": "scripts/debug_preprint_yaml.py",
        "message": message,
        "data": data,
        "timestamp": int(time.time() * 1000),
    }
    with LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry) + "\n")


def main():
    log("Start YAML debug", {"target": str(TARGET)}, "H1")
    text = TARGET.read_text(encoding="utf-8")
    parts = text.split("---")
    front_matter = parts[1].splitlines() if len(parts) > 2 else []
    log("Front matter lines", {"count": len(front_matter)}, "H1")

    suspicious = []
    for idx, line in enumerate(front_matter, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- "):
            continue
        if ":" not in stripped:
            suspicious.append({"line": idx, "content": line})
            continue
        if line.startswith("  ") and not front_matter[idx - 2].strip().endswith(":"):
            suspicious.append({"line": idx, "content": line})

    log("Suspicious lines", {"items": suspicious}, "H2")
    log("Done YAML debug", {"suspicious_count": len(suspicious)}, "H3")


if __name__ == "__main__":
    main()
