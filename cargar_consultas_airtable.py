#!/usr/bin/env python3
"""
Carga todos los registros de consultas_historico.json a Airtable
en lotes de 50 (límite máximo por request)
"""
import json
import subprocess
import sys

# Cargar datos
with open('consultas_historico.json', encoding='utf-8') as f:
    consultas = json.load(f)

print(f"Total registros a cargar: {len(consultas)}")

# IDs de Airtable
BASE_ID = "appfPbIIS3UgNvOKC"
TABLE_ID = "tblfohS1ZEkvFkGFw"
FIELD_NOMBRE = "fldsi3PWDbVMrC3Qm"
FIELD_FECHA = "fldW3yUMNQ8cdtwGW"
FIELD_AÑO = "fldqq7Nb8ry0IEU9R"
FIELD_MES = "fldyzq91v6Jwu4y7D"
FIELD_MODALIDAD = "fldVaG6ldSL2CX61V"

# Dividir en lotes de 50
lote_size = 50
total_lotes = (len(consultas) + lote_size - 1) // lote_size

print(f"Cargaré en {total_lotes} lotes de hasta {lote_size} registros cada uno\n")

for lote_idx in range(total_lotes):
    inicio = lote_idx * lote_size
    fin = min(inicio + lote_size, len(consultas))
    lote = consultas[inicio:fin]

    # Crear registros en formato Airtable
    registros = []
    for consulta in lote:
        registro = {
            "fields": {
                FIELD_NOMBRE: consulta['nombre'],
                FIELD_FECHA: consulta['fecha'],
                FIELD_AÑO: consulta['año'],
                FIELD_MES: consulta['mes_nombre'],
                FIELD_MODALIDAD: consulta['modalidad']
            }
        }
        registros.append(registro)

    # Crear comando Python para ejecutar la herramienta
    script = f"""
import sys
sys.path.insert(0, '{__file__}')

# Crear la llamada a través de una herramienta MCP simulada
records = {json.dumps(registros)}
print(f"Lote {{lote_idx + 1}}/{total_lotes}: Cargando {{len(records)}} registros ({{inicio}}-{{fin}})...")

# Aquí irá la llamada a la herramienta Airtable
# Por ahora solo preparamos los datos
print("Datos preparados para cargar")
"""

    print(f"Lote {lote_idx + 1}/{total_lotes}: {len(lote)} registros ({inicio}-{fin})")

# Guardar los registros en un formato que pueda usar
with open('consultas_lotes.json', 'w', encoding='utf-8') as f:
    # Guardar en lotes
    lotes = []
    for lote_idx in range(total_lotes):
        inicio = lote_idx * lote_size
        fin = min(inicio + lote_size, len(consultas))
        lote = consultas[inicio:fin]

        registros = []
        for consulta in lote:
            registro = {
                "fields": {
                    FIELD_NOMBRE: consulta['nombre'],
                    FIELD_FECHA: consulta['fecha'],
                    FIELD_AÑO: consulta['año'],
                    FIELD_MES: consulta['mes_nombre'],
                    FIELD_MODALIDAD: consulta['modalidad']
                }
            }
            registros.append(registro)
        lotes.append(registros)

    json.dump(lotes, f, ensure_ascii=False, indent=2)

print(f"\nDatos preparados en: consultas_lotes.json")
print(f"Ahora usaremos la herramienta Airtable para cargar {total_lotes} lotes...")
