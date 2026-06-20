---
name: cancelaciones-desde-2023
description: Registro de cancelaciones en agendamientos.xlsx desde 2023
metadata:
  type: project
---

# 📋 Cancelaciones Desde 2023

## Estructura de datos en agendamientos.xlsx

**Hojas**: 2023, 2024, 2025, 2026

**Estructura por hoja**:
- Columna A: Horarios (horas de consulta)
- Fila 1 (encabezados): Fechas en formato DD/MM (ej: 02/08 = 2 agosto)
- Intersecciones: Nombres de consultantes
- **Cancelaciones**: Nombres con STRIKETHROUGH (tachados)

**Fecha completa**: Día/Mes (columna fecha) + Año (nombre de hoja)

**Ejemplo**: 
- Celda C151 en hoja 2023 contiene un nombre tachado
- Significa: cancelación de ese consultante en la fecha de la columna C, año 2023

## Identificación de cancelaciones

Para identificar una cancelación:
1. Ir a hoja 2023, 2024, 2025 o 2026
2. Buscar celdas con STRIKETHROUGH (nombre tachado)
3. Registrar: [Nombre] | [Fecha DD/MM] | [Año]

## Impacto en Airtable

- Campo **"Estado"** con valores: "Realizado" / "Cancelado"
- Los nombres tachados = Estado: "Cancelado"
- Los normales = Estado: "Realizado"

## Fuente original
- Archivo: agendamientos.xlsx
- Ubicación: C:\Users\MI PC\psicoeduca\agendamientos.xlsx
- Métodos de extracción: Excel COM (Windows) o exportar CSV manualmente
