# 🎯 Decisiones — psicoeduca
> Por que elegiste cada tecnologia o enfoque

## 30/05/2026 - Sistema profesional Claude Code
- Elegimos configurar CC con el sistema completo: memoria + hooks + commands
- Por que: es la diferencia entre usar CC como un chat y usarlo como un profesional

## 10/06/2026 - Generar datos de Airtable vía conexión MCP de Claude, no vía PAT
- Ante el bloqueo persistente del PAT (403, ver errores-aprendidos.md), se generaron los 63 turnos directamente con la conexión Airtable de Claude
- Por que: desbloquea la agenda para esta semana sin esperar a resolver el problema de cuenta. Esto es solo para tareas puntuales de schema/datos — el agente Skinner en producción SI necesita un PAT funcional para leer/escribir en tiempo real
