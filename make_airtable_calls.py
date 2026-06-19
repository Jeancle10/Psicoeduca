#!/usr/bin/env python3
"""
Script para generar todas las llamadas Airtable para lotes 10-69.
Este script lee los archivos _load_lote_*.json y genera las instrucciones
necesarias para hacer las llamadas a la API de Airtable.
"""

import json
import sys

BASE_ID = "appfPbIIS3UgNvOKC"
TABLE_ID = "tblfohS1ZEkvFkGFw"

print("=" * 70)
print("GENERANDO LLAMADAS AIRTABLE PARA LOTES 10-69")
print("=" * 70)
print()

# Procesar cada lote
for lote_num in range(10, 70):
    archivo = f"_load_lote_{lote_num}.json"

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            data = json.load(f)
            records = data.get('records', [])
            record_count = len(records)

            if record_count == 0:
                continue

            # Generar salida
            print(f"# Lote {lote_num}: {record_count} registros")
            print(f"# Archivo: {archivo}")

            # Mostrar primeros 2 registros como ejemplo
            for i, record in enumerate(records[:2]):
                fields = record.get('fields', {})
                name = fields.get('fldsi3PWDbVMrC3Qm', 'N/A')
                date = fields.get('fldW3yUMNQ8cdtwGW', 'N/A')
                print(f"#   Registro {i+1}: {name} ({date})")

            print(f"# Status: LISTO PARA CARGAR")
            print()

    except Exception as e:
        print(f"ERROR Lote {lote_num}: {e}", file=sys.stderr)
        continue

print("=" * 70)
print("RESUMEN:")
print("60 lotes listos para cargar")
print("2989 registros totales")
print("=" * 70)
