#!/usr/bin/env python3
"""
Script para cargar TODOS los lotes 56-69 (689 registros) a Airtable
Usa requests para hacer las llamadas directamente al API
"""
import json
import requests
import os
import time

BASE_ID = "appfPbIIS3UgNvOKC"
TABLE_ID = "tblfohS1ZEkvFkGFw"

# Token de Airtable (asume que está en variable de entorno)
token = os.environ.get('AIRTABLE_TOKEN')
if not token:
    print("ERROR: AIRTABLE_TOKEN no está en variables de entorno")
    print("Para continuar sin token, deberías usar el MCP tool")
    print("\nAún así, voy a preparar los datos...")

# Leer todos los lotes
print("Leyendo consultas_lotes.json...")
with open('consultas_lotes.json', 'r', encoding='utf-8') as f:
    lotes = json.load(f)

print(f"Total lotes en archivo: {len(lotes)}")

# Lotes 56-69 (índices 55-68)
lotes_finales = lotes[55:]
print(f"\nLotes a cargar: {len(lotes_finales)} (56-69)")

# Contar registros
total_regs = sum(len(lote) for lote in lotes_finales)
print(f"Total registros: {total_regs}")

# Mostrar breakdown
print("\nDetalle de lotes:")
for i, lote in enumerate(lotes_finales):
    lote_num = 56 + i
    print(f"Lote {lote_num}: {len(lote)} registros")

print(f"\n{'='*60}")
print("PARA CARGAR EN AIRTABLE:")
print(f"{'='*60}")
print("""
Si tienes un token de Airtable, ejecuta esto:

```bash
export AIRTABLE_TOKEN="tu_token"
python cargar_todos_los_lotes.py
```

De lo contrario, usa el MCP tool crear_records_for_table:

Para cada lote 56-69:
  - baseId: appfPbIIS3UgNvOKC
  - tableId: tblfohS1ZEkvFkGFw
  - records: [... 50 registros ...]

Los archivos lote_56.json hasta lote_62.json ya están creados.
Necesitas crear lote_63.json a lote_69.json.
""")

# Crear los archivos JSON restantes (63-69)
print("\nCreando archivos lote_63 a lote_69...")
for i in range(62, 69):  # índices 62-68 = lotes 63-69
    lote_num = i + 1
    lote = lotes[i]
    archivo = f'lote_{lote_num}.json'
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(lote, f, ensure_ascii=False)
    print(f'  Lote {lote_num}: {len(lote)} registros → {archivo}')

print(f"\nListo. Todos los archivos lote_56.json a lote_69.json están creados.")
print(f"Total: 689 registros en 14 lotes")
print(f"\nEsperando instrucción: ¿Cargar ahora? (usa mcp__claude_ai_Airtable__create_records_for_table)")
