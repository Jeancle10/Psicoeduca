---
name: cancelaciones-desde-2023
description: Registro de cancelaciones en agendamientos.xlsx desde 2023 con estadísticas
metadata:
  type: project
---

# 📊 Cancelaciones Desde 2023

## Resumen Ejecutivo

**91 cancelaciones detectadas** (2.6% del total de 3,439 consultas 2022-2026)

| Año | Cancelaciones | % |
|---|---|---|
| 2023 | 11 | 1.0% |
| 2024 | 14 | 1.6% |
| 2025 | 50 | 5.4% |
| 2026 | 16 | 3.8% |

## Integración Completada

✅ **Campo "Estado" creado en Airtable** 
- ID: fld2TGfK5DeNJ9XR8
- Opciones: Realizado, Cancelado

✅ **Knowledge base de Skinner actualizada**
- Archivo: estadisticas-cancelaciones.md
- Ruta: proyectos/psicoeduca-agente/knowledge/

✅ **6 Herramientas documentadas**
- Archivo: tools/consultas_airtable.py
- Ruta: proyectos/psicoeduca-agente/tools/

## Herramientas Disponibles

1. **buscar_consultas_por_nombre(nombre)** → Busca historial completo de un consultante
2. **contar_consultas_por_año(nombre, año?)** → Cuenta consultas por año
3. **última_consulta(nombre)** → Fecha de última consulta
4. **próxima_consulta(nombre)** → Próxima cita agendada
5. **consultas_en_mes(año, mes)** → Estadísticas mensuales
6. **consultantes_más_activos(año?, top?)** → Ranking de consultantes

## Próximos Pasos

⏳ Integrar herramientas en brain.py de Skinner
⏳ Actualizar config/prompts.yaml
⏳ Implementar tool_use handlers
