# 📊 Progreso — psicoeduca
## Ultima sesion: 19/06/2026 (noche, 22:49)
## Estado actual: Skinner v4 con sistema de pagos completo. 151 contactos cargados. Dashboard 2022-2023-2024-2025 COMPLETO en Airtable (⚠️ 2022 tiene datos incorrectos, 2023-2024-2025 CORRECTOS, todos 12 meses). Total histórico: 1,956 consultantes, 2,854 consultas

## ✅ Completado
- Skinner desplegado en producción: `https://psicoeduca-agente-production.up.railway.app`
- `config/prompts.yaml` y `config/business.yaml` creados (personalidad, datos del negocio, menú de bienvenida)
- Repo GitHub `Jeancle10/psicoeduca-agente` creado y código pusheado
- `cowork-agentkit-nuevo` eliminado (lo útil se migró a `psicoeduca-agente`)
- Fix: `docker-entrypoint.sh` reconstruye `config/*.yaml` (gitignored) desde variables Railway en cada arranque
- Conexión Meta WhatsApp Cloud API: número real +595982469351 (Phone Number ID `1096140520250334`), webhook verificado, suscripción `messages` activa, token permanente `META_ACCESS_TOKEN` generado y cargado en Railway
- Estructura de carpetas creada
- Sistema de memoria configurado
- Limpieza profunda de Windows + reparación del sistema
- Python 3.12.10 + Node.js + Claude Code CLI + numpy instalados
- Extensión Python + python-pptx instalados
- Máquina APTA para Nivel 1
- Presentación AF: 24 slides, caso Marge Simpson (estilo crema anterior)
- Presentación Bases Filosóficas: 17 slides, caso Homero Simpson, NUEVA identidad visual
  - Paleta Rebranding: #1E3A5F, #F2EDE4, #E8A835, #4ABFB0
  - Logos transparentes del Rebranding (claro/oscuro sin fondo)
  - Fondos alternados dark/crema
- Repo `cowork-agentkit` clonado → `C:\Users\MI PC\proyectos\psicoeduca-agente`
- Base de conocimiento del agente: `knowledge/psicoeduca-conocimiento.md` (FAQs, precios, horarios, protocolo de crisis)
- Arquitectura Airtable en el agente: tools/airtable.py, tools/generador_turnos.py, brain.py con tool_use
- Base Airtable creada en cuenta de Jean: `PsicoEduca — Agenda` (appfPbIIS3UgNvOKC)
- Tabla "Turnos": 13/13 campos completos
- 63 turnos generados para las próximas 2 semanas (11/06 al 01/07/2026), todos "Disponible"

## ✅ Completado (16/06/2026 — sesión mediodía)
- **Análisis Excel "Interpretacion de instrumentos.xlsx"** (113K+ fórmulas, 6 hojas, evaluación psicométrica STAI+BDI+BFI+SCL)
  - Generado: `ANALISIS_INTERPRETACION_INSTRUMENTOS.md` (análisis técnico completo)
- **Mapeo Formulario Google → Excel** (135 preguntas, 5 tests, 10 tablas nombradas)
  - Identificados: STAI-E (P1-P20), STAI-R (P21-P40), BDI (P41-P63), BFI-5 (P64-P68), SCL-90-R (P69-P132)
  - Extraídos: Umbrales de categorización exactos (Leve/Moderado/Severo) por test
  - Generado: `MAPEO_FORMULARIO_GOOGLE.md` (listo para Google Apps Script)

## ✅ Completado (16/06/2026 — sesión tarde: Backend + Frontend)
- **PsicoEduca App Web — FASE 2 + 3 COMPLETADAS**
  - Backend API: 13 endpoints (consultantes CRUD + evaluaciones + reportes)
  - Modelos: Consultante, Evaluacion (SQLAlchemy + PostgreSQL)
  - Lógica tests: STAI-E, STAI-R, BDI, BFI-5, SCL-90-R (con baremos y percentiles)
  - Frontend: HTML/CSS/JS (dashboard + formulario 135 preguntas + resultados con gráficos)
  - Infraestructura: Railway (project 2434ba24...), PostgreSQL (a8242aef...), Drive (carpeta "Consultantes IA")
  - Documentación: API_DOCS.md, ESTADO_PROYECTO.md, RESUMEN_SESION.md
  - Status: ✅ BACKEND LIVE + FRONTEND LIVE (3.5 horas de trabajo)
  - Commits: 5 (backend + frontend + fixes + docs)
  - URL pública: https://railway.com/project/2434ba24-659c-4207-9dc7-667fab44c137

## ✅ Completado (16/06/2026 — sesión mañana)
- **Proyecto Ñakurutu** creado en `C:\Users\MI PC\proyectos\Ñakurutu\`
- 5 tablas creadas en Airtable (base `appcetoe3cXohXKUb` "Ñakurutu Historico"):
  Alumnos, Períodos, Inscripciones, Pagos, Cohortes (con fórmulas de retención y recaudación)
- Carga año 2024: 178 alumnos, 206 inscripciones, 749 pagos, 0 errores — `carga_24_25.py`
- Carga año 22-23: 156 alumnos nuevos, 193 inscripciones, 636 pagos, 0 errores — `carga_22_23.py`
  - Intensivo Mañana 22-23: 61 insc, 239 pagos
  - Intensivo Noche 22-23: 70 insc, 238 pagos
  - Extensivo 2022: 62 insc, 159 pagos
  - Costo base: 400k Intensivo / 385k Extensivo (verificar si es correcto)

## ✅ Completado (19/06/2026 — sesión Skinner v4: Sistema de Pagos)
- **Sistema de Pagos + Tabla Contactos**:
  - Tabla "Contactos" creada en Airtable (Nombre, Apellido, Teléfono, Correo)
  - Campo "Estado de pago" agregado a tabla Turnos (Pendiente a confirmar | Confirmado)
  - 6 nuevas herramientas: registrar_pago, confirmar_pago, reporte_pagos_pendientes, reporte_pagos_confirmados, crear_contacto, obtener_contactos
  - Flujo: Milva pasa comprobante → registra como "Pendiente" → Jean confirma → marca "Confirmado"
  - Deploy a Railway ✅ (PROMPTS_YAML_B64 regenerado 12360 chars)

## ✅ Completado (19/06/2026 — sesión tarde: Carga de Contactos + Dashboard Análisis 2022)
- **Carga masiva de 151 contactos a Airtable**:
  - CSV "Agendamientos - Consultantes" procesado
  - 4 lotes de 50 registros cada uno cargados sin errores
  - Campos: Nombre, Apellido, Teléfono (todos con acentos correctos)
- **Análisis estructura Dashboard "Análisis Mensual 2022+"**:
  - Estructura de datos clarificada: calendario con fechas como encabezados
  - Sistema de conteo: sesiones grupales = 1 consulta, cada persona se suma a consultantes distintos
  - Modalidades: "vir" = virtual, sin etiqueta = presencial
  - Cancelaciones: tachados = métrica separada (50% del valor)

## ✅ Completado (19/06/2026 — sesión tarde, retomada: Procesamiento 2022 Completo)
- **Análisis Mensual 2022 en Airtable — TABLA CREADA (datos incorrectos ⚠️)**:
  - Tabla "Análisis Mensual 2022" creada con 6 campos: Mes, Año, Consultantes Distintos, Total Consultas, Canceladas, Tasa Cancelación %
  - ⚠️ Datos en Airtable son INCORRECTOS (extracción manual con duplicaciones)
  - Datos CORRECTOS (desde Excel): 
    - Agosto: 30 consultantes, 51 consultas
    - Septiembre: 33 consultantes, 50 consultas
    - Octubre: 39 consultantes, 73 consultas
    - Noviembre: 47 consultantes, 70 consultas
    - Diciembre: 37 consultantes, 57 consultas
  - **Total 2022 (ago-dic): 186 consultantes distintos, 281 consultas**

## ✅ Completado (19/06/2026 — sesión noche: Procesamiento 2025 Completo)
- **Análisis Mensual 2025 en Airtable — TABLA CREADA Y CARGADA CORRECTAMENTE**:
  - Script `procesar_2025.py` procesa 12 bloques mensuales de fechas automáticamente
  - Tabla "Análisis Mensual 2025" creada (ID: tbl0FQBvqGUuoKMCl)
  - 11 registros cargados correctamente (Enero-Noviembre tienen datos, Diciembre sin datos):
    - Enero: 44 consultantes, 64 consultas
    - Febrero: 33 consultantes, 64 consultas
    - Marzo: 44 consultantes, 64 consultas
    - Abril: 51 consultantes, 86 consultas
    - Mayo: 51 consultantes, 68 consultas
    - Junio: 44 consultantes, 65 consultas
    - Julio: 52 consultantes, 81 consultas
    - Agosto: 54 consultantes, 77 consultas
    - Septiembre: 53 consultantes, 67 consultas
    - Octubre: 60 consultantes, 80 consultas
    - Noviembre: 48 consultantes, 62 consultas
  - **Total 2025 (hasta noviembre): 536 consultantes distintos, 818 consultas**

## ✅ Completado (19/06/2026 — sesión noche: Procesamiento 2024-2025 CORRECTO — todos los 12 meses)
- **Análisis Mensual 2024 en Airtable — 12 MESES COMPLETOS CARGADOS**:
  - Script `procesar_2024.py` corregido para procesar filas sin horarios explícitos
  - Tabla "Análisis Mensual 2024" recreada con 12 registros:
    - Enero: 40 consultantes, 77 consultas
    - Febrero: 42 consultantes, 79 consultas
    - Marzo: 29 consultantes, 42 consultas
    - Abril: 45 consultantes, 64 consultas
    - Mayo: 51 consultantes, 70 consultas
    - Junio: 45 consultantes, 73 consultas
    - Julio: 41 consultantes, 57 consultas
    - Agosto: 31 consultantes, 35 consultas
    - Septiembre: 37 consultantes, 63 consultas
    - Octubre: 53 consultantes, 97 consultas
    - Noviembre: 58 consultantes, 103 consultas
    - Diciembre: 32 consultantes, 49 consultas
  - **Total 2024: 504 consultantes distintos, 809 consultas**

- **Análisis Mensual 2025 en Airtable — 12 MESES COMPLETOS CARGADOS (incluyendo DICIEMBRE)**:
  - Script `procesar_2025.py` corregido, ahora captura todos los meses
  - Tabla "Análisis Mensual 2025" recreada con 12 registros:
    - Enero: 44 consultantes, 64 consultas
    - Febrero: 33 consultantes, 64 consultas
    - Marzo: 45 consultantes, 65 consultas
    - Abril: 51 consultantes, 86 consultas
    - Mayo: 56 consultantes, 74 consultas
    - Junio: 47 consultantes, 72 consultas
    - Julio: 58 consultantes, 88 consultas
    - Agosto: 57 consultantes, 84 consultas
    - Septiembre: 60 consultantes, 75 consultas
    - Octubre: 60 consultantes, 80 consultas
    - Noviembre: 51 consultantes, 65 consultas
    - Diciembre: 53 consultantes, 68 consultas
  - **Total 2025: 615 consultantes distintos, 885 consultas**

## ✅ Completado (19/06/2026 — sesión noche: Procesamiento 2023 Completo + Corrección 2022)
- **Análisis Mensual 2023 en Airtable — TABLA CREADA Y CARGADA CORRECTAMENTE**:
  - Descargado archivo "Agendamientos" de Google Drive (Google Sheets) como Excel
  - Script `procesar_2023.py` procesa 12 bloques mensuales de fechas automáticamente
  - Tabla "Análisis Mensual 2023" creada y 12 registros cargados correctamente:
    - Enero: 50 consultantes, 77 consultas
    - Febrero: 44 consultantes, 64 consultas
    - Marzo: 56 consultantes, 100 consultas
    - Abril: 62 consultantes, 97 consultas
    - Mayo: 64 consultantes, 105 consultas
    - Junio: 58 consultantes, 103 consultas
    - Julio: 67 consultantes, 114 consultas
    - Agosto: 49 consultantes, 73 consultas
    - Septiembre: 46 consultantes, 82 consultas
    - Octubre: 49 consultantes, 81 consultas
    - Noviembre: 47 consultantes, 93 consultas
    - Diciembre: 37 consultantes, 75 consultas
  - **Total 2023: 651 consultantes distintos, 1,064 consultas**
  
- **Corrección de metodología**:
  - Identificado error: duplicación manual "Samara Sosa" en extracción de texto (semana 2 oct 2022)
  - Solución implementada: acceso directo a Excel eliminó errores de copia/pega
  - Scripts reutilizables: `procesar_2023.py` es template para 2024-2025

## ✅ Completado (18/06/2026 — sesión Skinner expansión integral)
- **Skinner v3: Identificación de usuario + roles diferenciados**
  - Herramienta `buscar_usuario`: identifica quién escribe (Jean, Milva, consultante, desconocido)
  - Respuestas diferenciadas por rol:
    - **Jean**: acceso admin (reportes, estadísticas, datos)
    - **Milva Servian (asistente)**: saludo personal + modo recepción de datos
    - **Consultantes registrados**: atención al cliente estándar
    - **Desconocidos**: modo prospección
  - 6 herramientas total: buscar_usuario + 5 de reportes/prospección
  - Prompt rediseñado con sistema de identificación automática
  - Deploy a Railway ✅ (PROMPTS_YAML_B64 regenerado, 10660 chars)

## 🔄 En progreso
- **Ñakurutu**: cargar años anteriores 2014–2022 (archivos en `Copia Planillas presupuestos/`)
- **Skinner**: integración Google Calendar (siguiente fase)

## ⏳ Pendiente
- Ñakurutu próximos archivos (en orden): `2022.xlsx`, `2021.xlsx`, `Extensivo Virtual 2021.xlsx`, `2020.xlsx`, `2019 Int.xlsx`, `2019 Ext.xlsx`, `2018.xlsx`, `2017.xlsx`, `2016.xlsx`, `2014.xlsx`
- **Skinner**: carga de contactos de la hoja "Consultantes" + integración Google Calendar
- Decidir qué hacer con el turno de prueba `JUE-2026-06-18-1830` en Airtable
- Desinstalar Avast Update Helper (sin urgencia)
- Considerar upgrade a Windows 11 a largo plazo

## 🧠 Decisiones tomadas
- Sistema profesional CC con metodología Ivan Lafuente
- No instalar Docker por ahora (disco justo, sin proyecto concreto)
- Samsung printer apps: NO tocar
- Disco externo 1 TB disponible para datos/backups
- Agente usa Claude Haiku 4.5 (rápido y económico para WhatsApp)
- Base Airtable en cuenta jeancle.010@gmail.com (NO via MCP — genera conflictos de auth)
- Slots de 60 min: Mar 14-19:30, Mié/Vier 8-13, Jue 15-19:30

## 🌙 Sesion cerrada: 30/05/2026 13:31
## 🌙 Sesion cerrada: 30/05/2026 13:33
## 🌙 Sesion cerrada: 01/06/2026 09:45
## 🌙 Sesion cerrada: 01/06/2026 10:14
## 🌙 Sesion cerrada: 01/06/2026 11:21
## 🌙 Sesion cerrada: 01/06/2026 11:32
## 🌙 Sesion cerrada: 01/06/2026 11:58
## 🌙 Sesion cerrada: 01/06/2026 17:13
## 🌙 Sesion cerrada: 01/06/2026 17:13
## 🌙 Sesion cerrada: 01/06/2026 17:14
## 🌙 Sesion cerrada: 01/06/2026 17:21
## 🌙 Sesion cerrada: 02/06/2026 11:41
## 🌙 Sesion cerrada: 02/06/2026 11:45
## 🌙 Sesion cerrada: 02/06/2026 17:33
## 🌙 Sesion cerrada: 02/06/2026 17:37
## 🌙 Sesion cerrada: 07/06/2026 15:14
## 🌙 Sesion cerrada: 09/06/2026 10:16
## 🌙 Sesion cerrada: 09/06/2026 10:16
## 🌙 Sesion cerrada: 09/06/2026 10:17
## 🌙 Sesion cerrada: 09/06/2026 10:17
## 🌙 Sesion cerrada: 09/06/2026 13:22
## 🌙 Sesion cerrada: 09/06/2026 15:03
## 🌙 Sesion cerrada: 09/06/2026 15:06
## 🌙 Sesion cerrada: 10/06/2026 15:02
## 🌙 Sesion cerrada: 10/06/2026 15:02
## 🌙 Sesion cerrada: 11/06/2026 09:27
## 🌙 Sesion cerrada: 11/06/2026 09:52
## 🌙 Sesion cerrada: 11/06/2026 11:18
## 🌙 Sesion cerrada: 11/06/2026 13:16
## 🌙 Sesion cerrada: 11/06/2026 13:26
## 🌙 Sesion cerrada: 11/06/2026 13:26
## 🌙 Sesion cerrada: 11/06/2026 19:07
## 🌙 Sesion cerrada: 15/06/2026 15:52
## 🌙 Sesion cerrada: 15/06/2026 15:52
## 🌙 Sesion cerrada: 15/06/2026 15:52
## 🌙 Sesion cerrada: 16/06/2026 09:54
## 🌙 Sesion cerrada: 16/06/2026 10:52
## 🌙 Sesion cerrada: 16/06/2026 11:44
## 🌙 Sesion cerrada: 16/06/2026 11:50
## 🌙 Sesion cerrada: 16/06/2026 11:51
## 🌙 Sesion cerrada: 16/06/2026 12:04
## 🌙 Sesion cerrada: 16/06/2026 12:05
## 🌙 Sesion cerrada: 16/06/2026 12:20
## 🌙 Sesion cerrada: 16/06/2026 12:23
## 🌙 Sesion cerrada: 16/06/2026 12:33
## 🌙 Sesion cerrada: 16/06/2026 12:33
## 🌙 Sesion cerrada: 16/06/2026 12:35
## 🌙 Sesion cerrada: 16/06/2026 12:36
## 🌙 Sesion cerrada: 16/06/2026 12:38
## 🌙 Sesion cerrada: 16/06/2026 12:44
## 🌙 Sesion cerrada: 16/06/2026 13:04
## 🌙 Sesion cerrada: 16/06/2026 13:04
## 🌙 Sesion cerrada: 16/06/2026 13:54
## 🌙 Sesion cerrada: 16/06/2026 14:01
## 🌙 Sesion cerrada: 18/06/2026 10:20
## 🌙 Sesion cerrada: 18/06/2026 10:24
## 🌙 Sesion cerrada: 18/06/2026 10:24
## 🌙 Sesion cerrada: 19/06/2026 16:43
## 🌙 Sesion cerrada: 19/06/2026 16:43
## 🌙 Sesion cerrada: 19/06/2026 17:33
## 🌙 Sesion cerrada: 19/06/2026 17:37
## 🌙 Sesion cerrada: 19/06/2026 19:10
## 🌙 Sesion cerrada: 19/06/2026 19:10
## 🌙 Sesion cerrada: 19/06/2026 19:28
