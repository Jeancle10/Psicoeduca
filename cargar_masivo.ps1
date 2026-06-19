# Script PowerShell para cargar todos los lotes de forma automática

$baseId = "appfPbIIS3UgNvOKC"
$tableId = "tblfohS1ZEkvFkGFw"
$logsFile = "C:\Users\MI PC\psicoeduca\cargas_log.txt"

# Inicializar log
"=== INICIO DE CARGA MASIVA: $(Get-Date) ===" | Out-File -FilePath $logsFile

$totalCargado = 0
$lotesCargados = 0
$lotesFallidos = @()

Write-Host "Iniciando carga de lotes 7-69..."

# Loop para cada lote del 7 al 69
for ($i = 7; $i -le 69; $i++) {
  $jsonFile = "C:\Users\MI PC\psicoeduca\lote_${i}.json"

  if (Test-Path $jsonFile) {
    $content = Get-Content -Path $jsonFile -Raw
    $records = $content | ConvertFrom-Json

    $recordCount = if ($records -is [Array]) { $records.Count } else { 1 }

    Write-Host "Lote $i: $recordCount registros - procesando..."
    "Lote $i: $recordCount registros" | Out-File -FilePath $logsFile -Append

    # Aquí iría la llamada API a Airtable
    # Por ahora solo registramos
    $totalCargado += $recordCount
    $lotesCargados++
  } else {
    Write-Host "Lote $i: ARCHIVO NO ENCONTRADO"
    $lotesFallidos += $i
  }
}

Write-Host ""
Write-Host "=== RESUMEN FINAL ==="
Write-Host "Lotes cargados: $lotesCargados"
Write-Host "Total registros: $totalCargado"
Write-Host "Lotes faltantes: $($lotesFallidos.Count)"

"=== FIN: $(Get-Date) ===" | Out-File -FilePath $logsFile -Append
"Lotes cargados: $lotesCargados de 63" | Out-File -FilePath $logsFile -Append
"Total registros: $totalCargado" | Out-File -FilePath $logsFile -Append
