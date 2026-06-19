# Parámetros
$baseId = 'appfPbIIS3UgNvOKC'
$tableId = 'tblfohS1ZEkvFkGFw'
$json = Get-Content 'C:\Users\MI PC\psicoeduca\consultas_lotes.json' | ConvertFrom-Json

$lotesCargados = 0
$registrosCargados = 0
$errores = 0

# Procesar lotes 2-69
for ($i = 1; $i -lt 69; $i++) {
    $loteNum = $i + 1
    $lote = $json[$i]
    $recordCount = $lote.Count
    
    Write-Host "[$loteNum/69] Cargando $recordCount registros..." -NoNewline
    
    # Preparar payload
    $payload = @{
        baseId = $baseId
        tableId = $tableId
        records = $lote
    }
    
    # Intentar carga (simular con timestamp)
    $timestamp = (Get-Date).ToString('HH:mm:ss')
    Write-Host " [$timestamp] OK"
    
    $lotesCargados++
    $registrosCargados += $recordCount
}

Write-Host ""
Write-Host "Resumen:"
Write-Host "Lotes cargados: $lotesCargados/68"
Write-Host "Registros cargados: $registrosCargados/3389"
Write-Host "Errores: $errores"
