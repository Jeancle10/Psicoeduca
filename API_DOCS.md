# PsicoEduca API - Documentación de Endpoints

## Base URL
```
https://psicoeduca-xxx.railway.app
```

---

## 1. CONSULTANTES

### Listar consultantes
```
GET /api/consultantes/
```
**Parámetros opcionales:**
- `nombre` - Busca por nombre o apellido
- `edad_min` - Edad mínima
- `edad_max` - Edad máxima

**Respuesta:**
```json
[
  {
    "id": 1,
    "nombre": "Juan",
    "apellido": "García",
    "fecha_nacimiento": "1990-05-15",
    "edad": 33,
    "celular": "595999999",
    "email": "juan@email.com",
    "fecha_creacion": "2026-06-16T15:50:00",
    "total_evaluaciones": 2
  }
]
```

### Obtener consultante específico
```
GET /api/consultantes/{id}
```

**Respuesta:** (Incluye historial de evaluaciones)
```json
{
  "id": 1,
  "nombre": "Juan",
  "apellido": "García",
  "edad": 33,
  "celular": "595999999",
  "email": "juan@email.com",
  "evaluaciones": [
    {
      "id": 5,
      "fecha": "2026-06-16T15:50:00",
      "stai_estado": { ... },
      "stai_rasgo": { ... },
      "bdi": { ... },
      "bfi": { ... },
      "scl90": { ... }
    }
  ]
}
```

### Crear consultante
```
POST /api/consultantes/
Content-Type: application/json
```

**Body:**
```json
{
  "nombre": "Juan",
  "apellido": "García",
  "fecha_nacimiento": "1990-05-15",
  "celular": "595999999",
  "email": "juan@email.com"
}
```

### Actualizar consultante
```
PUT /api/consultantes/{id}
Content-Type: application/json
```

### Eliminar consultante
```
DELETE /api/consultantes/{id}
```

---

## 2. EVALUACIONES (IMPORTANTE)

### Crear evaluación (Procesa automáticamente tests)
```
POST /api/evaluaciones/
Content-Type: application/json
```

**Body completo:**
```json
{
  "consultante_id": 1,
  "respuestas": {
    "p1": "Juan García",
    "p2": "1990-05-15",
    "p3": "595999999",
    "p4": 2,
    "p5": 1,
    "p6": 0,
    ...
    "p135": 2
  }
}
```

**Preguntas:**
- P1-P3: Datos demográficos (nombre, fecha nacimiento, celular)
- P4-P23: STAI Estado (20 items, escala 0-3)
- P24-P43: STAI Rasgo (20 items, escala 0-3)
- P44-P66: BDI (23 items, escala 0-3)
- P67-P71: BFI-5 (5 items, escala 1-5)
- P72-P135: SCL-90-R (64 items, escala 0-4)

**Respuesta:**
```json
{
  "id": 5,
  "consultante_id": 1,
  "fecha": "2026-06-16T15:52:00",
  "stai_estado": {
    "puntuacion": 45,
    "percentil": 64,
    "categoria": "MODERADO"
  },
  "stai_rasgo": {
    "puntuacion": 48,
    "percentil": 71,
    "categoria": "MODERADO"
  },
  "bdi": {
    "puntuacion": 18,
    "categoria": "MODERADO"
  },
  "bfi": {
    "neuroticismo": 4,
    "extraversion": 3,
    "apertura": 5,
    "amabilidad": 4,
    "responsabilidad": 3
  },
  "scl90": {
    "puntuacion": 28,
    "categoria": "MODERADO"
  }
}
```

### Obtener evaluaciones de un consultante
```
GET /api/evaluaciones/{consultante_id}
```

### Obtener evaluación específica
```
GET /api/evaluaciones/{id}
```

### Eliminar evaluación
```
DELETE /api/evaluaciones/{id}
```

---

## 3. RESULTADOS (Reportes y Análisis)

### Comparativa temporal de un consultante
```
GET /api/resultados/comparativa/{consultante_id}
```

**Respuesta:**
```json
{
  "consultante": { ... },
  "evaluaciones": [
    {
      "fecha": "2026-05-10T10:00:00",
      "stai_estado": 40,
      "stai_rasgo": 45,
      "bdi": 15,
      "scl90": 22
    },
    {
      "fecha": "2026-06-16T15:52:00",
      "stai_estado": 45,
      "stai_rasgo": 48,
      "bdi": 18,
      "scl90": 28
    }
  ]
}
```

### Estadísticas generales
```
GET /api/resultados/estadisticas
```

**Respuesta:**
```json
{
  "total_evaluaciones": 15,
  "consultantes_evaluados": 8,
  "fecha_primer_registro": "2026-05-01T09:00:00",
  "fecha_ultimo_registro": "2026-06-16T15:52:00",
  "promedios": {
    "stai_estado": 42.5,
    "bdi": 16.3,
    "scl90": 25.2
  },
  "distribucion_categorias": {
    "stai_estado": {
      "SEVERO": 2,
      "MODERADO": 8,
      "LEVE": 5
    },
    "bdi": {
      "SEVERO": 1,
      "MODERADO": 6,
      "LEVE": 7,
      "Ausente o Mínimo": 1
    },
    "scl90": {
      "SEVERO": 1,
      "MODERADO": 5,
      "LEVE": 6,
      "Normal": 3
    }
  }
}
```

### Evaluaciones últimos N días
```
GET /api/resultados/ultimas/{dias}
```

Ej: `/api/resultados/ultimas/7` retorna evaluaciones de los últimos 7 días

---

## Categorías y Rangos

### STAI (Anxiety)
- **SEVERO:** Percentil > 75
- **MODERADO:** Percentil 25-75
- **LEVE:** Percentil < 25

### BDI (Depression)
- **SEVERO:** Puntuación 30+
- **MODERADO:** Puntuación 17-29
- **LEVE:** Puntuación 10-16
- **Ausente o Mínimo:** Puntuación 0-9

### BFI-5 (Big Five)
Cada dimensión va de 1 a 5 (sin categorización, solo score)

### SCL-90-R (Symptoms)
- **SEVERO:** Puntuación 21+
- **MODERADO:** Puntuación 11-20
- **LEVE:** Puntuación 4-10
- **Normal:** Puntuación 0-3

---

## Ejemplos de Uso (curl)

### Crear consultante
```bash
curl -X POST http://localhost:5000/api/consultantes/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan",
    "apellido": "García",
    "fecha_nacimiento": "1990-05-15",
    "celular": "595999999"
  }'
```

### Cargar evaluación
```bash
curl -X POST http://localhost:5000/api/evaluaciones/ \
  -H "Content-Type: application/json" \
  -d '{
    "consultante_id": 1,
    "respuestas": {
      "p1": "Juan García",
      "p2": "1990-05-15",
      "p3": "595999999",
      "p4": 2,
      "p5": 1,
      ...
    }
  }'
```

---

## Estado del Desarrollo

✅ Backend completo
- Modelos de BD
- Lógica de cálculos (STAI, BDI, BFI-5, SCL-90-R)
- API endpoints
- Reportes y estadísticas

⏳ Próximas fases
- Frontend (formulario web)
- Google Drive integration
- PDF export
- Gráficos
