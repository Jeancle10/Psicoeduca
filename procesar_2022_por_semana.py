#!/usr/bin/env python3
# Contar consultas POR SEMANA para encontrar diferencias

# OCTUBRE 2022
oct_semanas = {
    'semana 1 (01/10)': """
Gisela Gonzalez, Belen Gonzalez
""",
    'semana 2 (04-08/10)': """
Luis Elizeche, Clarisa Hermosilla,
Marimar Lopez, Julia Diaz, Nicolas Zapata, Hugo Lopez, Jose Palacios, Paz Salomon, Jovita Robles, Papas de Nahi, Samara Sosa,
Pathi Cabañas, Maga Pereira, Paola Ortiz, Mayra Pereira, Elea Ramirez, Samara Sosa
""",
    'semana 3 (10-15/10)': """
Mario Santander, Isaac Peralta, Eilyn Rubiños, Naoto Goto, Elena Sachero, Laura Moreno, Jovita Robles, Marimar López,
Clari Hermosilla, Marimar Lopez, Maga Pereira, Luis Elizeche, Nahiara Trinidad, Ricardo Flores, Mirtha de Palacios, Samara Sosa,
Paola Ortiz, Hugo Depps, Belen Gonzalez, Nicolas Zapata, Naoto Goto, Hugo Lopez, Lujan Amarilla, Jovita Robles, Mirtha de Palacios, Samara Sosa
""",
    'semana 4 (17-22/10)': """
Claudia Orrego, Gisela González, Fanny Ayala, Mirtha de Palacios,
Mario Santander, Clari Hermosilla, Naoto Goto, Hugo López, Gisela González, Fanny Ayala, Mirtha de Palacios,
Marimar Lopez, Hugo Depps, Maga Pereira, Luis Elizeche, Nicolas Zapata, Naoto Goto, Ricardo Flores, Melanie Ramirez, Fanny Ayala, Marcos Bar,
Elea Ramirez, Hugo Depps, Lujan Amarilla, Jovita Robles, Mirtha de Palacios, Samara Sosa
""",
    'semana 5 (24-31/10)': """
Claudia Orrego,
Mario Santander, Nicolas Zapata,
Marimar Lopez, Hugo Lopez,
Isaac Peralta
"""
}

# NOVIEMBRE 2022
nov_semanas = {
    'semana 1 (01-05/11)': """
Mario Santander,
Luis Elizeche, Fabián Ferreira, Paz Salomón, Naoto Goto, Belen González, Fanny Ayala,
José Matto
""",
    'semana 2 (07-12/11)': """
Mario Santander, Isaac Peralta, Berni, Luis Trinidad, Ricardo, Osvaldo J Palacios,
Mario Santander, Maria Jose Osorio, Patricia Cabañas, Naoto Goto, José Matto, Melanie Ramirez, Osvaldo Palacios,
Marimar Lopez, Marcos Bar, Nicolas Zapata, Milena Ojeda virtual, Samara Sosa,
Ele Ramirez, Marcos Bar, Eilyn Rubiños
""",
    'semana 3 (14-19/11)': """
Mario Santander, Clarisa Hermosilla virtual, Luis Elizeche, Claudia Orrego, Melanie Ramirez, Paz Salomon,
Marimar Lopez, Mayra Pereira, Maria Jose Osorio, Fabian Ferreira, Nahiara Trinidad, Berni Caballero,
Marimar Lopez, Jose Matto, Hugo López,
Ramón Ferreira, Belén González, Eilyn Rubiños, Fanny Ayala, Sol Benitez
""",
    'semana 4 (21-26/11)': """
Mario Santander,
Bruno Perrota, Dahiana Rojas, Mateo Rojas, Fabian Ferreira,
Cristina Cabrera videollamada, Nicolás Zapata,
Nicolás Zapata
""",
    'semana 5 (28-30/11)': """
(vacío)
"""
}

# DICIEMBRE 2022
dic_semanas = {
    'semana 1 (03/12)': """
Patricia Cabañas, belen valinotti, José Matto
""",
    'semana 2 (05-10/12)': """
Ramon Ferreira, Maria Alonso, Luz Duarte, Osvaldo Palacios Hijo,
Mario Santander, vt Clarisa Hermosilla, Naoto Goto, Nicolás Zapata, Berni C, Sol Benitez,
Marco Mendoza, Nathalia Serafini, Santiago Ruiz, Bruno perrota, Hugo López, Fernando Elizeche,
Marimar López, Melquiades Alonso, Marco Mendoza, Fabian Ferreira, Hugo López, Paz Amarilla, Sol Benitez
""",
    'semana 3 (12-17/12)': """
Mario Santander, Melquiades Alonso, Fernando Santos, Nicolás Zapata, Ricardo Flores,
Mario Santander, Fernando Santos, Nahiara Trinidad, Fanny Ayala, Samara Sosa,
Mayra P, Nathalia Serafini, Bruno perrota, Hugo López, Eilyn Rubiños, Sol Benitez, Fanny Ayala, Lujan Amarilla,
Isaac, Isaac, Belén González, Jimena Cabral, José Matto
""",
    'semana 4 (19-22/12)': """
Marimar López,
Melquiades Alonso, Nathalia Serafini, Marco Mendoza, Bruno perrota, Fernando Santos, Nahiara Trinidad, Fanny Ayala,
Luis Elizeche, Eilyn Rubiños
""",
    'semana 5 (26-31/12)': """
(vacío)
"""
}

def contar_semana(datos):
    """Contar consultas en un string (cada nombre = 1 consulta)"""
    items = [x.strip() for x in datos.split(',')]
    items = [x for x in items if x and x != '-' and x.lower() != '(vacío)']
    return len(items)

print("="*70)
print("OCTUBRE 2022 - CONTEO POR SEMANA")
print("="*70)
total_oct = 0
for semana, datos in oct_semanas.items():
    count = contar_semana(datos)
    total_oct += count
    print(f"{semana}: {count}")
print(f"\nTOTAL OCTUBRE: {total_oct} (tú dijiste: 73)")

print("\n" + "="*70)
print("NOVIEMBRE 2022 - CONTEO POR SEMANA")
print("="*70)
total_nov = 0
for semana, datos in nov_semanas.items():
    count = contar_semana(datos)
    total_nov += count
    print(f"{semana}: {count}")
print(f"\nTOTAL NOVIEMBRE: {total_nov} (tú dijiste: 70)")

print("\n" + "="*70)
print("DICIEMBRE 2022 - CONTEO POR SEMANA")
print("="*70)
total_dic = 0
for semana, datos in dic_semanas.items():
    count = contar_semana(datos)
    total_dic += count
    print(f"{semana}: {count}")
print(f"\nTOTAL DICIEMBRE: {total_dic} (tú dijiste: 59)")
