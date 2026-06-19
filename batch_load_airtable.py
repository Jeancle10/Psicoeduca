#!/usr/bin/env python3
"""
Script para cargar todos los lotes 10-69 a Airtable usando la API de MCP.
"""

import json
import sys
import time

# IDs de Airtable
BASE_ID = "appfPbIIS3UgNvOKC"
TABLE_ID = "tblfohS1ZEkvFkGFw"

# Cargar todos los lotes del archivo principal
print("Cargando archivo de lotes...")
with open('consultas_lotes.json', 'r', encoding='utf-8') as f:
    all_lotes = json.load(f)

print(f"Total de lotes cargados: {len(all_lotes)}")
print()

# Procesar lotes 10-69 (índices 9-68)
print("=" * 60)
print("COMENZANDO CARGA DE LOTES 10-69")
print("=" * 60)
print()

successful = 0
failed = 0
total_records = 0

for lote_idx in range(9, 69):  # índices 9-68 = lotes 10-69
    lote_num = lote_idx + 1
    lote_data = all_lotes[lote_idx]

    if not isinstance(lote_data, list):
        print(f"[ERROR] Lote {lote_num}: no es un array")
        failed += 1
        continue

    record_count = len(lote_data)

    if record_count > 50:
        print(f"[ERROR] Lote {lote_num}: {record_count} registros (máx 50)")
        failed += 1
        continue

    if record_count == 0:
        print(f"[SKIP] Lote {lote_num}: vacío")
        continue

    # Guardar datos a archivo temporal para referencia
    lote_file = f"_load_lote_{lote_num}.json"
    with open(lote_file, 'w', encoding='utf-8') as f:
        json.dump({
            "baseId": BASE_ID,
            "tableId": TABLE_ID,
            "records": lote_data
        }, f, ensure_ascii=False, indent=2)

    print(f"[{lote_num:02d}] {record_count} registros - archivo: {lote_file}")
    successful += 1
    total_records += record_count

print()
print("=" * 60)
print(f"RESUMEN:")
print(f"  Lotes listos: {successful}")
print(f"  Registros totales: {total_records}")
print(f"  Errores: {failed}")
print("=" * 60)

if successful == 60 and total_records == 2989:
    print("[OK] Todos los lotes están listos para cargar")
    print(f"[INFO] Ahora puedes hacer las llamadas a Airtable")
    sys.exit(0)
else:
    print(f"[WARN] Discrepancia: {successful} lotes, {total_records} registros")
    sys.exit(1)
