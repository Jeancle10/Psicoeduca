# HANDOFF — 2026-06-01 — 17:14

## ✅ Completado en esta sesión
- Copiados archivos de referencia visual a `materiales/referencias-visuales/`
- Guión completo de presentación AF (`materiales/presentacion-AF-guion.md`, 22 slides)
- Generado `materiales/presentacion-AF.pptx` v2 con todas las correcciones:
  - Fondo crema oscuro, títulos centrados, logo en todos los slides
  - Super Stock (Paraguay), CC corregido (asalto como EI — Jean tenía razón)
  - Slide nuevo: Estímulo Discriminativo (Ed+ / Ed−)
  - Slide nuevo: Ejemplos disposicionales/motivacionales en contexto Paraguay
  - Foto de Jean como fondo en slide de cierre
- Generado `materiales/presentacion-bases-filosoficas.pptx` (Cap 3 Froxán):
  - Caso: Homero Simpson, 20 slides, para psicólogos sin base en AF
- Creado `memory/estilo-presentaciones.md` — sistema de estilo maestro (nunca más redefinir diseño)
- Creado `memory/MEMORY.md` — índice de memoria del proyecto
- Instalada extensión Python de Microsoft en VS Code (4 componentes: Python, Pylance, Debugpy, Envs)
- Instalado python-pptx

## 🔄 En progreso (quedó a medias)
- Jean está revisando las 2 presentaciones — pendiente feedback y correcciones
- Avast Update Helper: sigue pendiente (sin urgencia, no hace nada activo)

## ⏳ Próxima sesión — primer paso EXACTO
1. Preguntar a Jean qué correcciones tiene de las 2 presentaciones
2. Aplicar correcciones y regenerar el `.pptx` con el script correspondiente
3. Cuando estén aprobadas → definir identidad de marca de PsicoEduca
4. (Opcional) Avast: `msiexec /x {19C3AB22-3718-4E4D-B203-242F5001565B} /qn`

## ⚠️ Errores encontrados hoy
- `presentacion-AF.pptx` abierto en PowerPoint → Permission denied al regenerar. Solución: cerrar PowerPoint antes de ejecutar el script.
- Emoji en `print()` → UnicodeEncodeError en PowerShell. Solución: ejecutar con `exec(open(...).read())` con encoding utf-8.

## 🧠 Decisiones tomadas
- EI en el ejemplo de CC: **asalto** (no ataque de pánico — el pánico es la RI)
- Supermercado de referencia: **Super Stock** (Villa Morra, Asunción)
- Logo para slides crema: `PsicoEduca Logo final_Mesa de trabajo 1 copia 4.png`
- Foto de cierre: `Desktop\PsicoEduca\Marketing\BOOK\sentado.JPG`
- Para importar a Canva: Canva → Crear diseño → Importar presentación → subir .pptx
- Estilo guardado en `memory/estilo-presentaciones.md` → se aplica automáticamente

## 📁 Archivos creados/modificados
- `bitacora/2026-06-01_1714.md` — esta sesión
- `.claude/handoff.md` — este archivo
- `materiales/referencias-visuales/` — 3 PDFs de referencia visual
- `materiales/presentacion-AF-guion.md` — guión 22 slides
- `materiales/crear_presentacion.py` — script v2
- `materiales/presentacion-AF.pptx` — presentación AF v2 (24 slides)
- `materiales/crear_bases_filosoficas.py` — script presentación filosófica
- `materiales/presentacion-bases-filosoficas.pptx` — Bases Filosóficas (20 slides)
- `memory/estilo-presentaciones.md` — sistema de estilo maestro
- `memory/MEMORY.md` — índice de memoria
