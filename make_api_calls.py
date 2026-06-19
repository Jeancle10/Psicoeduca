#!/usr/bin/env python3
"""
Este script genera todas las llamadas a Airtable necesarias para los lotes 10-69.
Imprime los comandos que pueden ser ejecutados con la herramienta mcp__claude_ai_Airtable__create_records_for_table.
"""

import json
import sys

# IDs de Airtable
BASE_ID = "appfPbIIS3UgNvOKC"
TABLE_ID = "tblfohS1ZEkvFkGFw"

# Cargar todos los lotes
with open('consultas_lotes.json', 'r', encoding='utf-8') as f:
    all_lotes = json.load(f)

# Procesar lotes 10-69 (índices 9-68)
print("#!/bin/bash")
print("# Script de carga de lotes 10-69 a Airtable")
print("# Generado automáticamente por make_api_calls.py")
print("")

for lote_idx in range(9, 69):  # índices 9-68 = lotes 10-69
    lote_num = lote_idx + 1
    lote_data = all_lotes[lote_idx]

    if not isinstance(lote_data, list):
        print(f"# ERROR: Lote {lote_num} no es un array", file=sys.stderr)
        continue

    record_count = len(lote_data)

    if record_count > 50:
        print(f"# ADVERTENCIA: Lote {lote_num} tiene {record_count} registros", file=sys.stderr)
        continue

    # Generar el JSON para el lote
    lote_json = json.dumps(lote_data, ensure_ascii=False)

    print(f"# Lote {lote_num}: {record_count} registros")
    print(f"echo 'Cargando lote {lote_num}...'")
    print(f"curl -X POST 'https://api.airtable.com/v1/bases/{BASE_ID}/tables/{TABLE_ID}/records' \\")
    print(f"  -H 'Authorization: Bearer YOUR_TOKEN' \\")
    print(f"  -H 'Content-Type: application/json' \\")
    print(f"  -d '{{\"records\": {lote_json}}}'")
    print("")

print("echo 'Carga completada'")
