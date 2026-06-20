#!/usr/bin/env python3
"""
Script para cargar los lotes 56-69 finales (637 registros)
"""
import json
import sys

BASE_ID = "appfPbIIS3UgNvOKC"
TABLE_ID = "tblfohS1ZEkvFkGFw"

print("=" * 70)
print("CARGAR LOTES 56-69 (637 REGISTROS FINALES)")
print("=" * 70)

# Leer consultas_lotes.json
print("\n1. Leyendo consultas_lotes.json...")
try:
    with open('consultas_lotes.json', 'r', encoding='utf-8') as f:
        lotes = json.load(f)
    print(f"   OK - {len(lotes)} lotes totales en archivo")
except Exception as e:
    print(f"   ERROR: {e}")
    sys.exit(1)

# Extraer lotes 56-69 (índices 55-68)
print("\n2. Extrayendo lotes 56-69...")
lotes_finales = lotes[55:]  # índices 55-68 = lotes 56-69
print(f"   OK - {len(lotes_finales)} lotes a cargar")

# Contar registros
total_regs = sum(len(lote) for lote in lotes_finales)
print(f"   Total registros: {total_regs}")

# Preparar llamadas
print(f"\n3. Información de carga:")
print(f"   - Base ID: {BASE_ID}")
print(f"   - Tabla ID: {TABLE_ID}")
print(f"   - Lotes: 56-69 ({len(lotes_finales)} lotes)")
print(f"   - Registros finales: {total_regs}")
print(f"   - Registros actuales en BD: 2,802")
print(f"   - Total cuando termine: {2802 + total_regs}")

# Guardar instrucciones
instrucciones = []
for idx, lote in enumerate(lotes_finales):
    lote_num = 56 + idx
    instrucciones.append({
        "lote": lote_num,
        "registros": len(lote),
        "baseId": BASE_ID,
        "tableId": TABLE_ID,
        "records": lote
    })

print(f"\n4. Preparando carga en paralelo...")
print(f"   Grupos de carga sugeridos:")
print(f"   - Grupo 1 (lotes 56-60): {sum(len(lotes[i]) for i in range(55,60))} regs")
print(f"   - Grupo 2 (lotes 61-65): {sum(len(lotes[i]) for i in range(60,65))} regs")
print(f"   - Grupo 3 (lotes 66-69): {sum(len(lotes[i]) for i in range(65,69))} regs")

# Guardar para referencia
with open('lotes_finales_instrucciones.json', 'w', encoding='utf-8') as f:
    json.dump(instrucciones, f, ensure_ascii=False, indent=2)

print(f"\nOK - Instrucciones guardadas en: lotes_finales_instrucciones.json")
print(f"\n{'='*70}")
print("PRÓXIMO PASO:")
print("="*70)
print("""
Llamaré a Airtable 3 veces en paralelo:
1. Lotes 56-60 (6 pasos hacia lotes 56-60)
2. Lotes 61-65
3. Lotes 66-69

Resultado esperado: 2,802 + 637 = 3,439 registros totales ✅
""")
