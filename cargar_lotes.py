import json
import sys

# Cargar el archivo JSON
with open("consultas_lotes.json", "r", encoding="utf-8") as f:
    lotes = json.load(f)

print("=== INFORMACIÓN DE LOTES A CARGAR ===")
print(f"Total de lotes en archivo: {len(lotes)}")
print()

# Verificar lotes 25-68
total_registros = 0
for i in range(25, 69):
    cant = len(lotes[i])
    total_registros += cant
    pos = i - 25 + 1
    print(f"Lote {i}: {cant:3d} registros", end="")
    if pos % 10 == 0:
        print(f"  [CHECKPOINT {pos}/44]")
    else:
        print()

print()
print(f"Total de registros a cargar: {total_registros}")
print()

# Crear archivos JSON para cada lote (en grupos de 5 para procesamiento)
print("=== PREPARANDO ARCHIVOS TEMPORALES ===")
for i in range(25, 69):
    filename = f"batch_lote_{i}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(lotes[i], f)
    print(f"Creado {filename} ({len(lotes[i])} registros)")

print()
print("Todos los archivos están listos para carga a Airtable")
