"""
Implementación de herramientas de consultas usando Airtable
Para ser usadas por Skinner
"""

# Estos métodos se implementarán como tool_use en el prompt de Skinner
# Aquí documentamos la lógica que debe hacer cada una

class ConsultasAirtable:
    """
    Wrapper para consultar la tabla "Consultas Histórico" en Airtable
    """

    BASE_ID = "appfPbIIS3UgNvOKC"
    TABLE_ID = "tblfohS1ZEkvFkGFw"

    @staticmethod
    def buscar_consultas_por_nombre(nombre: str) -> dict:
        """
        Busca todas las consultas de un consultante.

        Lógica:
        1. Filtrar tabla Consultas Histórico donde Nombre CONTAINS nombre (case-insensitive)
        2. Contar total
        3. Retornar lista con fecha, año, mes, modalidad de cada una

        Llamada Airtable:
        list_records_for_table(
            baseId="appfPbIIS3UgNvOKC",
            tableId="tblfohS1ZEkvFkGFw",
            filters={
                "operands": [
                    {
                        "operator": "contains",
                        "operands": ["fldsi3PWDbVMrC3Qm", nombre]  # Nombre field
                    }
                ]
            },
            sort=[{"fieldId": "fldW3yUMNQ8cdtwGW", "direction": "desc"}]  # Fecha desc
        )
        """
        pass

    @staticmethod
    def contar_consultas_por_año(nombre: str, año: int = None) -> dict:
        """
        Cuenta consultas de un consultante por año.

        Lógica:
        1. Si año se especifica: filtrar por año + nombre
        2. Si no: contar por cada año
        3. Retornar diccionario con totales

        Llamadas Airtable:
        - Si año específico: filtrar con AND de nombre + año
        - Si todos: traer todos y contar en memoria por año
        """
        pass

    @staticmethod
    def última_consulta(nombre: str) -> dict:
        """
        Retorna la última consulta de un consultante.

        Lógica:
        1. Filtrar por nombre
        2. Ordenar por fecha DESC
        3. Tomar el primero
        4. Calcular "hace X días/meses"
        """
        pass

    @staticmethod
    def próxima_consulta(nombre: str) -> dict:
        """
        Busca próxima consulta en tabla Turnos.

        Lógica:
        1. Buscar en tabla Turnos (no en Consultas Histórico)
        2. Filtrar por nombre + fecha > hoy
        3. Ordenar por fecha ASC
        4. Tomar la primera
        """
        pass

    @staticmethod
    def consultas_en_mes(año: int, mes: str) -> dict:
        """
        Estadísticas de un mes.

        Lógica:
        1. Filtrar por año + mes
        2. Contar total de consultas
        3. Contar consultantes distintos
        4. Contar virtuales vs presenciales
        5. Listar consultantes únicos

        Llamada:
        list_records_for_table(
            baseId="appfPbIIS3UgNvOKC",
            tableId="tblfohS1ZEkvFkGFw",
            filters={
                "operator": "and",
                "operands": [
                    {"operator": "=", "operands": ["fldqq7Nb8ry0IEU9R", año]},      # Año
                    {"operator": "=", "operands": ["fldyzq91v6Jwu4y7D", mes_nombre]} # Mes
                ]
            }
        )
        """
        pass

    @staticmethod
    def consultantes_más_activos(año: int = None, top: int = 10) -> dict:
        """
        Ranking de consultantes.

        Lógica:
        1. Si año: filtrar por año
        2. Contar por nombre
        3. Ordenar por count DESC
        4. Tomar top N

        Nota: Esto requiere procesar en memoria (Airtable no tiene GROUP BY)
        """
        pass


# NOTA: Estas funciones serán integradas como tools en el prompt de Skinner
# Formato de tool_use para LLM:
"""
{
    "type": "function",
    "function": {
        "name": "buscar_consultas_por_nombre",
        "description": "Busca el histórico de consultas de un consultante por nombre",
        "parameters": {
            "type": "object",
            "properties": {
                "nombre": {
                    "type": "string",
                    "description": "Nombre o parte del nombre del consultante"
                }
            },
            "required": ["nombre"]
        }
    }
}
"""
