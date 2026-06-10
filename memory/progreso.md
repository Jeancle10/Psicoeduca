# 📊 Progreso — psicoeduca
## Ultima sesion: 10/06/2026 (tarde, 16:20)
## Estado actual: Agente Skinner en construcción — Agenda Airtable lista, falta token API ⚙️

## ✅ Completado
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

## 🔄 En progreso
- Token Airtable (PAT) para `.env`: 4 tokens probados, todos 403 Forbidden — posible cuenta Airtable duplicada (ver errores-aprendidos.md)
- Generador de turnos: código listo, sigue bloqueado por el token

## ⏳ Pendiente
- Resolver el problema de cuenta duplicada de Airtable y conseguir un PAT funcional (ver handoff para pasos)
- Correr `python -m agent.tools.generador_turnos --semanas 2` una vez resuelto el token (validación)
- Configurar prompts.yaml del agente (personalidad de Skinner)
- Conectar WhatsApp (Meta o Twilio)
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
