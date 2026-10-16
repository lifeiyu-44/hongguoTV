个人归档：红果 Android TV 源码构建包，以及上游 Windows v1.2.2 原始发行文件。

- Windows 初次使用请下载完整 `hongguo-v1.2.2-windows-amd64.zip` 并解压，保留其中的 WebView2、HEVC 安装文件；单独 EXE 供已有完整环境使用。Windows EXE 不是本次重新编译的，哈希与上游一致。
- Android APK：`0.9.0-private`，最低 Android 8，已通过 Release 构建、签名校验与 Android 15 MuMu 安装，首页、详情正常。**实际播放失败，自动重试 3 次仍未恢复，目前不能保证看剧。**
- APK 使用个人归档签名，不能覆盖不同签名的上游版本。改装前先备份记录，卸载会清除数据。私钥没有上传。
- Windows JVM 测试 82/83 通过；1 项文件替换测试在 Windows 失败，相同 Java 操作在 Android 15 成功。完整测试、lint 和证据见仓库 `docs/DELIVERY.md`、`verification/` 与 Actions。
- 两份上游源码快照共 201 文件，版本、许可、目录统计及重建方式已保留。桌面项目公开仓库不含构建源码。本次没有 iPhone IPA。

下载后可按 `RELEASE-SHA256SUMS.txt` 核对三个发行文件。访问此 Release 需要有私有仓库权限的 GitHub 账号。
