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

## PC（Windows）端如何启动

从 [Releases](https://github.com/lifeiyu-44/hongguoTV/releases) 下载完整 `hongguo-v1.2.2-windows-amd64.zip`（仓库内 `artifacts/windows/` 是同一套文件）：

1. 解压整个 ZIP 到一个文件夹。建议放 D 盘等非系统目录，不要放 `C:\Program Files`（没有写入权限，无法自动更新）；也不要只单独拿走 exe——`红果短剧.exe` 要和 WebView2、HEVC 安装文件留在同一目录。
2. 双击 `红果短剧.exe` 启动。
3. 首次运行缺依赖时程序会提示，Windows 10/11 一般已自带：
   - 缺 WebView2 会自动安装；失败就手动双击 `MicrosoftEdgeWebview2Setup.exe`，装好后再打开程序。
   - 缺 HEVC 视频扩展（视频为 H.265 编码，缺了会有声音没画面）会后台自动安装；失败就双击 `HEVC视频扩展-双击安装.appx` 手动安装后重启程序。
4. 首次启动如果防火墙/杀毒软件弹窗：在网络授权提示里点「一键放行」或「允许」（程序需要访问本地播放服务 127.0.0.1）；杀毒软件误报时把程序所在文件夹加入信任区。

登录状态、观看记录和缓存在 `C:\Users\<用户名>\AppData\Roaming\hgplayer`，可在程序「设置 › 数据与缓存」里迁移或清理。完整说明见 `artifacts/windows/使用说明.txt`。

Android APK 的签名、安装方式和实际验证结果以 [交付记录](docs/DELIVERY.md) 为准。

**本次 Android APK 已通过构建、签名和 MuMu 安装，首页与详情正常，但实际播放失败，自动重试后仍未恢复。** Windows v1.2.2 有同日既有播放成功记录，本轮重新核对了其发行文件哈希。

[下载本次发布包](https://github.com/lifeiyu-44/hongguoTV/releases/tag/archive-2026-10-16-final)。

这是个人备份，Windows EXE 为上游原始发行文件，并非从 Android 工程转换或重新编译而来。Android 源码沿用上游 GPL-3.0 许可，原始 LICENSE/NOTICE 完整保留；桌面项目不公开源码，其说明见 `sources/hongguo-player/README.md`。

- [来源和源码版本](docs/PROVENANCE.md)
- [完整目录统计](docs/DIRECTORY_TREE.md)
- [文件 SHA-256](verification/SHA256SUMS.txt)
- [构建、检查和安装结果](docs/DELIVERY.md)

重新统计：`python scripts/inventory.py`。校验发行文件：`powershell -File scripts/Verify-Archive.ps1`。

未包含平台账号、登录数据、观看记录、签名私钥或口令。iOS 目录是上游 tvOS 工程骨架，本次没有交付 iPhone IPA。
