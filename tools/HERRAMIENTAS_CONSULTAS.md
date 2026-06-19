# Herramientas de Consultas para Skinner

Estas herramientas permiten que Skinner responda preguntas sobre el histórico de consultas de los consultantes.

## Base de Datos
- **Base ID**: `appfPbIIS3UgNvOKC`
- **Tabla**: `Consultas Histórico` (ID: `tblfohS1ZEkvFkGFw`)
- **Total registros**: 3,439 consultas (2022-2026)

## Herramientas Disponibles

### 1. `buscar_consultas_por_nombre(nombre: str)`
**Busca todas las consultas de un consultante.**

Parámetros:
- `nombre` (str): Nombre del consultante (búsqueda parcial)

Retorna:
```json
{
  "nombre": "Mayra",
  "total_consultas": 12,
  "consultas": [
    {"fecha": "2022-08-15", "año": 2022, "mes": "Agosto", "modalidad": "Presencial"},
    {"fecha": "2022-09-10", "año": 2022, "mes": "Septiembre", "modalidad": "Virtual"}
  ]
}
```

Ejemplo:
- "Cuántas consultas tuvo Mayra?"
- "Mostrame el historial de Adri Zacarias"

---

### 2. `contar_consultas_por_año(nombre: str, año: int = None)`
**Cuenta consultas por año.**

Parámetros:
- `nombre` (str): Nombre del consultante
- `año` (int, opcional): Año específico. Si no se da, retorna todos los años.

Retorna:
```json
{
  "nombre": "Adri Zacarias",
  "consultas_por_año": {
    "2022": 5,
    "2023": 8,
    "2024": 3,
    "2025": 4,
    "2026": 1
  },
  "total": 21
}
```

O si se especifica año:
```json
{
  "nombre": "Adri Zacarias",
  "año": 2022,
  "consultas": 5
}
```

Ejemplo:
- "Cuántas consultas tuvo Mayra en 2022?"
- "Cuántas consultas totales tiene Adri?"

---

### 3. `última_consulta(nombre: str)`
**Retorna la última consulta registrada.**

Parámetros:
- `nombre` (str): Nombre del consultante

Retorna:
```json
{
  "nombre": "Mayra",
  "última_consulta": {
    "fecha": "2026-03-20",
    "año": 2026,
    "mes": "Marzo",
    "modalidad": "Virtual"
  },
  "hace": "3 meses atrás"
}
```

Ejemplo:
- "Cuándo fue la última consulta de Mayra?"
- "Última vez que vino Adri Zacarias?"

---

### 4. `próxima_consulta(nombre: str)`
**Retorna la próxima consulta agendada (de tabla Turnos).**

Parámetros:
- `nombre` (str): Nombre del consultante

Retorna:
```json
{
  "nombre": "Mayra",
  "próxima_consulta": {
    "fecha": "2026-06-25",
    "hora": "14:30",
    "día": "Jueves",
    "modalidad": "Virtual"
  },
  "en": "6 días"
}
```

Ejemplo:
- "Cuándo viene Mayra?"
- "Próxima cita de Adri?"

---

### 5. `consultas_en_mes(año: int, mes: str)`
**Estadísticas de un mes.**

Parámetros:
- `año` (int): Año (2022-2026)
- `mes` (str): Nombre del mes ("Enero", "Febrero", etc.)

Retorna:
```json
{
  "período": "Junio 2026",
  "total_consultas": 40,
  "consultantes_distintos": 35,
  "virtuales": 15,
  "presenciales": 25,
  "consultantes": ["Mayra", "Adri", "Juan", ...]
}
```

Ejemplo:
- "Cuántas consultas hubo en junio 2026?"
- "Estadísticas del mes de marzo?"

---

### 6. `consultantes_más_activos(año: int = None, top: int = 10)`
**Ranking de consultantes con más consultas.**

Parámetros:
- `año` (int, opcional): Año específico. Si no se da, retorna de todos los años.
- `top` (int): Top N consultantes (default: 10)

Retorna:
```json
{
  "período": "2026",
  "top_consultantes": [
    {"nombre": "Mayra", "consultas": 12},
    {"nombre": "Adri Zacarias", "consultas": 10},
    {"nombre": "Juan González", "consultas": 8}
  ]
}
```

Ejemplo:
- "Quiénes fueron los consultantes más activos en 2026?"
- "Top 5 consultantes de este año?"

---

## Integración en Skinner

### Prompt Update
Agregar a `config/prompts.yaml`:

```yaml
herramientas_consultas:
  descripción: "Puedes responder preguntas sobre el historial de consultas de los consultantes usando estas herramientas"
  disponibles:
    - buscar_consultas_por_nombre
    - contar_consultas_por_año
    - última_consulta
    - próxima_consulta
    - consultas_en_mes
    - consultantes_más_activos

respuestas_esperadas:
  - "¿Cuántas consultas tuvo Mayra?" → buscar_consultas_por_nombre("Mayra")
  - "¿Cuántas consultas de Adri en 2022?" → contar_consultas_por_año("Adri", 2022)
  - "¿Cuándo fue la última consulta de Mayra?" → última_consulta("Mayra")
  - "¿Cuándo viene Adri?" → próxima_consulta("Adri")
```

### Tools Definition en brain.py
```python
{
    "type": "function",
    "function": {
        "name": "buscar_consultas_por_nombre",
        "description": "Busca todas las consultas de un consultante",
        "parameters": {
            "type": "object",
            "properties": {
                "nombre": {
                    "type": "string",
                    "description": "Nombre del consultante (búsqueda parcial)"
                }
            },
            "required": ["nombre"]
        }
    }
}
```

---

## Base de Datos Airtable

### Tabla: Consultas Histórico
| Campo | Tipo | Descripción |
|-------|------|-------------|
| Nombre | Texto | Nombre del consultante |
| Fecha | Fecha (YYYY-MM-DD) | Fecha exacta de la consulta |
| Año | Número | Año de la consulta |
| Mes | Texto | Nombre del mes |
| Modalidad | Select (Virtual/Presencial) | Tipo de consulta |

### Tabla: Turnos (existente)
Usada para obtener próximas consultas agendadas.

---

## Notas
- Las búsquedas por nombre usan búsqueda parcial/insensible a mayúsculas
- El histórico incluye 3,439 consultas de 2022-2026
- Los datos vienen del Excel "Agendamientos" procesado
- Las próximas consultas se sacan de la tabla "Turnos" que es futura
