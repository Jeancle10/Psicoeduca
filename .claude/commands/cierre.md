El command /cierre hace TODO esto en orden:

PASO 1 — BITACORA: ejecuta date '+%Y-%m-%d' para la fecha real. Despues
ESCRIBI vos (Claude) un resumen de la conversacion de hoy en
bitacora/[fecha].md (si ya existe hoy, agrega _HHMM con date '+%H%M').
NO uses /export: Claude no puede ejecutar slash commands. Escribi el archivo
a mano con el resumen de lo que se hizo en la sesion.

PASO 2 — HANDOFF: crea .claude/handoff.md con:
# HANDOFF — [fecha real] — [hora real]
## ✅ Completado en esta sesion
## 🔄 En progreso (quedo a medias)
## ⏳ Proxima sesion — primer paso EXACTO sin ambiguedad
## ⚠️ Errores encontrados hoy (o "Ninguno")
## 🧠 Decisiones tomadas
## 📁 Archivos modificados

PASO 2b — ARCHIVAR HANDOFF: ejecuta
mkdir -p .claude/handoffs && cp .claude/handoff.md ".claude/handoffs/handoff_$(date +%Y%m%d_%H%M).md"
Esto garantiza que el handoff queda archivado con timestamp ahora, sin depender de cerrar la conversacion (en VS Code no siempre se dispara SessionEnd).

PASO 3 — COMMIT + PUSH: git add . / mostra git status / commit con formato
[feat/fix/docs/config/refactor]: [descripcion]
Despues ejecuta git push para subir los cambios a GitHub.

PASO 4 — MEMORIA: actualiza memory/progreso.md. Si hubo errores,
actualiza memory/errores-aprendidos.md. Si hubo correcciones de
comportamiento, preguntame si agrego regla al CLAUDE.md.

PASO 5 — INDICE DE SESIONES: en VS Code no se puede renombrar la sesion del
panel (la app cachea los nombres y no relee archivos). Por eso llevamos un
indice propio en memory/sesiones.md — queda buscable y te deja retomar
cualquier sesion. Sugeri 3 nombres segun lo trabajado, que el alumno elija.
Despues obtene el codigo de la sesion activa y registrala:
  PROJ=$(basename "$(pwd)")
  DIR=$(ls -dt ~/.claude/projects/*"$PROJ"/ | head -1)
  SID=$(basename "$(ls -t "$DIR"*.jsonl | head -1)" .jsonl)
Agrega a memory/sesiones.md una fila: Nombre elegido | codigo (SID) | fecha |
resumen de 1 linea. Si el archivo no existe, crealo con el encabezado.
Para retomar una sesion despues: claude --resume <codigo>.

PASO 6 — CONFIRMAR: mostra "✅ Commit: [mensaje] — pushed" y resumen
de cada cosa guardada.
Decime: "✅ Todo guardado y archivado. Podes seguir trabajando o cerrar la conversacion cuando quieras."
