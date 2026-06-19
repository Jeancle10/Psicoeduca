#!/usr/bin/env python3
import json
import sys

# Cargar el archivo de lotes
with open('consultas_lotes.json', 'r') as f:
    all_lotes = json.load(f)

print(f"Total de lotes en archivo: {len(all_lotes)}")

# Procesar lotes 9-69 (índices 8-68)
for lote_idx in range(8, 69):  # 8 to 68 inclusive = lotes 9-69
    lote_num = lote_idx + 1
    lote_data = all_lotes[lote_idx]

    # El lote_data es un array de registros
    if isinstance(lote_data, list):
        record_count = len(lote_data)
    else:
        record_count = 1

    print(f"Lote {lote_num}: {record_count} registros")

    # Guardar cada lote en un archivo JSON temporal
    temp_file = f"temp_lote_{lote_num}.json"
    with open(temp_file, 'w') as f:
        json.dump(lote_data, f, indent=2)

    print(f"  - Guardado en {temp_file}")

print("\nTodos los lotes han sido exportados a archivos temporales.")
