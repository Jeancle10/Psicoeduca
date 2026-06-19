"""
Herramientas para consultar el histórico de consultas de Psicoeduca
Usadas por Skinner para responder preguntas sobre consultantes
"""

def buscar_consultas_por_nombre(nombre):
    """
    Busca todas las consultas de un consultante por nombre.
    Retorna: lista de diccionarios con fecha, año, mes, modalidad

    Ejemplo:
    >>> buscar_consultas_por_nombre("Mayra")
    [
        {"fecha": "2022-08-15", "año": 2022, "mes": "Agosto", "modalidad": "Presencial"},
        {"fecha": "2022-09-10", "año": 2022, "mes": "Septiembre", "modalidad": "Virtual"},
        ...
    ]
    """
    pass

def contar_consultas_por_año(nombre, año=None):
    """
    Cuenta las consultas de un consultante por año.
    Si año no se especifica, retorna total de todos los años.

    Ejemplo:
    >>> contar_consultas_por_año("Adri Zacarias", 2022)
    5
    >>> contar_consultas_por_año("Adri Zacarias")
    {"2022": 5, "2023": 8, "2024": 3, "2025": 4, "2026": 1}
    """
    pass

def última_consulta(nombre):
    """
    Retorna los datos de la última consulta de un consultante.

    Ejemplo:
    >>> última_consulta("Mayra")
    {"fecha": "2026-03-20", "año": 2026, "mes": "Marzo", "modalidad": "Virtual"}
    """
    pass

def próxima_consulta(nombre):
    """
    Busca la próxima consulta agendada de un consultante en la tabla Turnos.

    Ejemplo:
    >>> próxima_consulta("Mayra")
    {"fecha": "2026-06-25", "hora": "14:30", "modalidad": "Virtual"}
    """
    pass

def consultas_en_mes(año, mes):
    """
    Retorna estadísticas de un mes específico.

    Ejemplo:
    >>> consultas_en_mes(2026, "Junio")
    {
        "total_consultas": 40,
        "total_consultantes": 35,
        "consultantes": ["Mayra", "Adri", ...],
        "virtuales": 15,
        "presenciales": 25
    }
    """
    pass

def consultantes_más_activos(año=None, top=10):
    """
    Retorna los consultantes con más consultas.

    Ejemplo:
    >>> consultantes_más_activos(2026, top=5)
    [
        {"nombre": "Mayra", "consultas": 12},
        {"nombre": "Adri", "consultas": 10},
        ...
    ]
    """
    pass
