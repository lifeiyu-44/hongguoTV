"""Generate the tracked-delivery inventory and hashes without machine metadata."""
import hashlib
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", ".gradle", ".kotlin", "build", "node_modules", "__pycache__"}


def files_under(folder):
    return sorted(p for p in folder.rglob("*") if p.is_file()
                  and not IGNORED.intersection(p.relative_to(ROOT).parts))


def main():
    totals = defaultdict(lambda: [0, 0])
    source_files = files_under(ROOT / "sources")
    for path in source_files:
        key = "/".join(path.relative_to(ROOT).parts[:3])
        totals[key][0] += 1
        totals[key][1] += path.stat().st_size
    rows = ["# 目录统计", "", "统计对象：两个上游 Git 源码快照。字节数为文件实际大小，不包含 Git 历史、依赖缓存或构建目录。", "",
            "| 目录 | 文件数 | 字节数 |", "|---|---:|---:|"]
    for key, (count, size) in sorted(totals.items()):
        rows.append(f"| `{key}` | {count} | {size:,} |")
    rows += [f"| **总计** | **{len(source_files)}** | **{sum(p.stat().st_size for p in source_files):,}** |",
             "", "## 源码文件清单", "", "```text"]
    rows += [p.relative_to(ROOT).as_posix() for p in source_files]
    rows += ["```", ""]
    (ROOT / "docs" / "DIRECTORY_TREE.md").write_text("\n".join(rows), encoding="utf-8")
    manifest = []
    for path in files_under(ROOT / "artifacts"):
        with path.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        manifest.append({"path": path.relative_to(ROOT).as_posix(), "size": path.stat().st_size,
                         "sha256": digest})
    (ROOT / "verification" / "artifacts.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "verification" / "SHA256SUMS.txt").write_text(
        "".join(f'{f["sha256"]}  {f["path"]}\n' for f in manifest), encoding="utf-8")
    print(json.dumps({"source_files": len(source_files), "source_bytes": sum(p.stat().st_size for p in source_files),
                      "artifact_files": len(manifest)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
