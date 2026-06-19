#!/usr/bin/env python3
import json
import sys

# Este script genera el JSON necesario para hacer llamadas a Airtable
# para todos los lotes 10-69

# IDs de Airtable
BASE_ID = "appfPbIIS3UgNvOKC"
TABLE_ID = "tblfohS1ZEkvFkGFw"

# Cargar todos los lotes
with open('consultas_lotes.json', 'r', encoding='utf-8') as f:
    all_lotes = json.load(f)

print("=" * 60)
print("GENERANDO COMANDOS AIRTABLE PARA LOTES 10-69")
print("=" * 60)

total_records = 0
successful_lotes = 0

# Procesar lotes 10-69 (índices 9-68)
for lote_idx in range(9, 69):  # índices 9-68 = lotes 10-69
    lote_num = lote_idx + 1
    lote_data = all_lotes[lote_idx]

    # Validar que es un array
    if not isinstance(lote_data, list):
        print(f"ERROR: Lote {lote_num} no es un array")
        continue

    record_count = len(lote_data)

    # Validar que no excede 50 registros
    if record_count > 50:
        print(f"ADVERTENCIA: Lote {lote_num} tiene {record_count} registros (máx 50)")
        print(f"  Se dividirá en múltiples llamadas")

    # Para esta versión, solo reportamos que está listo
    # La llamada real se hará desde Claude Code
    print(f"Lote {lote_num}: {record_count} registros - LISTO")
    total_records += record_count
    successful_lotes += 1

print("=" * 60)
print(f"RESUMEN: {successful_lotes} lotes, {total_records} registros")
print(f"Esperado: 60 lotes, 3039 registros")
print("=" * 60)

# Validar que tenemos los números correctos
if successful_lotes == 60 and total_records == 3039:
    print("VALIDACION: OK - Todos los lotes listos para cargar")
    sys.exit(0)
else:
    print(f"ADVERTENCIA: {successful_lotes} lotes != 60, {total_records} registros != 3039")
    sys.exit(1)
