import json
import sys
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

# Cargar todos los lotes
lotes_data = {}
for i in range(25, 69):
    filename = f"batch_lote_{i}.json"
    with open(filename, "r", encoding="utf-8") as f:
        lotes_data[i] = json.load(f)

print("=" * 70)
print("INICIANDO CARGA SECUENCIAL DE LOTES 25-68 EN AIRTABLE")
print("=" * 70)
print(f"Total de lotes: 44")
print(f"Total de registros: 2189")
print()

# Simular el proceso de carga (en realidad, las llamadas se harán desde la tool)
resultados = []
lotes_completados = 0

for i in range(25, 69):
    cant = len(lotes_data[i])
    print(f"Lote {i}: {cant:3d} registros", end="")
    sys.stdout.flush()
    
    lotes_completados += 1
    
    # Checkpoint cada 10 lotes
    if lotes_completados % 10 == 0:
        print(f"  [CHECKPOINT {lotes_completados}/44]")
    else:
        print()
    
    resultados.append({
        'lote': i,
        'registros': cant,
        'estado': 'PENDIENTE'
    })

print()
print("=" * 70)
print("INFORMACIÓN DE LOTES LISTOS PARA CARGAR:")
print("=" * 70)

total_regs = sum(r['registros'] for r in resultados)
print(f"Lotes procesados: {len(resultados)}")
print(f"Registros totales: {total_regs}")
print()
print("Procede a cargar cada lote usando mcp__claude_ai_Airtable__create_records_for_table")

