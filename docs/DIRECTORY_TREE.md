# 目录统计

统计对象：两个上游 Git 源码快照。字节数为文件实际大小，不包含 Git 历史、依赖缓存或构建目录。

| 目录 | 文件数 | 字节数 |
|---|---:|---:|
| `sources/hongguo-player/README.md` | 1 | 6,789 |
| `sources/hongguo-player/docs` | 8 | 7,008,992 |
| `sources/hongguoTV/.dockerignore` | 1 | 86 |
| `sources/hongguoTV/.env.example` | 1 | 441 |
| `sources/hongguoTV/.github` | 3 | 6,988 |
| `sources/hongguoTV/.gitignore` | 1 | 535 |
| `sources/hongguoTV/.npmrc` | 1 | 104 |
| `sources/hongguoTV/App.tsx` | 1 | 17,393 |
| `sources/hongguoTV/LICENSE` | 1 | 35,823 |
| `sources/hongguoTV/README.md` | 1 | 5,194 |
| `sources/hongguoTV/android` | 29 | 176,824 |
| `sources/hongguoTV/app.json` | 1 | 60 |
| `sources/hongguoTV/babel.config.js` | 1 | 75 |
| `sources/hongguoTV/compose.yaml` | 1 | 507 |
| `sources/hongguoTV/docs` | 11 | 62,817 |
| `sources/hongguoTV/index.js` | 1 | 196 |
| `sources/hongguoTV/ios` | 10 | 32,632 |
| `sources/hongguoTV/kotlin-tv` | 95 | 611,662 |
| `sources/hongguoTV/metro.config.js` | 1 | 312 |
| `sources/hongguoTV/package-lock.json` | 1 | 318,846 |
| `sources/hongguoTV/package.json` | 1 | 1,277 |
| `sources/hongguoTV/scripts` | 5 | 11,185 |
| `sources/hongguoTV/server` | 12 | 129,317 |
| `sources/hongguoTV/src` | 9 | 38,308 |
| `sources/hongguoTV/tests` | 3 | 6,671 |
| `sources/hongguoTV/tsconfig.json` | 1 | 209 |
| **总计** | **201** | **8,473,243** |

## 源码文件清单

```text
sources/hongguo-player/docs/screenshots/favorites.png
sources/hongguo-player/docs/screenshots/history.png
sources/hongguo-player/docs/screenshots/likes.png
sources/hongguo-player/docs/screenshots/new.png
sources/hongguo-player/docs/screenshots/rank.png
sources/hongguo-player/docs/screenshots/recommend.png
sources/hongguo-player/docs/screenshots/reservations.png
sources/hongguo-player/docs/screenshots/search.png
sources/hongguo-player/README.md
sources/hongguoTV/.dockerignore
sources/hongguoTV/.env.example
sources/hongguoTV/.github/workflows/kotlin-native.yml
sources/hongguoTV/.github/workflows/kotlin-public-sync.yml
sources/hongguoTV/.github/workflows/verify-publish.yml
sources/hongguoTV/.gitignore
sources/hongguoTV/.npmrc
sources/hongguoTV/android/app/build.gradle
sources/hongguoTV/android/app/proguard-rules.pro
sources/hongguoTV/android/app/src/debug/AndroidManifest.xml
sources/hongguoTV/android/app/src/main/AndroidManifest.xml
sources/hongguoTV/android/app/src/main/java/com/hongguotv/MainActivity.kt
sources/hongguoTV/android/app/src/main/java/com/hongguotv/MainApplication.kt
sources/hongguoTV/android/app/src/main/res/drawable/app_icon.xml
sources/hongguoTV/android/app/src/main/res/drawable/rn_edit_text_material.xml
sources/hongguoTV/android/app/src/main/res/drawable/tv_banner.png
sources/hongguoTV/android/app/src/main/res/drawable/tv_brand.xml
sources/hongguoTV/android/app/src/main/res/mipmap-hdpi/ic_launcher.png
sources/hongguoTV/android/app/src/main/res/mipmap-hdpi/ic_launcher_round.png
sources/hongguoTV/android/app/src/main/res/mipmap-mdpi/ic_launcher.png
sources/hongguoTV/android/app/src/main/res/mipmap-mdpi/ic_launcher_round.png
sources/hongguoTV/android/app/src/main/res/mipmap-xhdpi/ic_launcher.png
sources/hongguoTV/android/app/src/main/res/mipmap-xhdpi/ic_launcher_round.png
sources/hongguoTV/android/app/src/main/res/mipmap-xxhdpi/ic_launcher.png
sources/hongguoTV/android/app/src/main/res/mipmap-xxhdpi/ic_launcher_round.png
sources/hongguoTV/android/app/src/main/res/mipmap-xxxhdpi/ic_launcher.png
sources/hongguoTV/android/app/src/main/res/mipmap-xxxhdpi/ic_launcher_round.png
sources/hongguoTV/android/app/src/main/res/values/strings.xml
sources/hongguoTV/android/app/src/main/res/values/styles.xml
sources/hongguoTV/android/build.gradle
sources/hongguoTV/android/gradle/wrapper/gradle-wrapper.jar
sources/hongguoTV/android/gradle/wrapper/gradle-wrapper.properties
sources/hongguoTV/android/gradle.properties
sources/hongguoTV/android/gradlew
sources/hongguoTV/android/gradlew.bat
sources/hongguoTV/android/settings.gradle
sources/hongguoTV/app.json
sources/hongguoTV/App.tsx
sources/hongguoTV/babel.config.js
sources/hongguoTV/compose.yaml
sources/hongguoTV/docs/ACCOUNT_SYNC.md
sources/hongguoTV/docs/API.md
sources/hongguoTV/docs/ARCHITECTURE.md
sources/hongguoTV/docs/DOCKER.md
sources/hongguoTV/docs/FIRST_RELEASE.md
sources/hongguoTV/docs/PROJECT_STATUS.md
sources/hongguoTV/docs/RELEASE_0.1.1.md
sources/hongguoTV/docs/research/2026-09-21-hongguo-open-source.md
sources/hongguoTV/docs/research/2026-09-22-low-end-tv-audit.md
sources/hongguoTV/docs/superpowers/plans/2026-09-22-comic-speed.md
sources/hongguoTV/docs/superpowers/specs/2026-09-22-comic-speed-design.md
sources/hongguoTV/index.js
sources/hongguoTV/ios/_xcode.env
sources/hongguoTV/ios/HongguoTV/AppDelegate.swift
sources/hongguoTV/ios/HongguoTV/Images.xcassets/AppIcon.appiconset/Contents.json
sources/hongguoTV/ios/HongguoTV/Images.xcassets/Contents.json
sources/hongguoTV/ios/HongguoTV/Info.plist
sources/hongguoTV/ios/HongguoTV/LaunchScreen.storyboard
sources/hongguoTV/ios/HongguoTV/PrivacyInfo.xcprivacy
sources/hongguoTV/ios/HongguoTV.xcodeproj/project.pbxproj
sources/hongguoTV/ios/HongguoTV.xcodeproj/xcshareddata/xcschemes/HongguoTV.xcscheme
sources/hongguoTV/ios/Podfile
sources/hongguoTV/kotlin-tv/app/build.gradle.kts
sources/hongguoTV/kotlin-tv/app/proguard-rules.pro
sources/hongguoTV/kotlin-tv/app/src/main/AndroidManifest.xml
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/AppUpdater.kt
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/ArtworkCache.kt
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/ArtworkLoader.kt
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/EpisodePanel.kt
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/FavoriteMonitor.kt
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/HomeScreen.kt
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/Library.kt
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/MainActivity.kt
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/TvMediaSession.kt
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/TvStyle.kt
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/TvTools.kt
sources/hongguoTV/kotlin-tv/app/src/main/kotlin/com/hongguotv/nativeapp/VideoDataSource.kt
sources/hongguoTV/kotlin-tv/app/src/main/res/drawable/app_icon.xml
sources/hongguoTV/kotlin-tv/app/src/main/res/drawable/tv_banner.png
sources/hongguoTV/kotlin-tv/app/src/main/res/values/styles.xml
sources/hongguoTV/kotlin-tv/app/src/main/res/xml/network_security_config.xml
sources/hongguoTV/kotlin-tv/app/src/main/res/xml/update_paths.xml
sources/hongguoTV/kotlin-tv/AUTO_UPDATES.md
sources/hongguoTV/kotlin-tv/build.gradle.kts
sources/hongguoTV/kotlin-tv/COMIC_RANKING_VERIFICATION.md
sources/hongguoTV/kotlin-tv/COMIC_SPEED_VERIFICATION.md
sources/hongguoTV/kotlin-tv/core/build.gradle.kts
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/AesV3.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/AppUpdates.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/Bytes.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/CatalogSnapshot.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/ComicRank.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/ContentRepository.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/ContentType.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/LatestWriteQueue.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/LibraryBackup.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/LibraryIndex.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/LibraryTransferServer.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/MediaCrypto.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/PhoneSearchServer.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/PlaybackComfort.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/PlaybackSpeed.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/PrefetchPolicy.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/PreparedSlot.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/Probe.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/RemoteVideo.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/RequestScope.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/Signer.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/VendorConstants.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/ViewingTools.kt
sources/hongguoTV/kotlin-tv/core/src/main/kotlin/com/hongguotv/core/Watching.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/AppUpdatesTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/ContentRepositoryTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/FasterBrowsingTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/LatestWriteQueueTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/LibraryBackupTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/LibraryIndexTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/LibraryTransferServerTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/LowEndPlaybackTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/MediaCryptoTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/PhoneSearchServerTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/PlaybackComfortTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/PlaybackSpeedTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/SignerTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/ViewingToolsTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/kotlin/com/hongguotv/core/WatchingTest.kt
sources/hongguoTV/kotlin-tv/core/src/test/resources/signing.json
sources/hongguoTV/kotlin-tv/DELIVERY.md
sources/hongguoTV/kotlin-tv/distribution/publish-tv-update.py
sources/hongguoTV/kotlin-tv/distribution/release.yml
sources/hongguoTV/kotlin-tv/gradle/wrapper/gradle-wrapper.jar
sources/hongguoTV/kotlin-tv/gradle/wrapper/gradle-wrapper.properties
sources/hongguoTV/kotlin-tv/gradle.properties
sources/hongguoTV/kotlin-tv/gradlew
sources/hongguoTV/kotlin-tv/gradlew.bat
sources/hongguoTV/kotlin-tv/LICENSE
sources/hongguoTV/kotlin-tv/NOTICE.md
sources/hongguoTV/kotlin-tv/README.md
sources/hongguoTV/kotlin-tv/RELEASE_0.3.0.md
sources/hongguoTV/kotlin-tv/RELEASE_0.4.0.md
sources/hongguoTV/kotlin-tv/RELEASE_0.5.0.md
sources/hongguoTV/kotlin-tv/RELEASE_0.6.0.md
sources/hongguoTV/kotlin-tv/RELEASE_0.7.0.md
sources/hongguoTV/kotlin-tv/RELEASE_0.8.0.md
sources/hongguoTV/kotlin-tv/RELEASE_0.9.0.md
sources/hongguoTV/kotlin-tv/settings.gradle.kts
sources/hongguoTV/kotlin-tv/tools/signing-oracle.cjs
sources/hongguoTV/kotlin-tv/tools/verify-comfort-evidence.py
sources/hongguoTV/kotlin-tv/tools/verify-comic-ranking-evidence.py
sources/hongguoTV/kotlin-tv/tools/verify-comic-speed-evidence.py
sources/hongguoTV/kotlin-tv/tools/verify-convenience-evidence.py
sources/hongguoTV/kotlin-tv/tools/verify-discovery-evidence.py
sources/hongguoTV/kotlin-tv/tools/verify-interaction-evidence.py
sources/hongguoTV/kotlin-tv/tools/verify-low-end-evidence.py
sources/hongguoTV/kotlin-tv/tools/verify-tv-evidence.py
sources/hongguoTV/kotlin-tv/tools/verify-viewing-evidence.py
sources/hongguoTV/kotlin-tv/tools/verify-watching-evidence.py
sources/hongguoTV/LICENSE
sources/hongguoTV/metro.config.js
sources/hongguoTV/package-lock.json
sources/hongguoTV/package.json
sources/hongguoTV/README.md
sources/hongguoTV/scripts/build-android.sh
sources/hongguoTV/scripts/build-kotlin.sh
sources/hongguoTV/scripts/probe.mjs
sources/hongguoTV/scripts/smoke-docker.sh
sources/hongguoTV/scripts/sync-kotlin-public.py
sources/hongguoTV/server/compose.yaml
sources/hongguoTV/server/Dockerfile
sources/hongguoTV/server/healthcheck.mjs
sources/hongguoTV/server/http.mjs
sources/hongguoTV/server/index.mjs
sources/hongguoTV/server/package-lock.json
sources/hongguoTV/server/package.json
sources/hongguoTV/server/provider.mjs
sources/hongguoTV/server/vendor/hongguo.cjs
sources/hongguoTV/server/vendor/LICENSE.drpys
sources/hongguoTV/server/vendor/LICENSE.template-tv
sources/hongguoTV/server/vendor/NOTICE.md
sources/hongguoTV/src/data/provider.ts
sources/hongguoTV/src/data/storage.ts
sources/hongguoTV/src/data/useCatalog.ts
sources/hongguoTV/src/domain/model.ts
sources/hongguoTV/src/ui/components.tsx
sources/hongguoTV/src/ui/Player.tsx
sources/hongguoTV/src/ui/tv/DetailTV.tsx
sources/hongguoTV/src/ui/tv/layout.ts
sources/hongguoTV/src/ui/tv/TVGrid.tsx
sources/hongguoTV/tests/domain.test.ts
sources/hongguoTV/tests/server.test.mjs
sources/hongguoTV/tests/tv.test.ts
sources/hongguoTV/tsconfig.json
```
