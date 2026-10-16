# 从源码构建 Android APK

构建对象为 `sources/hongguoTV/kotlin-tv`，不需要 npm、React Native 或服务端。需要 JDK 17、Android SDK Platform 36、Build Tools 36.0.0；包装器使用 Gradle 8.14.3。

Windows PowerShell 示例（路径请替换为本机路径）：

```powershell
$env:JAVA_HOME = 'C:\path\to\jdk-17'
$env:ANDROID_HOME = 'C:\path\to\android-sdk'
.\scripts\Build-Android.ps1
```

默认运行 JVM 测试、Debug lint 和 Debug 构建，输出 `sources/hongguoTV/kotlin-tv/app/build/outputs/apk/debug/app-debug.apk`。Debug 包使用本机 Android 开发签名，不能覆盖不同签名的已安装包。

正式构建需要自行保管签名文件，并设置四个环境变量：

```text
HONGGUOTV_KEYSTORE        签名文件绝对路径
HONGGUOTV_STORE_PASSWORD 签名库口令
HONGGUOTV_KEY_ALIAS      密钥别名
HONGGUOTV_KEY_PASSWORD   密钥口令
```

之后运行 `./scripts/Build-Android.ps1 -Release`。APK 位于 `sources/hongguoTV/kotlin-tv/app/build/outputs/apk/release/app-release.apk`。脚本不会将新包自动覆盖到归档发行目录；替换发行文件后，重新运行 `python scripts/inventory.py` 更新校验清单（Python 3.11 或更高版本）。

源码快照未修改。本次首次构建在工作克隆 `H:\gpt_work_dir\hongguoTV\kotlin-tv` 执行，使用相同 Git 提交；发布前另行核对快照文件。完整环境与结果见 DELIVERY.md。

本次归档签名材料单独保存在本机 `H:\gpt_work_dir\toolchain\hongguotv-signing`，不在 Git 仓库中。`local-signing.json` 只用于本机重建，不应上传。后续自有签名版本要保留同一密钥。

Android 与桌面是两个独立应用。公开桌面仓库没有构建源码，因此此处不提供重新编译 EXE 的命令。Windows 文件直接来自上游 v1.2.2 Release，并已按其 SHA-256 验证。
