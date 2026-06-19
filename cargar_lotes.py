#!/usr/bin/env python3
import json
import os

# Configuración
BASE_DIR = r"C:\Users\MI PC\psicoeduca"
BASE_ID = "appfPbIIS3UgNvOKC"
TABLE_ID = "tblfohS1ZEkvFkGFw"

# Procesar cada lote
results = []
total_records = 0

for i in range(2, 70):  # Lotes 2-69
    file_path = os.path.join(BASE_DIR, f"payload_lote_{i}.json")
    
    if not os.path.exists(file_path):
        results.append(f"Lote {i}: archivo no encontrado")
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            records = json.load(f)
        
        # Asegurar que es un array
        if not isinstance(records, list):
            records = [records]
        
        count = len(records)
        total_records += count
        results.append(f"Lote {i}: {count} registros - LISTO")
        
    except Exception as e:
        results.append(f"Lote {i}: ERROR - {str(e)}")

# Imprimir resultados
print("=== VERIFICACION DE LOTES 2-69 ===")
for result in results[-20:]:  # Últimos 20
    print(result)

print(f"\nTotal de registros en lotes 2-69: {total_records}")
print(f"Total esperado: {50*68 - 11} (68 lotes x 50 - 11 del último lote)")
