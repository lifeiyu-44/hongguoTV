# 交付与验证记录（2026-10-16）

## 内容和来源

个人私有仓库：https://github.com/lifeiyu-44/hongguoTV 。

两个 Git 快照共 201 个文件、8,449,349 字节：Android 项目 192 个文件，桌面发布仓库 9 个文件。导出时关闭 Windows 行尾自动转换，暂存区 Git blob 和文件权限逐个核对，全部与指定上游提交一致。来源与完整目录见 PROVENANCE.md 和 DIRECTORY_TREE.md。

Windows 为 `hongguo-player v1.2.2` 原始发行包，EXE 与完整 ZIP 的 SHA-256 均与 GitHub 上游 Release digest 一致。配套 WebView2/HEVC 安装文件原样保留。桌面仓库不公开构建源码，因此没有重新编译 EXE。

`verification/windows-prior-playback.png` 和 `prior-installation-notes.txt` 是同日已有的安装与播放证据，记录 v1.2.2 的画面播放至 00:29、暂停正常。本轮重新核对了原始文件哈希，没有将旧证据描述为本轮重新播放。已有桌面快捷方式和原 MuMu 第 0 号设备保留。

## 本机构建环境

- Windows，Eclipse Temurin JDK 17.0.20.1+1，Gradle 8.14.3。
- Android SDK Platform 36 revision 2、Build Tools 36.0.0。
- Gradle 和 SDK ZIP 分别核对官方 SHA-256、SDK 清单 SHA-1 后解压。
- 构建对象：上游 `eea73e6a45569a2cbbb9440f7cd5290c459b0b70` 的 `kotlin-tv`，未修改源码。
- SDK 下载与 Gradle 的 Google Maven 代理连接出现 TLS 问题后，改用官方地址直连。

## Windows JVM 测试

运行 `:core:test`：83 项测试，82 通过、1 失败，无错误。

失败项：`AppUpdatesTest.verifiedDownloadAtomicallyReplacesOldFile`。上游 `UpdateFiles.receive` 使用 `File.renameTo` 替换已有文件，该操作在本机 Windows 返回 false，抛出“无法保存安装包”。本次没有跳过该测试并声称全部通过，也没有为打包改写原始快照。

使用相同 Java 文件操作单独核对：Windows 得到 `renamed=false; content=previous`；Android 15 MuMu 得到 `renamed=true; content=verified-new-apk`。探针源文件保存在 `verification/RenameProbe.java`。这验证了文件替换行为，不能代替真实自动更新下载和安装验收。

仓库另配置 Linux CI 执行完整 JVM 测试、Debug lint 与 Debug APK 构建，不使用或上传本机签名私钥。Windows 上如只需构建 APK，可直接运行 `:app:lintRelease :app:assembleRelease`；默认 `Build-Android.ps1` 会严格执行测试，并如实报告上述 Windows 失败。

## 本次签名 APK

- 文件：`artifacts/android/hongguotv-kotlin-0.9.0-private-android8.apk`，2,677,001 字节。
- 包名：`com.hongguotv.nativeapp`；versionCode 9；versionName `0.9.0-private`。版本名称通过上游已有环境变量设置，源码未改动。
- 最低 API 26（Android 8.0），目标和编译 API 36，无需另部署服务。
- `:app:lintRelease :app:assembleRelease` 成功，Release lint：0 errors、28 warnings。记录见 `verification/release-build.txt` 和 `lint-results-release.txt`。
- `apksigner verify --verbose --print-certs` 成功，APK v2 签名有效；证书 SHA-256：`29609e5f0ac5e58fbcef98948b2a0f8bf4940c5c52387fd139addd87037b86d4`。
- 这是个人归档签名，与上游正式签名不同。私钥只保存在本机仓库外，未上传 GitHub。

## 安装和实际播放

使用全新 MuMu 第 1 号 Android 15 设备验证，未覆盖原有第 0 号设备。该测试设备名为 `HongguoTV Archive Verification`，测试后停止运行，供后续复查。

1. `adb install -r` 安装成功，`am start -W` 启动状态 ok，冷启动 190 ms（只是 Activity 启动用时，不代表内容全部加载用时）。
2. 首页真实加载了漫剧列表、海报和集数；进入「满院亲戚全是上古大妖第五季」，详情展示 222 集，遥控确认进入第 1 集。
3. **播放未通过**：自动重试 3 次后仍显示“已自动重试 3 次，仍无法播放。可手动重试或切换清晰度。”本轮未修改或修复第三方播放接口。已有 0.8.0 安装记录也显示播放失败，但不足以据此判断本次错误的根因。
4. 证据：`verification/android-home.png`、`android-detail.png`、`android-playback-failure.png`。不把列表加载、签名或安装成功当作可播放。

Windows 桌面版与 Android 使用不同实现。归档保留已核对过哈希、此前实际播放成功的 Windows v1.2.2；Android APK 是可安装的源码构建产物，目前不能保证看剧。Android 8 实体电视上的解码、音频和长期稳定性没有验证。

## 安装到自己的电视

没有装过这个包名时，可以直接安装本次 APK。已安装上游签名包时，Android 不允许不同签名覆盖安装；**先通过旧应用备份本机记录**，再考虑改装，卸载旧应用会清除其本机数据。也可继续使用上游正式版本或在独立设备安装本次归档包。

应用中的更新器仍指向上游 `N3urda/hongguoTV-updates`，不会从本私有归档仓库更新。上游 APK 与本次签名不同，不能覆盖本归档包；后续归档版本应继续用本机同一密钥构建并手动安装。

## 下载

私有发布页：https://github.com/lifeiyu-44/hongguoTV/releases/tag/archive-2026-10-16-final 。访问需要有仓库权限的 GitHub 账号。Release 提供 APK、Windows 完整 ZIP、主 EXE 和 SHA-256 清单；Git 仓库也直接保留这些文件和配套安装程序。
