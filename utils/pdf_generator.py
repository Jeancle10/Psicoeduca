"""
Generación de PDFs con resultados de evaluaciones
Usa reportlab para crear documentos profesionales
"""

from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.pdfgen import canvas
import io


class PDFGenerator:
    def __init__(self, filename=None):
        """
        Inicializa el generador de PDF

        Args:
            filename: Ruta del archivo de salida (opcional, si None devuelve bytes)
        """
        self.filename = filename
        self.styles = getSampleStyleSheet()
        self._crear_estilos_custom()

    def _crear_estilos_custom(self):
        """Crea estilos personalizados para la empresa"""
        # Color púrpura de PsicoEduca
        color_primario = colors.HexColor("#667eea")
        color_secundario = colors.HexColor("#764ba2")

        self.styles.add(ParagraphStyle(
            name='TituloPersonalizado',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=color_primario,
            spaceAfter=12,
            alignment=1  # Centro
        ))

        self.styles.add(ParagraphStyle(
            name='SubtituloPersonalizado',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=color_secundario,
            spaceAfter=10
        ))

        self.styles.add(ParagraphStyle(
            name='NormalPersonalizado',
            parent=self.styles['Normal'],
            fontSize=10,
            leading=12
        ))

    def generar_ficha_evaluacion(self, consultante, evaluacion):
        """
        Genera un PDF con la ficha de evaluación completa

        Args:
            consultante: dict con datos del consultante
            evaluacion: dict con resultados de evaluación

        Returns:
            bytes o archivo: PDF generado
        """
        # Usar buffer o archivo
        if self.filename:
            pdf_file = self.filename
        else:
            pdf_file = io.BytesIO()

        # Crear documento
        doc = SimpleDocTemplate(
            pdf_file,
            pagesize=letter,
            topMargin=0.75 * inch,
            bottomMargin=0.75 * inch,
            leftMargin=0.75 * inch,
            rightMargin=0.75 * inch
        )

        # Elementos del documento
        elements = []

        # Título
        titulo = Paragraph(
            "FICHA PSICOLÓGICA",
            self.styles['TituloPersonalizado']
        )
        elements.append(titulo)
        elements.append(Spacer(1, 0.2 * inch))

        # Datos del consultante
        nombre_completo = f"{consultante.get('nombre', 'N/A')} {consultante.get('apellido', 'N/A')}".upper()
        consultante_info = Paragraph(
            f"<b>{nombre_completo}</b>",
            self.styles['Heading2']
        )
        elements.append(consultante_info)
        elements.append(Spacer(1, 0.1 * inch))

        # Tabla de datos personales
        data_consultante = [
            ['Edad', f"{consultante.get('edad', 'N/A')} años"],
            ['Fecha de Nacimiento', consultante.get('fecha_nacimiento', 'N/A')],
            ['Celular', consultante.get('celular', 'N/A')],
            ['Email', consultante.get('email', 'N/A')],
            ['Fecha de Evaluación', datetime.now().strftime('%d/%m/%Y %H:%M')]
        ]

        tabla_datos = Table(data_consultante, colWidths=[1.5 * inch, 3.5 * inch])
        tabla_datos.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f0f0')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey)
        ]))
        elements.append(tabla_datos)
        elements.append(Spacer(1, 0.3 * inch))

        # Resultados de tests
        elements.append(Paragraph("RESULTADOS DE EVALUACIONES PSICOMÉTRICAS", self.styles['SubtituloPersonalizado']))
        elements.append(Spacer(1, 0.15 * inch))

        # STAI
        elements.append(self._crear_seccion_stai(evaluacion))
        elements.append(Spacer(1, 0.2 * inch))

        # BDI
        elements.append(self._crear_seccion_bdi(evaluacion))
        elements.append(Spacer(1, 0.2 * inch))

        # BFI-5
        elements.append(self._crear_seccion_bfi(evaluacion))
        elements.append(Spacer(1, 0.2 * inch))

        # SCL-90-R
        elements.append(self._crear_seccion_scl90(evaluacion))
        elements.append(Spacer(1, 0.3 * inch))

        # Pie de página
        elements.append(Paragraph(
            "<i>Generado automáticamente por PsicoEduca — Sistema de Evaluaciones Psicométricas</i>",
            self.styles['Normal']
        ))

        # Construir PDF
        doc.build(elements)

        # Retornar
        if not self.filename:
            pdf_file.seek(0)
            return pdf_file.getvalue()

        return True

    def _crear_seccion_stai(self, evaluacion):
        """Crea sección de STAI"""
        stai = evaluacion.get('stai_estado', {})
        stai_r = evaluacion.get('stai_rasgo', {})

        data = [
            ['TEST', 'Puntuación', 'Percentil', 'Categoría'],
            ['STAI-E (Estado)', str(stai.get('puntuacion', 'N/A')), str(stai.get('percentil', 'N/A')), stai.get('categoria', 'N/A')],
            ['STAI-R (Rasgo)', str(stai_r.get('puntuacion', 'N/A')), str(stai_r.get('percentil', 'N/A')), stai_r.get('categoria', 'N/A')]
        ]

        tabla = Table(data, colWidths=[1.5 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch])
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey)
        ]))

        return tabla

    def _crear_seccion_bdi(self, evaluacion):
        """Crea sección de BDI"""
        bdi = evaluacion.get('bdi', {})

        data = [
            ['TEST', 'Puntuación', 'Categoría'],
            ['BDI (Depresión)', str(bdi.get('puntuacion', 'N/A')), bdi.get('categoria', 'N/A')]
        ]

        tabla = Table(data, colWidths=[2 * inch, 1.5 * inch, 2 * inch])
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#764ba2')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey)
        ]))

        return tabla

    def _crear_seccion_bfi(self, evaluacion):
        """Crea sección de BFI-5"""
        bfi = evaluacion.get('bfi', {})

        data = [
            ['Dimensión', 'Score (1-5)'],
            ['Neuroticismo', str(bfi.get('neuroticismo', 'N/A'))],
            ['Extraversión', str(bfi.get('extraversion', 'N/A'))],
            ['Apertura', str(bfi.get('apertura', 'N/A'))],
            ['Amabilidad', str(bfi.get('amabilidad', 'N/A'))],
            ['Responsabilidad', str(bfi.get('responsabilidad', 'N/A'))]
        ]

        tabla = Table(data, colWidths=[2 * inch, 2 * inch])
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey)
        ]))

        return tabla

    def _crear_seccion_scl90(self, evaluacion):
        """Crea sección de SCL-90-R"""
        scl90 = evaluacion.get('scl90', {})

        data = [
            ['TEST', 'Puntuación', 'Categoría'],
            ['SCL-90-R (Síntomas)', str(scl90.get('puntuacion', 'N/A')), scl90.get('categoria', 'N/A')]
        ]

        tabla = Table(data, colWidths=[2 * inch, 1.5 * inch, 2 * inch])
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#764ba2')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey)
        ]))

        return tabla
