"""
Integración con Google Drive API
- Crear documentos automáticamente
- Generar plantillas de fichas
"""

import os
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials as ServiceAccountCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Scopes de Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']

class GoogleDriveManager:
    def __init__(self, credentials_path=None, access_token=None):
        """
        Inicializa el cliente de Google Drive

        Args:
            credentials_path: Ruta a credentials.json (OAuth)
            access_token: Token de acceso directo (si ya está autorizado)
        """
        self.service = None
        self.folder_id = os.getenv('GOOGLE_DRIVE_FOLDER_ID')

        if not self.folder_id:
            raise ValueError("GOOGLE_DRIVE_FOLDER_ID no está configurado")

        if access_token:
            self._authenticate_with_token(access_token)
        elif credentials_path:
            self._authenticate_with_oauth(credentials_path)
        else:
            raise ValueError("Se requiere credentials_path o access_token")

    def _authenticate_with_token(self, access_token):
        """Autentica usando un token de acceso directo"""
        try:
            self.service = build('drive', 'v3',
                                credentials=Credentials(token=access_token))
        except Exception as e:
            raise Exception(f"Error autenticando con token: {str(e)}")

    def _authenticate_with_oauth(self, credentials_path):
        """Autentica usando OAuth (credentials.json)"""
        try:
            creds = None

            # Si token.json existe, usar credenciales guardadas
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)

            # Si no hay credenciales válidas, hacer flow de autenticación
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        credentials_path, SCOPES)
                    creds = flow.run_local_server(port=0)

                # Guardar credenciales para próximos usos
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())

            self.service = build('drive', 'v3', credentials=creds)
        except Exception as e:
            raise Exception(f"Error en autenticación OAuth: {str(e)}")

    def crear_documento(self, titulo, contenido_html=None, plantilla_id=None):
        """
        Crea un documento en Google Docs

        Args:
            titulo: Título del documento
            contenido_html: HTML para insertar (opcional)
            plantilla_id: ID de documento plantilla para copiar (opcional)

        Returns:
            dict: Info del documento creado (id, webViewLink)
        """
        try:
            if plantilla_id:
                # Copiar desde plantilla
                file_metadata = {
                    'name': titulo,
                    'parents': [self.folder_id],
                    'mimeType': 'application/vnd.google-apps.document'
                }
                doc = self.service.files().copy(
                    fileId=plantilla_id,
                    body=file_metadata
                ).execute()
                doc_id = doc.get('id')
            else:
                # Crear documento nuevo
                file_metadata = {
                    'name': titulo,
                    'parents': [self.folder_id],
                    'mimeType': 'application/vnd.google-apps.document'
                }
                doc = self.service.files().create(
                    body=file_metadata,
                    fields='id, webViewLink'
                ).execute()
                doc_id = doc.get('id')

            # Si hay contenido, insertarlo
            if contenido_html and not plantilla_id:
                self._insertar_contenido(doc_id, contenido_html)

            return {
                'id': doc_id,
                'url': doc.get('webViewLink'),
                'titulo': titulo
            }
        except HttpError as error:
            raise Exception(f"Error creando documento: {error}")

    def _insertar_contenido(self, doc_id, contenido_html):
        """Inserta contenido HTML en un documento"""
        from google.apps import docs_v1

        try:
            docs_service = build('docs', 'v1')

            # Para usar HTML, necesitamos convertir a requests de Google Docs
            # Por ahora, insertamos como texto plano
            requests = [
                {
                    'insertText': {
                        'text': contenido_html,
                        'location': {'index': 1}
                    }
                }
            ]

            docs_service.documents().batchUpdate(
                documentId=doc_id,
                body={'requests': requests}
            ).execute()
        except Exception as e:
            print(f"Advertencia: No se pudo insertar contenido: {str(e)}")

    def crear_ficha_consultante(self, consultante, evaluacion):
        """
        Crea una ficha de consultante con resultados

        Args:
            consultante: dict con datos del consultante
            evaluacion: dict con resultados de evaluación

        Returns:
            dict: Info del documento creado
        """
        titulo = f"Ficha — {consultante['nombre']} {consultante['apellido']}"

        # Generar contenido de la ficha
        contenido = self._generar_contenido_ficha(consultante, evaluacion)

        # Crear documento
        return self.crear_documento(titulo, contenido)

    def _generar_contenido_ficha(self, consultante, evaluacion):
        """Genera contenido formateado para la ficha"""
        from datetime import datetime

        edad = consultante.get('edad', 'N/A')

        contenido = f"""
FICHA PSICOLÓGICA — {consultante['nombre'].upper()} {consultante['apellido'].upper()}

═══════════════════════════════════════════════════════════════

DATOS PERSONALES:
─────────────────
Nombre y Apellido: {consultante['nombre']} {consultante['apellido']}
Edad: {edad} años
Fecha de Nacimiento: {consultante.get('fecha_nacimiento', 'N/A')}
Celular: {consultante.get('celular', 'N/A')}
Email: {consultante.get('email', 'N/A')}

EVALUACIÓN:
───────────
Fecha de Evaluación: {datetime.now().strftime('%d/%m/%Y %H:%M')}

RESULTADOS DE TESTS PSICOMÉTRICOS:
═══════════════════════════════════

1. STAI (State-Trait Anxiety Inventory)
   ─────────────────────────────────────
   STAI-E (Estado):
   • Puntuación: {evaluacion.get('stai_estado', {}).get('puntuacion', 'N/A')}
   • Percentil: {evaluacion.get('stai_estado', {}).get('percentil', 'N/A')}
   • Categoría: {evaluacion.get('stai_estado', {}).get('categoria', 'N/A')}

   STAI-R (Rasgo):
   • Puntuación: {evaluacion.get('stai_rasgo', {}).get('puntuacion', 'N/A')}
   • Percentil: {evaluacion.get('stai_rasgo', {}).get('percentil', 'N/A')}
   • Categoría: {evaluacion.get('stai_rasgo', {}).get('categoria', 'N/A')}

2. BDI (Beck Depression Inventory)
   ───────────────────────────────
   • Puntuación: {evaluacion.get('bdi', {}).get('puntuacion', 'N/A')}
   • Categoría: {evaluacion.get('bdi', {}).get('categoria', 'N/A')}

3. BFI-5 (Big Five Inventory)
   ──────────────────────────
   • Neuroticismo: {evaluacion.get('bfi', {}).get('neuroticismo', 'N/A')}/5
   • Extraversión: {evaluacion.get('bfi', {}).get('extraversion', 'N/A')}/5
   • Apertura: {evaluacion.get('bfi', {}).get('apertura', 'N/A')}/5
   • Amabilidad: {evaluacion.get('bfi', {}).get('amabilidad', 'N/A')}/5
   • Responsabilidad: {evaluacion.get('bfi', {}).get('responsabilidad', 'N/A')}/5

4. SCL-90-R (Symptom Checklist 90-Revised)
   ────────────────────────────────────────
   • Puntuación: {evaluacion.get('scl90', {}).get('puntuacion', 'N/A')}
   • Categoría: {evaluacion.get('scl90', {}).get('categoria', 'N/A')}

═══════════════════════════════════════════════════════════════

INTERPRETACIÓN Y RECOMENDACIONES:
─────────────────────────────────
(Completar según criterio profesional)

═══════════════════════════════════════════════════════════════

Profesional: _______________________    Fecha: {datetime.now().strftime('%d/%m/%Y')}
"""
        return contenido.strip()

    def compartir_documento(self, doc_id, email, rol='reader'):
        """
        Comparte un documento con otra persona

        Args:
            doc_id: ID del documento
            email: Email de la persona
            rol: 'reader', 'writer', 'commenter'
        """
        try:
            permission = {
                'type': 'user',
                'role': rol,
                'emailAddress': email
            }

            self.service.permissions().create(
                fileId=doc_id,
                body=permission,
                fields='id'
            ).execute()

            return True
        except HttpError as error:
            raise Exception(f"Error compartiendo documento: {error}")
