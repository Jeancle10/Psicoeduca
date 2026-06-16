# Fase 4: Integraciones — Google Docs + PDF

## 🎯 Objetivo

Automatizar la creación de documentos y exportación de reportes cuando se carga una evaluación.

---

## ✅ Completado

### 1. Google Drive Manager (`utils/google_drive.py`)
- ✅ Autenticación OAuth + Token directo
- ✅ Crear documentos en Drive automáticamente
- ✅ Copiar desde plantillas
- ✅ Insertar contenido (texto)
- ✅ Compartir documentos con otros usuarios
- ✅ Generar fichas de consultantes con formato profesional

**Métodos disponibles:**
```python
class GoogleDriveManager:
    def crear_documento(titulo, contenido_html, plantilla_id)
    def crear_ficha_consultante(consultante, evaluacion)
    def compartir_documento(doc_id, email, rol)
```

### 2. PDF Generator (`utils/pdf_generator.py`)
- ✅ Generación de PDFs profesionales con reportlab
- ✅ Fichas de evaluación con datos personales
- ✅ Tablas de resultados (STAI, BDI, BFI-5, SCL-90-R)
- ✅ Estilos personalizados (colores PsicoEduca)
- ✅ Exportación a archivo o BytesIO

**Métodos disponibles:**
```python
class PDFGenerator:
    def generar_ficha_evaluacion(consultante, evaluacion)
    def _crear_seccion_stai(evaluacion)
    def _crear_seccion_bdi(evaluacion)
    def _crear_seccion_bfi(evaluacion)
    def _crear_seccion_scl90(evaluacion)
```

### 3. API Endpoints (`api/integraciones.py`)

#### POST `/api/integraciones/google-docs/{evaluacion_id}`
Crea un Google Doc automáticamente con la ficha del consultante

**Request body (opcional):**
```json
{
  "compartir_con": "email@example.com"
}
```

**Response:**
```json
{
  "success": true,
  "documento": {
    "id": "doc_id_aqui",
    "url": "https://docs.google.com/document/d/...",
    "titulo": "Ficha — Juan García"
  },
  "mensaje": "Ficha creada exitosamente en Google Drive"
}
```

---

#### GET `/api/integraciones/pdf/{evaluacion_id}`
Descarga un PDF con los resultados de la evaluación

**Response:**
- Archivo PDF directamente (descarga en navegador)
- Nombre: `Ficha_[Nombre]_[Apellido].pdf`

**Headers:**
```
Content-Type: application/pdf
Content-Disposition: attachment; filename="Ficha_Juan_García.pdf"
```

---

#### GET `/api/integraciones/drive/config`
Obtiene la configuración actual de Google Drive

**Response:**
```json
{
  "folder_id": "1GTOx8fihwgG1dFonkR_wnkfnzGiS3rhj",
  "carpeta_nombre": "Consultantes IA",
  "autorizado": true,
  "url_carpeta": "https://drive.google.com/drive/folders/1GTOx8fihwgG1dFonkR_wnkfnzGiS3rhj"
}
```

---

#### POST `/api/integraciones/drive/autorizar`
Endpoint para autorización OAuth (placeholder, implementación pendiente)

---

## 📋 Contenido de Ficha (Google Docs + PDF)

```
FICHA PSICOLÓGICA

═══════════════════════════════════════════════════════════════

DATOS PERSONALES:
  - Nombre y Apellido
  - Edad
  - Fecha de Nacimiento
  - Celular
  - Email
  - Fecha de Evaluación

RESULTADOS DE TESTS PSICOMÉTRICOS:

1. STAI (State-Trait Anxiety Inventory)
   - STAI-E (Estado): Puntuación | Percentil | Categoría
   - STAI-R (Rasgo): Puntuación | Percentil | Categoría

2. BDI (Beck Depression Inventory)
   - Puntuación | Categoría

3. BFI-5 (Big Five Inventory)
   - Neuroticismo | Extraversión | Apertura | Amabilidad | Responsabilidad

4. SCL-90-R (Symptom Checklist 90-Revised)
   - Puntuación | Categoría

═══════════════════════════════════════════════════════════════

INTERPRETACIÓN Y RECOMENDACIONES:
(Completar según criterio profesional)
```

---

## 🔧 Configuración Necesaria

### Variables de Entorno

```bash
# Google Drive
GOOGLE_DRIVE_FOLDER_ID=1GTOx8fihwgG1dFonkR_wnkfnzGiS3rhj
GOOGLE_ACCESS_TOKEN=your_access_token_here  # Obtenido de OAuth

# Base de datos
DATABASE_URL=postgresql://...
```

### Dependencias Agregadas

```
reportlab==4.0.9      # Generación de PDFs
PyPDF2==3.0.1         # Manipulación de PDFs (opcional)
google-auth-oauthlib==1.2.0
google-api-python-client==2.120.0
```

---

## 📝 Casos de Uso

### Caso 1: Crear Google Doc automáticamente
```bash
curl -X POST https://[dominio]/api/integraciones/google-docs/5 \
  -H "Content-Type: application/json" \
  -d '{
    "compartir_con": "psicologia@example.com"
  }'
```

**Resultado:** Se crea un documento en Drive carpeta "Consultantes IA" y se comparte con el email especificado.

---

### Caso 2: Descargar PDF de evaluación
```bash
curl -X GET https://[dominio]/api/integraciones/pdf/5 \
  -o Ficha_Juan_García.pdf
```

**Resultado:** Se descarga un PDF profesional con todos los resultados.

---

### Caso 3: Integración Frontend
```javascript
// Después de cargar evaluación, crear Google Doc
const evaluacionId = 5;
const response = await fetch(`/api/integraciones/google-docs/${evaluacionId}`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    compartir_con: 'jean@psicoeduca.com'
  })
});

const resultado = await response.json();
console.log('Documento creado:', resultado.documento.url);
```

---

## 🚀 Implementación Pendiente

### Autenticación OAuth Completa
- [ ] Implementar flujo OAuth completo en frontend
- [ ] Guardar refresh token en BD
- [ ] Renovar tokens automáticamente

### Plantillas
- [ ] Crear plantilla Google Doc profesional
- [ ] Usar como base para fichas (en lugar de generar desde cero)

### Notificaciones
- [ ] Enviar email cuando se crea documento
- [ ] Notificación en sistema de la app

### Mejoras PDF
- [ ] Agregar gráficos/charts al PDF
- [ ] Firma digital del psicólogo
- [ ] Número de referencia único

---

## 📊 Flujo de Datos

```
Frontend (formulario 135 preguntas)
    ↓
Backend (calcular tests)
    ↓
Evaluacion guardada en BD
    ↓
POST /api/integraciones/google-docs/{id}
    ↓
Google Drive API
    ↓
Documento creado en Drive
    ↓
Share link devuelto al frontend
```

---

## 🔗 Archivos Modificados/Creados

```
✅ NUEVOS:
  - utils/google_drive.py (Google Drive integration)
  - utils/pdf_generator.py (PDF generation)
  - api/integraciones.py (3 endpoints + helpers)

✏️ MODIFICADOS:
  - api/__init__.py (registrar blueprint)
  - requirements.txt (reportlab + google-api-python-client)
```

---

## 📈 Próximas Fases

- **Fase 5:** Testing + optimizaciones (2-3 horas)
- **Fase 6:** Deploy final + documentación (1 hora)

**Estimado restante:** ~4 horas más (1-2 sesiones)
