param([switch]$Release)
$ErrorActionPreference = 'Stop'
$archiveRoot = Split-Path $PSScriptRoot -Parent
$project = Join-Path $archiveRoot 'sources/hongguoTV/kotlin-tv'
if (-not $env:JAVA_HOME -or -not $env:ANDROID_HOME) {
    throw 'Set JAVA_HOME to JDK 17 and ANDROID_HOME to an Android SDK with platform 36 and build-tools 36.0.0.'
}
$variant = 'Debug'
if ($Release) {
    foreach ($key in @('HONGGUOTV_KEYSTORE', 'HONGGUOTV_STORE_PASSWORD', 'HONGGUOTV_KEY_ALIAS', 'HONGGUOTV_KEY_PASSWORD')) {
        if (-not [Environment]::GetEnvironmentVariable($key)) { throw ('Set signing variable: ' + $key) }
    }
    $variant = 'Release'
}
& (Join-Path $project 'gradlew.bat') -p $project :core:test (':app:lint' + $variant) (':app:assemble' + $variant) --console=plain
if ($LASTEXITCODE -ne 0) { throw ('Gradle failed: ' + $LASTEXITCODE) }
Write-Output ('APK output: ' + (Join-Path $project ('app/build/outputs/apk/' + $variant.ToLowerInvariant())))
Write-Output 'Signing keys and local configuration must stay outside this Git repository.'
