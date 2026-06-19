# Integración de Herramientas de Consultas en Skinner

## Resumen
Skinner ahora puede responder preguntas sobre el histórico de consultas de los 3,439 registros cargados en Airtable.

## Paso 1: Copiar el archivo de herramientas

Copiar `C:\Users\MI PC\psicoeduca\tools\consultas_airtable.py` a tu repo de psicoeduca-agente:
```bash
tools/consultas_airtable.py
```

Este archivo contiene:
- Configuración de IDs de Airtable
- 6 herramientas documentadas
- Instrucciones de integración

## Paso 2: Agregar tools al brain.py o prompt

En tu archivo que defina las tools (puede ser `brain.py`, `config/tools.yaml`, o donde tengas las definiciones):

```python
from tools.consultas_airtable import (
    buscar_consultas_por_nombre,
    contar_consultas_por_año,
    última_consulta,
    próxima_consulta,
    consultas_en_mes,
    consultantes_más_activos
)

CONSULTAS_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "buscar_consultas_por_nombre",
            "description": "Busca todas las consultas históricas de un consultante por su nombre. Retorna lista con fechas, años, meses y modalidades de cada consulta.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre": {
                        "type": "string",
                        "description": "Nombre o parte del nombre del consultante (búsqueda insensible a mayúsculas)"
                    }
                },
                "required": ["nombre"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "contar_consultas_por_año",
            "description": "Cuenta la cantidad de consultas de un consultante por año. Si no se especifica año, retorna totales por cada año.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre": {
                        "type": "string",
                        "description": "Nombre del consultante"
                    },
                    "año": {
                        "type": "integer",
                        "description": "Año específico (2022-2026). Opcional."
                    }
                },
                "required": ["nombre"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "última_consulta",
            "description": "Retorna la fecha y detalles de la última consulta registrada de un consultante",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre": {
                        "type": "string",
                        "description": "Nombre del consultante"
                    }
                },
                "required": ["nombre"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "próxima_consulta",
            "description": "Busca la próxima consulta agendada de un consultante en el calendario de turnos",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre": {
                        "type": "string",
                        "description": "Nombre del consultante"
                    }
                },
                "required": ["nombre"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "consultas_en_mes",
            "description": "Retorna estadísticas de un mes específico: total de consultas, consultantes distintos, virtual vs presencial",
            "parameters": {
                "type": "object",
                "properties": {
                    "año": {
                        "type": "integer",
                        "description": "Año (2022-2026)"
                    },
                    "mes": {
                        "type": "string",
                        "description": "Nombre del mes (Enero, Febrero, Marzo, etc.)"
                    }
                },
                "required": ["año", "mes"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "consultantes_más_activos",
            "description": "Retorna ranking de consultantes con más consultas. Puede filtrar por año específico.",
            "parameters": {
                "type": "object",
                "properties": {
                    "año": {
                        "type": "integer",
                        "description": "Año específico (2022-2026). Opcional."
                    },
                    "top": {
                        "type": "integer",
                        "description": "Cantidad de consultantes a retornar (default: 10)"
                    }
                },
                "required": []
            }
        }
    }
]
```

## Paso 3: Agregar al prompt

En tu `config/prompts.yaml` o donde tengas el sistema prompt:

```yaml
herramientas_disponibles: |
  Tienes acceso a herramientas para consultar el histórico de consultas:
  
  - buscar_consultas_por_nombre(nombre): Busca todas las consultas de un consultante
  - contar_consultas_por_año(nombre, año?): Cuenta consultas por año
  - última_consulta(nombre): Última consulta registrada
  - próxima_consulta(nombre): Próxima consulta agendada
  - consultas_en_mes(año, mes): Estadísticas mensuales
  - consultantes_más_activos(año?, top?): Top consultantes

instrucciones_consultas: |
  Cuando alguien pregunte sobre:
  - "¿Cuántas consultas tuvo X?" → usa buscar_consultas_por_nombre o contar_consultas_por_año
  - "¿Cuándo fue la última consulta de X?" → usa última_consulta
  - "¿Cuándo viene X?" → usa próxima_consulta
  - "Estadísticas del mes" → usa consultas_en_mes
  - "Consultantes más activos" → usa consultantes_más_activos
  
  Responde siempre en formato amigable, e.g.:
  "Mayra ha tenido 12 consultas en total: 
   - 2022: 3 (todas presenciales)
   - 2023: 5 (3 virtual, 2 presencial)
   - 2024: 4 (2 virtual, 2 presencial)"
```

## Paso 4: Implementar las herramientas en tool_use

En tu función que maneja tool_use (donde procesan las llamadas a herramientas):

```python
def handle_tool_call(tool_name, tool_input):
    if tool_name == "buscar_consultas_por_nombre":
        # Llamar a Airtable list_records_for_table con el filtro
        # Retornar: {"nombre": X, "total": N, "consultas": [...]}
        pass
    
    elif tool_name == "contar_consultas_por_año":
        # Similar, con filtro por año si se especifica
        pass
    
    # ... etc para las otras 4 herramientas
```

## Datos disponibles en Airtable

### Tabla: Consultas Histórico
- **Base ID**: `appfPbIIS3UgNvOKC`
- **Table ID**: `tblfohS1ZEkvFkGFw`
- **Total registros**: 3,439
- **Campos**:
  - `Nombre` (fldsi3PWDbVMrC3Qm): singleLineText
  - `Fecha` (fldW3yUMNQ8cdtwGW): date (YYYY-MM-DD)
  - `Año` (fldqq7Nb8ry0IEU9R): number
  - `Mes` (fldyzq91v6Jwu4y7D): singleLineText
  - `Modalidad` (fldVaG6ldSL2CX61V): singleSelect (Virtual/Presencial)

### Tabla: Turnos (para próximas citas)
- **Base ID**: `appfPbIIS3UgNvOKC`
- **Table ID**: `tblaeQco2NuB9vkMa`
- **Campos relevantes**:
  - `Nombre paciente` (fldjiuursXi1VgSR5): singleLineText
  - `Fecha` (fldtk1LVlNUn1L3ph): date
  - `Hora inicio` (fld505u0ZTLeaiiOJ): singleLineText
  - `Modalidad` (fldZ05QAaaMPLKuYz): singleSelect

## Ejemplos de preguntas que Skinner puede responder

**Con búsqueda simple:**
- "¿Cuántas consultas tuvo Mayra?" → buscar_consultas_por_nombre("Mayra")
- "Historial de Adri Zacarias" → buscar_consultas_por_nombre("Adri")

**Con filtro de año:**
- "¿Cuántas consultas de Juan en 2022?" → contar_consultas_por_año("Juan", 2022)
- "Total de consultas de María" → contar_consultas_por_año("María")

**Últimas y próximas:**
- "¿Cuándo fue la última consulta de Mayra?" → última_consulta("Mayra")
- "¿Cuándo viene Adri?" → próxima_consulta("Adri")

**Estadísticas:**
- "¿Cuántas consultas hubo en junio 2026?" → consultas_en_mes(2026, "Junio")
- "Consultantes más activos del 2025" → consultantes_más_activos(2025, 10)

## Testing

Prueba estas preguntas en Skinner después de integrar:

```
Usuario: "¿Cuántas consultas tuvo Daniel Rojas?"
Skinner: [Usa buscar_consultas_por_nombre] 
         "Daniel Rojas ha tenido X consultas en total..."

Usuario: "Cuándo fue la última consulta de Marimar Lopez?"
Skinner: [Usa última_consulta]
         "La última consulta de Marimar Lopez fue el..."

Usuario: "Quiénes fueron los 5 más activos en 2024?"
Skinner: [Usa consultantes_más_activos]
         "Los 5 consultantes más activos en 2024 fueron..."
```

## Troubleshooting

**Error: "Record not found"**
- La búsqueda es case-insensitive pero debe coincidir en contenido
- Probar con partes del nombre: "Juan" en lugar de "Juan García"

**Error: "Invalid field ID"**
- Verificar que los field IDs en `consultas_airtable.py` sean correctos
- Los IDs están en comentarios en la tabla de Airtable

**Respuestas lentas**
- La tabla tiene 3,439 registros
- Las búsquedas por nombre son rápidas (filtradas por Airtable)
- El agrupamiento se hace en memoria (aceptable hasta ~100 registros)

---

**¿Necesitas ayuda con la integración? Pregunta cualquier cosa.**
