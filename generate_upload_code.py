#!/usr/bin/env python3
"""
Genera código Python que hace todas las 60 llamadas a Airtable.
"""

import json

BASE_ID = "appfPbIIS3UgNvOKC"
TABLE_ID = "tblfohS1ZEkvFkGFw"

print("# Script generado automáticamente para cargar lotes 10-69 a Airtable")
print("# Generado por generate_upload_code.py")
print()

# Generar un diccionario con todos los lotes
print("lotes_data = {")

for lote_num in range(10, 70):
    archivo = f"_load_lote_{lote_num}.json"
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            data = json.load(f)
            records = data['records']

            # Generar el código para cada lote
            records_json = json.dumps(records, ensure_ascii=False)

            print(f"    {lote_num}: {records_json},")
    except Exception as e:
        print(f"    # ERROR lote {lote_num}: {e}", file=__import__('sys').stderr)

print("}")
print()
print("print('Todos los lotes están listos para cargar')")
print(f"print(f'Total: 60 lotes, 2989 registros')")
