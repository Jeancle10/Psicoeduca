#!/usr/bin/env python3
"""
Script simple para cargar todos los lotes de consultas a Airtable
Usa la herramienta MCP de Airtable directamente
"""
import json
import sys

# IDs Airtable
BASE_ID = "appfPbIIS3UgNvOKC"
TABLE_ID = "tblfohS1ZEkvFkGFw"

print("="*70)
print("CARGAR 3,439 CONSULTAS A AIRTABLE")
print("="*70)

# Leer los lotes
print("\n1. Leyendo consultas_lotes.json...")
try:
    with open('consultas_lotes.json', 'r', encoding='utf-8') as f:
        lotes = json.load(f)
    print(f"   OK - {len(lotes)} lotes cargados")
except Exception as e:
    print(f"   ERROR: {e}")
    sys.exit(1)

# Preparar llamadas
print(f"\n2. Preparando {len(lotes)} llamadas a Airtable...")

llamadas = []
total_registros = 0

for lote_idx, registros in enumerate(lotes):
    llamada = {
        "tool": "mcp__claude_ai_Airtable__create_records_for_table",
        "params": {
            "baseId": BASE_ID,
            "tableId": TABLE_ID,
            "records": registros
        },
        "lote": lote_idx + 1,
        "cantidad": len(registros)
    }
    llamadas.append(llamada)
    total_registros += len(registros)

print(f"   OK - {total_registros} registros preparados en {len(llamadas)} llamadas")

# Mostrar información
print(f"\n3. Información de la carga:")
print(f"   - Base ID: {BASE_ID}")
print(f"   - Tabla ID: {TABLE_ID}")
print(f"   - Total registros: {total_registros}")
print(f"   - Total lotes: {len(lotes)}")
print(f"   - Registros por lote: ~50 (último: {len(lotes[-1])})")

# Guardar instrucciones para Claude
print(f"\n4. Próximos pasos:")
print(f"   - Necesito que hagas {len(lotes)} llamadas a mcp__claude_ai_Airtable__create_records_for_table")
print(f"   - Cada una con 50 registros (máximo permitido por Airtable)")
print(f"   - Puedes hacerlas secuencialmente o en pequeños lotes")

# Guardar en JSON para referencia
output = {
    "total_lotes": len(lotes),
    "total_registros": total_registros,
    "base_id": BASE_ID,
    "table_id": TABLE_ID,
    "llamadas_necesarias": [
        {
            "lote": i+1,
            "registros": len(lotes[i]),
            "params": {
                "baseId": BASE_ID,
                "tableId": TABLE_ID,
                "records": lotes[i]
            }
        }
        for i in range(len(lotes))
    ]
}

with open('carga_plan.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\nOK - Plan de carga guardado en: carga_plan.json")
print(f"\n{'='*70}")
print("INSTRUCCIONES PARA CLAUDE:")
print("{'='*70}")
print("""
Lee el archivo carga_plan.json y haz las 69 llamadas a Airtable usando la herramienta:
  mcp__claude_ai_Airtable__create_records_for_table

Para cada lote (i = 0 a 68):
  1. Lee lotes[i] del archivo consultas_lotes.json
  2. Llama a la herramienta con:
     - baseId: "appfPbIIS3UgNvOKC"
     - tableId: "tblfohS1ZEkvFkGFw"
     - records: lotes[i]
  3. Reporta si fue exitoso

Puedes hacerlas en paralelo en grupos de 5-10 para ir mas rapido.
""")
