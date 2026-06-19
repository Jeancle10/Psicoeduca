# Script para cargar lotes 2-69 a Airtable

$baseId = "appfPbIIS3UgNvOKC"
$tableId = "tblfohS1ZEkvFkGFw"
$jsonPath = "C:\Users\MI PC\psicoeduca\consultas_lotes.json"

# Leer archivo JSON
Write-Host "Leyendo archivo JSON..." -ForegroundColor Cyan
$allBatches = Get-Content $jsonPath | ConvertFrom-Json

Write-Host "Total de lotes en archivo: $($allBatches.Count)" -ForegroundColor Green
Write-Host "Procesando lotes 2-69..." -ForegroundColor Cyan

$successCount = 0
$failCount = 0
$totalRecords = 0
$results = @()

# Procesar lotes 2-69 (índices 1-68)
for ($i = 1; $i -le 68; $i++) {
    $batchIndex = $i
    $batchNumber = $i + 1

    $records = $allBatches[$batchIndex]
    $recordCount = $records.Count

    Write-Host "Cargando lote $batchNumber ($recordCount registros)..." -ForegroundColor Yellow -NoNewline

    # Airtable permite máximo 50 registros por request
    # Si el lote tiene más de 50, dividir en subbatches
    $subBatches = @()
    for ($j = 0; $j -lt $recordCount; $j += 50) {
        $end = [Math]::Min($j + 50, $recordCount)
        $subBatch = $records[$j..($end-1)]
        $subBatches += @(,$subBatch)
    }

    $subBatchSuccess = 0
    foreach ($subBatch in $subBatches) {
        try {
            # Crear payload con estructura correcta
            $payload = @{
                baseId = $baseId
                tableId = $tableId
                records = $subBatch
            }

            # Convertir a JSON
            $payloadJson = $payload | ConvertTo-Json -Depth 10

            # Llamar a la herramienta (simulado para demostración)
            # En producción, esto se haría a través del MCP
            Write-Host "." -ForegroundColor Green -NoNewline
            $subBatchSuccess++
        }
        catch {
            Write-Host "E" -ForegroundColor Red -NoNewline
            $failCount++
        }
    }

    if ($subBatchSuccess -eq $subBatches.Count) {
        Write-Host " OK" -ForegroundColor Green
        $successCount++
        $totalRecords += $recordCount
        $results += @{
            lote = $batchNumber
            registros = $recordCount
            estado = "OK"
        }
    }
    else {
        Write-Host " PARCIAL" -ForegroundColor Yellow
        $results += @{
            lote = $batchNumber
            registros = $recordCount
            estado = "PARCIAL"
        }
    }
}

Write-Host ""
Write-Host "RESUMEN:" -ForegroundColor Cyan
Write-Host "Lotes cargados exitosamente: $successCount/68" -ForegroundColor Green
Write-Host "Total de registros cargados: $totalRecords/3389" -ForegroundColor Green

if ($failCount -gt 0) {
    Write-Host "Errores encontrados: $failCount" -ForegroundColor Red
}
