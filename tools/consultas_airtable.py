"""
Herramientas de consultas para Skinner - Implementación con Airtable
Cada herramienta busca en la tabla "Consultas Histórico" en Airtable
"""

# Estos son los parámetros necesarios para las llamadas a Airtable
AIRTABLE_CONFIG = {
    "BASE_ID": "appfPbIIS3UgNvOKC",
    "TABLE_CONSULTAS": "tblfohS1ZEkvFkGFw",  # Consultas Histórico
    "TABLE_TURNOS": "tblaeQco2NuB9vkMa",     # Turnos (para próxima cita)

    "FIELDS": {
        "nombre": "fldsi3PWDbVMrC3Qm",
        "fecha": "fldW3yUMNQ8cdtwGW",
        "año": "fldqq7Nb8ry0IEU9R",
        "mes": "fldyzq91v6Jwu4y7D",
        "modalidad": "fldVaG6ldSL2CX61V"
    }
}

def buscar_consultas_por_nombre(nombre: str) -> dict:
    """
    Busca todas las consultas de un consultante por nombre.

    Implementación:
    - Llama a list_records_for_table con filtro CONTAINS en campo "Nombre"
    - Ordena por fecha DESC
    - Retorna lista con fecha, año, mes, modalidad

    Filtro Airtable:
    {
        "operands": [{
            "operator": "contains",
            "operands": ["fldsi3PWDbVMrC3Qm", nombre]
        }]
    }
    """
    # Esta función será implementada en Skinner usando tool_use
    # Aquí documentamos la lógica
    return {
        "herramienta": "list_records_for_table",
        "parámetros": {
            "baseId": AIRTABLE_CONFIG["BASE_ID"],
            "tableId": AIRTABLE_CONFIG["TABLE_CONSULTAS"],
            "filters": {
                "operands": [{
                    "operator": "contains",
                    "operands": [AIRTABLE_CONFIG["FIELDS"]["nombre"], nombre]
                }]
            },
            "sort": [{"fieldId": AIRTABLE_CONFIG["FIELDS"]["fecha"], "direction": "desc"}]
        },
        "procesamiento": "Contar total, agrupar por año/mes, retornar lista"
    }

def contar_consultas_por_año(nombre: str, año: int = None) -> dict:
    """
    Cuenta consultas por año.

    Si año se especifica:
    - Filtro AND: nombre CONTAINS + año EQUALS

    Si año es None:
    - Filtro solo nombre CONTAINS
    - Procesar en memoria para agrupar por año
    """
    if año:
        filtro = {
            "operator": "and",
            "operands": [
                {
                    "operator": "contains",
                    "operands": [AIRTABLE_CONFIG["FIELDS"]["nombre"], nombre]
                },
                {
                    "operator": "=",
                    "operands": [AIRTABLE_CONFIG["FIELDS"]["año"], año]
                }
            ]
        }
    else:
        filtro = {
            "operands": [{
                "operator": "contains",
                "operands": [AIRTABLE_CONFIG["FIELDS"]["nombre"], nombre]
            }]
        }

    return {
        "herramienta": "list_records_for_table",
        "parámetros": {
            "baseId": AIRTABLE_CONFIG["BASE_ID"],
            "tableId": AIRTABLE_CONFIG["TABLE_CONSULTAS"],
            "filters": filtro
        },
        "procesamiento": "Contar registros. Si año=None, agrupar por año en memoria"
    }

def última_consulta(nombre: str) -> dict:
    """
    Retorna la última consulta de un consultante.

    - Filtro: nombre CONTAINS
    - Ordenar: fecha DESC
    - Tomar: primer registro
    """
    return {
        "herramienta": "list_records_for_table",
        "parámetros": {
            "baseId": AIRTABLE_CONFIG["BASE_ID"],
            "tableId": AIRTABLE_CONFIG["TABLE_CONSULTAS"],
            "filters": {
                "operands": [{
                    "operator": "contains",
                    "operands": [AIRTABLE_CONFIG["FIELDS"]["nombre"], nombre]
                }]
            },
            "sort": [{"fieldId": AIRTABLE_CONFIG["FIELDS"]["fecha"], "direction": "desc"}],
            "pageSize": 1
        },
        "procesamiento": "Tomar primer registro y formatear con fecha en formato legible"
    }

def próxima_consulta(nombre: str) -> dict:
    """
    Busca próxima consulta en tabla Turnos (no en histórico).

    - Tabla: Turnos
    - Filtro: Nombre Paciente CONTAINS + Fecha > hoy
    - Ordenar: Fecha ASC
    - Tomar: primer registro
    """
    return {
        "herramienta": "list_records_for_table",
        "parámetros": {
            "baseId": AIRTABLE_CONFIG["BASE_ID"],
            "tableId": AIRTABLE_CONFIG["TABLE_TURNOS"],
            "filters": {
                "operator": "and",
                "operands": [
                    {
                        "operator": "contains",
                        "operands": ["fldjiuursXi1VgSR5", nombre]  # Nombre paciente en Turnos
                    },
                    {
                        "operator": ">",
                        "operands": ["fldtk1LVlNUn1L3ph", {"mode": "today", "timeZone": "America/Asuncion"}]  # Fecha > hoy
                    }
                ]
            },
            "sort": [{"fieldId": "fldtk1LVlNUn1L3ph", "direction": "asc"}],  # Fecha ASC
            "pageSize": 1
        },
        "procesamiento": "Tomar primer registro, formatear con fecha/hora, calcular 'en X días'"
    }

def consultas_en_mes(año: int, mes: str) -> dict:
    """
    Estadísticas de un mes.

    - Filtro AND: año EQUALS + mes EQUALS
    - Procesar en memoria: contar total, contar únicos, contar por modalidad
    """
    meses_map = {
        "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5,
        "Junio": 6, "Julio": 7, "Agosto": 8, "Septiembre": 9,
        "Octubre": 10, "Noviembre": 11, "Diciembre": 12
    }

    return {
        "herramienta": "list_records_for_table",
        "parámetros": {
            "baseId": AIRTABLE_CONFIG["BASE_ID"],
            "tableId": AIRTABLE_CONFIG["TABLE_CONSULTAS"],
            "filters": {
                "operator": "and",
                "operands": [
                    {
                        "operator": "=",
                        "operands": [AIRTABLE_CONFIG["FIELDS"]["año"], año]
                    },
                    {
                        "operator": "=",
                        "operands": [AIRTABLE_CONFIG["FIELDS"]["mes"], mes]
                    }
                ]
            }
        },
        "procesamiento": "Contar total, contar distintos por nombre, contar por modalidad"
    }

def consultantes_más_activos(año: int = None, top: int = 10) -> dict:
    """
    Ranking de consultantes.

    - Si año: filtrar por año
    - Procesar en memoria: agrupar por nombre, contar, ordenar DESC, tomar top N
    """
    filtro = None
    if año:
        filtro = {
            "operands": [{
                "operator": "=",
                "operands": [AIRTABLE_CONFIG["FIELDS"]["año"], año]
            }]
        }

    return {
        "herramienta": "list_records_for_table",
        "parámetros": {
            "baseId": AIRTABLE_CONFIG["BASE_ID"],
            "tableId": AIRTABLE_CONFIG["TABLE_CONSULTAS"],
            "filters": filtro,
            "pageSize": 1000  # Traer muchos para procesar
        },
        "procesamiento": f"Agrupar por nombre, contar, ordenar DESC, retornar top {top}"
    }


# INSTRUCCIONES DE INTEGRACIÓN EN SKINNER
"""
En brain.py o prompt de Skinner, agregar estos tools:

tools = [
    {
        "type": "function",
        "function": {
            "name": "buscar_consultas_por_nombre",
            "description": "Busca todas las consultas históricas de un consultante",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre": {"type": "string", "description": "Nombre del consultante"}
                },
                "required": ["nombre"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "contar_consultas_por_año",
            "description": "Cuenta consultas por año",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre": {"type": "string"},
                    "año": {"type": "integer", "description": "Opcional"}
                },
                "required": ["nombre"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "última_consulta",
            "description": "Última consulta registrada de un consultante",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre": {"type": "string"}
                },
                "required": ["nombre"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "próxima_consulta",
            "description": "Próxima consulta agendada",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre": {"type": "string"}
                },
                "required": ["nombre"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "consultas_en_mes",
            "description": "Estadísticas de un mes",
            "parameters": {
                "type": "object",
                "properties": {
                    "año": {"type": "integer"},
                    "mes": {"type": "string"}
                },
                "required": ["año", "mes"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "consultantes_más_activos",
            "description": "Top N consultantes más activos",
            "parameters": {
                "type": "object",
                "properties": {
                    "año": {"type": "integer", "description": "Opcional"},
                    "top": {"type": "integer", "description": "Default: 10"}
                },
                "required": []
            }
        }
    }
]
"""
