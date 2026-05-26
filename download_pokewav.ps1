$destDir = "C:\Users\sokuryou10\.gemini\tmp\system32\pokewav"
if (!(Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir -Force
}

$htmlFile = "C:\Users\sokuryou10\.gemini\tmp\system32\index.html_temp"
$baseUrl = "http://games255.512.jp/pokewav/"

# HTMLから href="../pokewav/xxx.wav" または xxx.mp3 を抽出
$content = Get-Content $htmlFile -Raw
$matches = [regex]::Matches($content, 'href="\.\./pokewav/([^"]+\.(wav|mp3))"')

Write-Host "Found $($matches.Count) files to download."

foreach ($match in $matches) {
    $fileName = $match.Groups[1].Value
    $url = $baseUrl + $fileName
    $outPath = Join-Path $destDir $fileName
    
    if (Test-Path $outPath) {
        Write-Host "Skipping (already exists): $fileName"
        continue
    }

    Write-Host "Downloading $fileName ..."
    try {
        Invoke-WebRequest -Uri $url -OutFile $outPath -TimeoutSec 15 -ErrorAction Stop
    } catch {
        Write-Warning "Failed to download $fileName"
    }
}
Write-Host "All downloads finished."
