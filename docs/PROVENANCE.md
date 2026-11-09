# 来源与版本

| 项目 | 上游 | 快照提交 | 内容 |
|---|---|---|---|
| Android TV | https://github.com/N3urda/hongguoTV | `eea73e6a45569a2cbbb9440f7cd5290c459b0b70` | main 分支 Git 源码快照；本次原生应用版本 0.9.0 / versionCode 9 |
| Windows 发布仓库 | https://github.com/yangbin1322/hongguo-player | `a4688b02e57c11c159b15d4ce369f53f98299b2d` | Git 源码快照，README、文档截图与 issue 模板，无 EXE 构建源码 |
| Windows 二进制 | https://github.com/yangbin1322/hongguo-player/releases/tag/v1.2.2 | `v1.2.2` | 上游原始 Windows amd64 EXE 与完整 ZIP |

Windows 文件在 2026-10-16 通过 GitHub Release API 的 digest 字段核对：

```text
f040009e0a5e12cc2a414a226ddfa5830256bd6775ef1c9a7c478e2441e2e3b4  红果短剧.exe
4c484e00ef25bc520944605b6663dfdeeafed5fda21306b8a0c585eb78e28e84  hongguo-v1.2.2-windows-amd64.zip
```

完整 ZIP 包含主程序、WebView2 安装程序、HEVC 扩展和使用说明。归档只复制明确列出的发行文件，不复制应用数据或登录记录。

两个 `sources/` 目录通过对应 Git 提交的 `git archive` 导出，不嵌套 `.git`。Android 源码的 LICENSE、原生目录 LICENSE/NOTICE 以及上游文档完整保留。上游文档中既往版本的验证结论不代表本次验证，本次结果见 DELIVERY.md。

原始本地克隆分别位于 `H:\gpt_work_dir\hongguoTV` 和 `H:\gpt_work_dir\hongguo-player`；归档工作目录为 `H:\gpt_work_dir\hongguo-archive`。

## 更新记录

- 2026-11-09：核对上游——N3urda/hongguoTV main 与 `codex/kotlin-standalone` 分支自 `eea73e6`（2026-09-23）后均无新提交，Android TV 快照仍为最新。`sources/hongguo-player` 快照由 `f71f66b2` 更新至 `a4688b02`（2026-11-04，上游 README/FAQ 与 issue 模板更新，仍无 EXE 构建源码）。
- 2026-11-09：上游已发布 v1.2.25（2026-11-07），本归档 Windows 发行文件保持 v1.2.2 不变。v1.2.25 官方 SHA256（GitHub Release API digest 字段）：

```text
2766fa669c23c161613be11200626652ba9e0ef04b38d9f72359871d97951ea5  hongguo-v1.2.25-windows-amd64.zip
34ca6b31abbaf1a70a09d07b47aa365dacffa7d085113fcecac753e4edb1cd06  hongguo-v1.2.25-windows-amd64.exe
```
