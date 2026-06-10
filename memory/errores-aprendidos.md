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
