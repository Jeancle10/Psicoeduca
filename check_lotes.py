import json
import sys

# Cargar archivo de lotes
with open('consultas_lotes.json', 'r', encoding='utf-8') as f:
    lotes = json.load(f)

# Procesar lotes 24-68
print(f"Total de lotes en archivo: {len(lotes)}")
print(f"Procesando lotes 24-68 ({69-24} lotes)")
print(f"Cada lote tiene {len(lotes[24])} registros")
print(f"Total a cargar: {sum(len(lotes[i]) for i in range(24, 69))} registros")
