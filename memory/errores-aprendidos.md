# ⚠️ Errores aprendidos — psicoeduca
> Cada vez que CC cometa un error, se registra aca para no repetirlo.
> Formato: fecha - que paso - por que - como se resuelve

## 10/06/2026 - Token Airtable (PAT) da 403 aunque la cuenta es correcta
- Que paso: se probaron 4 Personal Access Tokens distintos de Airtable, generados con los scopes correctos (data.records:read + write) y acceso a la base "PsicoEduca — Agenda", todos confirmados desde la cuenta jeancle.010@gmail.com. Todos dieron 401 o 403.
- Por que: el usuario asociado al PAT (`usr8MwG0xCVOFKF09`) no tiene NINGUNA base visible vía `/v0/meta/bases`, aunque la conexión Airtable de Claude (MCP/OAuth) sí ve la base con permiso "create" usando aparentemente la misma cuenta. Posible cuenta de Airtable duplicada con el mismo email (ej. registro con Google vs email/contraseña).
- Como se resuelve: pendiente — revisar airtable.com/account por workspaces/cuentas duplicadas, probar generar el token desde la app móvil, o contactar soporte de Airtable. Mientras tanto, para tareas puntuales de datos/schema se puede usar la conexión Airtable de Claude (MCP) directamente, sin depender del PAT.

## 10/06/2026 - Token pegado incompleto
- Que paso: uno de los tokens pegados por Jean tenia el secret de 40 caracteres en vez de 64 (se cortó al copiar) y dio 401.
- Por que: el botón de copiar/selección manual en la página del token a veces no copia el valor completo.
- Como se resuelve: antes de probar un token nuevo, verificar que la parte despues del punto tenga 64 caracteres (`len(key.split('.')[1]) == 64`).

## 11/06/2026 - `railway up` no sube archivos del .gitignore (config/prompts.yaml y config/business.yaml faltaban en producción)
- Que paso: el deploy a Railway quedó online y respondiendo, pero Skinner usaba el prompt genérico de fallback ("Sos un asistente útil de WhatsApp...") en vez de su personalidad real, y no mandaba el menú de bienvenida.
- Por que: `config/prompts.yaml` y `config/business.yaml` están en `.gitignore` (contienen datos del negocio, no van a git). `railway up` respeta el `.gitignore` al subir el build context, así que esos archivos nunca llegaban al contenedor. Crear un `.railwayignore` NO sirve para "rescatarlos" — railway igual los excluye.
- Como se resuelve: se creó `docker-entrypoint.sh` que, al arrancar el contenedor, decodifica esos dos archivos desde variables de entorno de Railway (`PROMPTS_YAML_B64`, `BUSINESS_YAML_B64`, contenido en base64) y los escribe en `config/`. El `Dockerfile` usa ese entrypoint. IMPORTANTE: si se edita `config/prompts.yaml` o `config/business.yaml` en el futuro, hay que regenerar esas dos variables base64 y volver a cargarlas en Railway, o el cambio no se reflejará en producción.
