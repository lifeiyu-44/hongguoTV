# 红果项目个人归档

归档日期：2026-10-16。此仓库同时保留 Android TV 源码和已经可用的 Windows 桌面发行包，两者是独立项目。

| 目录 | 内容 |
|---|---|
| `sources/hongguoTV/` | `N3urda/hongguoTV` 原始源码快照，含原生 Kotlin Android TV、旧 React Native 和服务端代码 |
| `sources/hongguo-player/` | `yangbin1322/hongguo-player` 公开仓库快照，只有说明和截图，不包含桌面应用构建源码 |
| `artifacts/windows/` | 上游 v1.2.2 原始 EXE、完整 ZIP 和配套安装文件 |
| `artifacts/android/` | 本机从上述 Kotlin 源码构建的 APK |
| `docs/` | 目录清单、来源、安装和构建说明 |
| `verification/` | 校验清单、构建与检查结果 |
| `scripts/` | 目录统计、文件校验和 Android 构建脚本 |

Windows 使用：下载 `artifacts/windows/hongguo-v1.2.2-windows-amd64.zip`，完整解压后双击 `红果短剧.exe`。保留同目录的 WebView2、HEVC 安装文件。也可直接使用本归档 `artifacts/windows/` 中的完整文件夹。

Android APK 的签名、安装方式和实际验证结果以 [交付记录](docs/DELIVERY.md) 为准。

这是个人备份，Windows EXE 为上游原始发行文件，并非从 Android 工程转换或重新编译而来。Android 源码沿用上游 GPL-3.0 许可，原始 LICENSE/NOTICE 完整保留；桌面项目不公开源码，其说明见 `sources/hongguo-player/README.md`。

- [来源和源码版本](docs/PROVENANCE.md)
- [完整目录统计](docs/DIRECTORY_TREE.md)
- [文件 SHA-256](verification/SHA256SUMS.txt)
- [构建、检查和安装结果](docs/DELIVERY.md)

重新统计：`python scripts/inventory.py`。校验发行文件：`powershell -File scripts/Verify-Archive.ps1`。

未包含平台账号、登录数据、观看记录、签名私钥或口令。iOS 目录是上游 tvOS 工程骨架，本次没有交付 iPhone IPA。
