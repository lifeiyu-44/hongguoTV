$ErrorActionPreference = 'Stop'
$archiveRoot = Split-Path $PSScriptRoot -Parent
$manifest = Get-Content -LiteralPath (Join-Path $archiveRoot 'verification/artifacts.json') -Raw -Encoding UTF8 | ConvertFrom-Json
foreach ($item in $manifest) {
    $filePath = Join-Path $archiveRoot $item.path
    $actual = Get-FileHash -LiteralPath $filePath -Algorithm SHA256
    if ($actual.Hash -ne $item.sha256 -or (Get-Item -LiteralPath $filePath).Length -ne $item.size) {
        throw ('Checksum or size mismatch: ' + $item.path)
    }
    Write-Output ('OK ' + $item.path)
}
