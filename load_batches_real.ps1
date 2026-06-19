# Script para cargar lotes 2-69 a Airtable
# Parámetros
$baseId = "appfPbIIS3UgNvOKC"
$tableId = "tblfohS1ZEkvFkGFw"
$jsonPath = "C:\Users\MI PC\psicoeduca\consultas_lotes.json"

# Leer archivo JSON
Write-Host "Leyendo archivo JSON..." -ForegroundColor Cyan
$allBatches = Get-Content $jsonPath | ConvertFrom-Json

# Variables de control
$successCount = 0
$failCount = 0
$totalRecords = 0
$results = @()

# Procesar lotes 2-69 (índices 1-68)
Write-Host "Preparando carga de 68 lotes (lotes 2-69)..." -ForegroundColor Cyan
Write-Host ""

$lotsToProcess = @()
for ($i = 1; $i -le 68; $i++) {
    $records = $allBatches[$i]
    $lotNumber = $i + 1

    $lotsToProcess += @{
        number = $lotNumber
        index = $i
        records = $records
        count = $records.Count
    }
}

# Guardar información de lotes para procesar
$lotsToProcess | ConvertTo-Json -Depth 10 | Out-File "C:\Users\MI PC\psicoeduca\lots_metadata.json" -Encoding UTF8

Write-Host "Guardado: lots_metadata.json" -ForegroundColor Green
Write-Host "Total de lotes a cargar: $($lotsToProcess.Count)" -ForegroundColor Green
Write-Host "Total de registros: $(($lotsToProcess | Measure-Object -Property count -Sum).Sum)" -ForegroundColor Green
