# 交付与验证记录（2026-10-16）

## 内容和来源

个人私有仓库：https://github.com/lifeiyu-44/hongguoTV 。

两个 Git 快照共 201 个文件、8,473,243 字节：Android 项目 192 个文件，桌面发布仓库 9 个文件。导出文件内容和暂存区 Git blob 均逐个核对，全部与指定上游提交一致；原来的可执行文件权限也已保留。来源与完整目录见 PROVENANCE.md 和 DIRECTORY_TREE.md。

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
