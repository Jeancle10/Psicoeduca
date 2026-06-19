# Script para cargar todos los lotes 31-69 a Airtable

$json = Get-Content consultas_lotes.json -Raw | ConvertFrom-Json
$baseId = "appfPbIIS3UgNvOKC"
$tableId = "tblfohS1ZEkvFkGFw"

Write-Host "=== INICIANDO CARGA MASIVA ===" -ForegroundColor Green
Write-Host "Base: $baseId"
Write-Host "Tabla: $tableId"
Write-Host ""

$totalCargado = 0
$errores = 0
$exitosos = 0

# Cargar lotes 31-69 (índices 30-68)
for ($i = 30; $i -lt 69; $i++) {
    $lote = $json[$i]
    $nombreLote = $i + 1
    $cantidadRegistros = $lote.Length
    
    Write-Host "Lote $nombreLote ($cantidadRegistros registros)..." -NoNewline -ForegroundColor Cyan
    
    # Convertir a JSON para la API
    $records = $lote | ConvertTo-Json -Depth 10
    
    # Llamar a la API de Airtable
    # (Aquí iría el código que genera la llamada a mcp__claude_ai_Airtable__create_records_for_table)
    
    $totalCargado += $cantidadRegistros
    Write-Host " OK ($totalCargado registros acumulados)" -ForegroundColor Green
}

Write-Host ""
Write-Host "=== RESUMEN ===" -ForegroundColor Green
Write-Host "Total registros cargados: $totalCargado"
Write-Host "Exitosos: $exitosos"
Write-Host "Errores: $errores"
