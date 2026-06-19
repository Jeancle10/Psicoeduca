#!/usr/bin/env python3
# Procesar datos de consultas 2022 (ago-dic)

import re
from collections import defaultdict

# AGOSTO 2022 (ya procesado)
agosto = {
    'mes': 'Agosto',
    'año': 2022,
    'consultas': 51,
    'consultantes': 27,
    'canceladas': 0,
    'tasa_cancelacion': 0
}

# SEPTIEMBRE 2022
# Extrayendo todos los nombres no vacíos y no "-"
sept_data = """
01/09: Naoto Goto, Julia Díaz
03/09: Naoto Goto, Gisela González, Belén González, Nico Zapata, Marcos Ortiz, Mauro López, Marcos Bar, Flor González
06/09: Marimar Lopez, Julia Diaz, Jimena Ortiz, Eilyn Rubiños, Nahiara Trinidad, Mayra Pereira, Paz Salomón, Jimena Cabral
08/09: Luis Elizeche, Nicolas Zapata, Sadam Medina, Mabel Drakeford, Fanny Ayala, Samara Sosa
10/09: Hugo Lopez
13/09: Marimar Lopez, Julia Diaz, Dahiana Rojas, Eilyn Rubiños, Jose Palacios, Paz Salomon, Fanny Ayala, Naoto Goto
15/09: Elea Ramirez, Sadam Medina, Nicolas Zapata, Marcos Bar, Lujan Amarilla
17/09: Gisela Gonzalez, Belen Gonzalez
27/09: Marimar Lopez, Mario Santander, Jimena Ortiz, Nicolas Zapata, Naoto Goto, Nahiara Trinidad, Paz Salomon, Fanny Ayala
29/09: Hugo Lopez, Marcos Bar
"""

# OCTUBRE 2022
oct_data = """
01/10: Gisela Gonzalez, Belen Gonzalez
04/10: Luis Elizeche, Clarisa Hermosilla
06/10: Marimar Lopez, Julia Diaz
08/10: Pathi Cabañas, Maga Pereira, Paola Ortiz, Nicolas Zapata, Hugo Lopez, Jose Palacios, Paz Salomon, Mayra Pereira, Jovita Robles, Elea Ramirez, Papas de Nahi, Samara Sosa
10/10: Mario Santander, Isaac Peralta, Eilyn Rubiños, Naoto Goto, Elena Sachero, Laura Moreno, Jovita Robles, Marimar López
11/10: Clari Hermosilla, Maga Pereira, Fabián Ferreira
13/10: Marimar Lopez, Hugo Depps, Nahiara Trinidad
15/10: Paola Ortiz, Hugo Depps, Luis Elizeche, Nicolas Zapata, Naoto Goto, Ricardo Flores, Melanie Ramirez, Fanny Ayala, Mirtha de Palacios, Samara Sosa
17/10: Claudia Orrego
18/10: Mario Santander, Clari Hermosilla
20/10: Hugo López, Gisela González, Fanny Ayala, Mirtha de Palacios
22/10: Elea Ramirez, Lujan Amarilla
24/10: Claudia Orrego
25/10: Mario Santander, Nicolas Zapata
27/10: Marimar Lopez, Hugo Lopez
31/10: (vacío)
"""

# NOVIEMBRE 2022
nov_data = """
01/11: Mario Santander
03/11: Luis Elizeche, Fabián Ferreira, Paz Salomón, Naoto Goto, Belen González, Fanny Ayala
05/11: José Matto
07/11: Mario Santander, Isaac Peralta, Berni, Luis Trinidad, Ricardo, Osvaldo J Palacios
08/11: Mario Santander, Maria Jose Osorio, Patricia Cabañas, Naoto Goto, José Matto, Melanie Ramirez, Osvaldo Palacios
10/11: Marimar Lopez, Marcos Bar, Nicolas Zapata, Milena Ojeda virtual, Samara Sosa
12/11: Ele Ramirez, Marcos Bar, Eilyn Rubiños
14/11: Mario Santander, Clarisa Hermosilla virtual, Luis Elizeche, Claudia Orrego, Melanie Ramirez, Paz Salomon
15/11: Marimar Lopez, Mayra Pereira, Maria Jose Osorio, Fabian Ferreira, Nahiara Trinidad, Berni Caballero
17/11: Marimar Lopez, Jose Matto, Hugo López
19/11: Ramón Ferreira, Belén González, Eilyn Rubiños, Fanny Ayala, Sol Benitez
21/11: Mario Santander
22/11: Bruno Perrota, Dahiana Rojas, Mateo Rojas, Fabian Ferreira
24/11: Cristina Cabrera videollamada, Nicolás Zapata
26/11: Nicolás Zapata
28/11: (vacío)
29/11: (vacío)
"""

# DICIEMBRE 2022
dic_data = """
03/12: Patricia Cabañas, belen valinotti, José Matto
05/12: Ramon Ferreira, Maria Alonso, Luz Duarte, Osvaldo Palacios Hijo
06/12: Mario Santander, vt Clarisa Hermosilla, Naoto Goto, Nicolás Zapata, Berni C, Sol Benitez
07/12: Marco Mendoza, Nathalia Serafini, Santiago Ruiz, Bruno perrota, Hugo López, Fernando Elizeche
10/12: Marimar López, Melquiades Alonso, Marco Mendoza, Fabian Ferreira, Hugo López, Paz Amarilla, Sol Benitez
12/12: Mario Santander, Melquiades Alonso, Fernando Santos, Nicolás Zapata, Ricardo Flores
13/12: Mario Santander, Fernando Santos, Nahiara Trinidad, Fanny Ayala, Samara Sosa
15/12: Mayra P, Nathalia Serafini, Bruno perrota, Hugo López, Eilyn Rubiños, Sol Benitez, Fanny Ayala, Lujan Amarilla
17/12: Isaac, Isaac, Belén González, Jimena Cabral, José Matto
19/12: Marimar López
20/12: Melquiades Alonso, Nathalia Serafini, Marco Mendoza, Bruno perrota, Fernando Santos, Nahiara Trinidad, Fanny Ayala
22/12: Luis Elizeche, Eilyn Rubiños
23/12: viernes (no hay datos)
"""

def procesar_mes(mes_data, mes_name):
    """Procesar datos de un mes y retornar stats"""
    # Extraer todos los nombres (excluir "-" y vacíos)
    nombres = []
    lineas = mes_data.strip().split('\n')

    for linea in lineas:
        if linea and ':' in linea:
            # Tomar la parte después del ':'
            partes = linea.split(':', 1)[1]
            # Dividir por coma
            items = [x.strip() for x in partes.split(',')]
            # Agregar si no está vacío y no es "-"
            for item in items:
                if item and item != '-' and item != '(vacío)' and item.lower() != 'viernes (no hay datos)':
                    # Limpiar "virtual", "videollamada", etc.
                    item_limpio = re.sub(r'\s*(virtual|videollamada|vt|de)$', '', item, flags=re.IGNORECASE).strip()
                    if item_limpio and item_limpio != '-':
                        nombres.append(item_limpio)

    # Consultantes distintos (case-insensitive, normalizando)
    nombres_norm = [n.lower().strip() for n in nombres]
    consultantes_distintos = len(set(nombres_norm))
    total_consultas = len(nombres)

    return {
        'mes': mes_name,
        'año': 2022,
        'consultas': total_consultas,
        'consultantes': consultantes_distintos,
        'canceladas': 0,
        'tasa_cancelacion': 0.0
    }

# Procesar todos los meses
sept = procesar_mes(sept_data, 'Septiembre')
oct = procesar_mes(oct_data, 'Octubre')
nov = procesar_mes(nov_data, 'Noviembre')
dic = procesar_mes(dic_data, 'Diciembre')

# Mostrar resultados
print("="*60)
print("ANÁLISIS MENSUAL 2022")
print("="*60)
for mes in [agosto, sept, oct, nov, dic]:
    print(f"\n{mes['mes'].upper()} {mes['año']}")
    print(f"  Consultas totales: {mes['consultas']}")
    print(f"  Consultantes distintos: {mes['consultantes']}")
    print(f"  Canceladas: {mes['canceladas']}")
    print(f"  Tasa cancelación: {mes['tasa_cancelacion']:.0%}")

# Datos para Airtable
datos_airtable = [agosto, sept, oct, nov, dic]
print("\n" + "="*60)
print("DATOS PARA AIRTABLE")
print("="*60)
for d in datos_airtable:
    print(f"{d['mes']} | {d['año']} | {d['consultantes']} | {d['consultas']} | {d['canceladas']} | {d['tasa_cancelacion']:.0%}")
