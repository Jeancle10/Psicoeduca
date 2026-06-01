"""
Genera: presentacion-AF.pptx  v2
Correcciones aplicadas:
 1. Fondo CREAM2 en todos los slides
 2. Titulos centrados
 3. Logo en todos los slides
 4. Texto proporcional al espacio (fuentes mas grandes)
 5. Super Stock en vez de Kwik-E-Mart (contexto Paraguay)
 6. CC corregido: Asalto como EI (no ataque de panico)
 7. Tabla slide 12 centrada y letra grande
 8. Slide nuevo: Estimulo Discriminativo
 9. Slide nuevo: Ejemplos disposicionales/motivacionales
10. Slide final con foto de Jean como fondo
"""
from pptx import Presentation
from pptx.util import Cm, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from lxml import etree
from pptx.oxml.ns import qn
import copy

# ── COLORES ─────────────────────────────────────────────
BG     = RGBColor(0xE8, 0xE3, 0xD8)   # crema oscuro (el que le gusta)
NAVY   = RGBColor(0x1B, 0x3A, 0x5C)
BLACK  = RGBColor(0x1A, 0x1A, 0x1A)
GRAY   = RGBColor(0x66, 0x66, 0x66)
LGRAY  = RGBColor(0xCC, 0xC8, 0xC0)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
BLUE   = RGBColor(0x2E, 0x76, 0xA0)
RED    = RGBColor(0xCC, 0x33, 0x33)
GREEN  = RGBColor(0x22, 0x77, 0x44)
BOXBG  = RGBColor(0xD8, 0xD2, 0xC5)

SERIF = 'Georgia'
SANS  = 'Calibri'

W  = Cm(33.87)
H  = Cm(19.05)
ML = Cm(1.8)
CW = Cm(30.27)

# ── RUTAS ───────────────────────────────────────────────
LOGO  = r'C:\Users\MI PC\Desktop\PsicoEduca\Marketing\PsicoEduca Logo final_Mesa de trabajo 1 copia 4.png'
PHOTO = r'C:\Users\MI PC\Desktop\PsicoEduca\Marketing\BOOK\sentado.JPG'

prs = Presentation()
prs.slide_width  = W
prs.slide_height = H
blank = prs.slide_layouts[6]


# ── HELPERS ─────────────────────────────────────────────

def bg(slide, color=BG):
    f = slide.background.fill
    f.solid()
    f.fore_color.rgb = color


def hline(slide, x, y, w, color=BLACK, thick=Pt(1.5)):
    s = slide.shapes.add_shape(1, x, y, w, thick)
    s.fill.solid()
    s.fill.fore_color.rgb = color
    s.line.fill.background()


def txt(slide, text, x, y, w, h,
        font=SANS, size=16, bold=False, italic=False,
        color=BLACK, align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    p  = tf.paragraphs[0]
    p.alignment = align
    r  = p.add_run()
    r.text        = text
    r.font.name   = font
    r.font.size   = Pt(size)
    r.font.bold   = bold
    r.font.italic = italic
    r.font.color.rgb = color
    return tb


def paras(slide, lines, x, y, w, h,
          font=SANS, size=15, color=BLACK, align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        if isinstance(ln, dict):
            r = p.add_run()
            r.text           = ln.get('t', '')
            r.font.name      = ln.get('font', font)
            r.font.size      = Pt(ln.get('size', size))
            r.font.bold      = ln.get('bold', False)
            r.font.italic    = ln.get('italic', False)
            r.font.color.rgb = ln.get('color', color)
        else:
            r = p.add_run()
            r.text = str(ln)
            r.font.name  = font
            r.font.size  = Pt(size)
            r.font.color.rgb = color
    return tb


def add_logo(slide):
    """Logo PsicoEduca arriba a la derecha."""
    slide.shapes.add_picture(LOGO, W - Cm(4.2), Cm(0.2), Cm(3.8), Cm(3.0))


def footer(slide):
    txt(slide, 'Lic. Jean Clemotte  |  @Psico_Educa20',
        ML, H - Cm(1.2), Cm(22), Cm(0.9),
        SANS, 11, italic=True, color=GRAY)


def dividers(slide):
    hline(slide, ML, Cm(1.5), CW - Cm(4.5))   # deja espacio para logo
    hline(slide, ML, Cm(1.8), CW - Cm(4.5))
    hline(slide, ML, H - Cm(1.6), CW)
    hline(slide, ML, H - Cm(1.3), CW)


def top_label(slide, label='ANÁLISIS FUNCIONAL DE LA CONDUCTA'):
    txt(slide, label, ML, Cm(0.6), Cm(20), Cm(0.8),
        SANS, 9, color=GRAY)


def tbl(slide, data, x, y, w, h,
        hdr_bg=NAVY, hdr_fg=WHITE, odd=BG, even=BOXBG,
        font_size=14, center=False):
    rows = len(data)
    cols = max(len(r) for r in data)
    t = slide.shapes.add_table(rows, cols, x, y, w, h).table
    align = PP_ALIGN.CENTER if center else PP_ALIGN.LEFT
    for ri, row in enumerate(data):
        for ci in range(cols):
            val  = row[ci] if ci < len(row) else ''
            cell = t.cell(ri, ci)
            cell.text = str(val)
            tf = cell.text_frame
            tf.word_wrap = True
            for para in tf.paragraphs:
                para.alignment = align
                for run in para.runs:
                    run.font.name  = SANS
                    run.font.size  = Pt(font_size)
                    run.font.bold  = (ri == 0)
                    run.font.color.rgb = hdr_fg if ri == 0 else BLACK
            tcPr = cell._tc.get_or_add_tcPr()
            for old in tcPr.findall(qn('a:solidFill')):
                tcPr.remove(old)
            sf  = etree.SubElement(tcPr, qn('a:solidFill'))
            clr = etree.SubElement(sf,   qn('a:srgbClr'))
            if ri == 0:
                clr.set('val', '{:02X}{:02X}{:02X}'.format(*hdr_bg))
            elif ri % 2 == 1:
                clr.set('val', '{:02X}{:02X}{:02X}'.format(*odd))
            else:
                clr.set('val', '{:02X}{:02X}{:02X}'.format(*even))
    return t


def box(slide, text, x, y, w, h,
        bg_color=BOXBG, border=NAVY,
        font=SANS, size=15, bold=False, color=BLACK,
        align=PP_ALIGN.CENTER):
    s = slide.shapes.add_shape(5, x, y, w, h)
    s.fill.solid()
    s.fill.fore_color.rgb = bg_color
    s.line.color.rgb = border
    s.line.width = Pt(1)
    tf = s.text_frame
    tf.word_wrap = True
    p  = tf.paragraphs[0]
    p.alignment = align
    r  = p.add_run()
    r.text = text
    r.font.name  = font
    r.font.size  = Pt(size)
    r.font.bold  = bold
    r.font.color.rgb = color
    return s


def section_slide(num, titulo):
    sl = prs.slides.add_slide(blank)
    bg(sl)
    hline(sl, 0, Cm(8.0), W, NAVY, Pt(0.8))
    txt(sl, num, 0, Cm(5.8), W, Cm(1.8),
        SANS, 22, color=NAVY, align=PP_ALIGN.CENTER)
    txt(sl, titulo, 0, Cm(8.3), W, Cm(6),
        SERIF, 46, bold=True, color=BLACK, align=PP_ALIGN.CENTER)
    footer(sl)
    add_logo(sl)
    return sl


# ════════════════════════════════════════════════════════
# SLIDE 1 — PORTADA
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
hline(sl, ML, Cm(1.8), CW - Cm(4.5), BLACK, Pt(2))
hline(sl, ML, Cm(17.2), CW, BLACK, Pt(2))

txt(sl, 'Fundamentos teóricos y práctica clínica',
    ML, Cm(0.7), Cm(20), Cm(0.9), SANS, 11, color=GRAY)

txt(sl, 'Análisis\nFuncional\nde la Conducta',
    ML, Cm(2.5), Cm(22), Cm(12),
    SERIF, 58, bold=True, color=BLACK)

txt(sl, 'Cómo entender el comportamiento más allá del diagnóstico',
    ML, Cm(14.8), Cm(28), Cm(1.4), SANS, 16, color=GRAY)

txt(sl, 'Presentación por Lic. Jean Clemotte',
    ML, Cm(16.3), Cm(22), Cm(1.2),
    SERIF, 15, italic=True, color=GRAY)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 2 — GANCHO: MARGE
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Marge, 39 años — Asunción, Paraguay',
    ML, Cm(2.0), CW - Cm(4), Cm(2.0),
    SERIF, 34, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

txt(sl, '"Homero convenció a Marge de ir a consulta. Ella '
       'dice que "no puede salir sola". Hace 2 años la asaltaron '
       'en el Super Stock de Villa Morra. Desde entonces evita ir '
       'sola a cualquier lugar concurrido. Le dijeron: trastorno '
       'de pánico con agorafobia."',
    ML, Cm(4.5), Cm(17), Cm(6.5),
    SANS, 17, italic=True, color=BLACK)

txt(sl, '¿Eso explica por qué\nMarge no puede\nir al supermercado?',
    Cm(21), Cm(3.8), Cm(11), Cm(5),
    SERIF, 22, color=NAVY, align=PP_ALIGN.CENTER)

txt(sl, 'No.\nSolo le pone nombre.',
    Cm(21), Cm(9.5), Cm(11), Cm(3.5),
    SERIF, 30, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

txt(sl, 'Vamos a aprender a responder la pregunta real.',
    ML, Cm(13.5), CW - Cm(1), Cm(1.5),
    SANS, 18, italic=True, color=GRAY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 3 — ÍNDICE
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, '¿Qué vamos\na ver?',
    ML, Cm(2.2), Cm(10), Cm(5),
    SERIF, 38, bold=True, color=BLACK)

bloques = [
    ('01', 'Fundamentos del AF',
     'Qué es y para qué sirve  •  4 supuestos  •  Funcionalidad vs Morfología'),
    ('02', 'Las leyes del aprendizaje',
     'Habituación  •  Condicionamiento clásico  •  Operante  •  Ed  •  Variables'),
    ('03', 'El procedimiento paso a paso',
     'Describir la conducta  •  Antecedentes y consecuentes  •  Hipótesis funcional'),
]
for i, (num, titulo, items) in enumerate(bloques):
    y = Cm(2.8) + i * Cm(4.3)
    txt(sl, num, Cm(12.5), y, Cm(2.5), Cm(1.5),
        SERIF, 22, bold=True, color=NAVY)
    txt(sl, titulo, Cm(15.2), y, Cm(16.5), Cm(1.3),
        SANS, 18, bold=True, color=BLACK)
    txt(sl, items, Cm(15.2), y + Cm(1.5), Cm(16.5), Cm(2.5),
        SANS, 14, color=GRAY)
    if i < 2:
        hline(sl, Cm(12.5), y + Cm(4.0), Cm(19.5), LGRAY)

txt(sl, 'Caso guía: Marge Simpson  —  "¿agorafobia"... o algo más?',
    ML, Cm(15.8), CW - Cm(1), Cm(1.2),
    SANS, 14, italic=True, color=GRAY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 4 — PORTADA BLOQUE 1
# ════════════════════════════════════════════════════════
section_slide('Bloque 01', '¿Qué es el\nAnálisis Funcional?')


# ════════════════════════════════════════════════════════
# SLIDE 5 — DIAGNÓSTICO VS AF
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'El diagnóstico describe. El AF explica.',
    ML, Cm(2.0), CW - Cm(4), Cm(2.0),
    SERIF, 32, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

data5 = [
    ['Diagnóstico', 'El Análisis Funcional pregunta...'],
    ['"Trastorno de pánico"',  '¿Qué hace Marge exactamente?'],
    ['"Depresión mayor"',      '¿Cuándo ocurre? ¿Cuándo NO ocurre?'],
    ['"Fobia social"',         '¿Qué pasa después de que lo hace?'],
]
tbl(sl, data5, ML, Cm(4.5), CW - Cm(1), Cm(8.5), font_size=16)

txt(sl, 'El AF busca relaciones entre la conducta y su contexto.',
    ML, Cm(14.0), CW - Cm(1), Cm(1.8),
    SANS, 18, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 6 — FUNCIONALIDAD VS MORFOLOGÍA
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Lo que importa no es cómo se ve,\nsino para qué sirve.',
    ML, Cm(2.0), CW - Cm(4), Cm(3.2),
    SERIF, 30, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

txt(sl, 'Bart quiere evitar ir a la escuela...',
    ML, Cm(5.5), CW, Cm(1.2),
    SANS, 18, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

behaviors = ['Dice que\nle duele\nla panza', 'Esconde\nla mochila', 'Hace una\nrabieta',
             'Llora', 'Pierde\nel cuaderno']
bw = CW / 5 - Cm(0.4)
for i, b in enumerate(behaviors):
    box(sl, b, ML + i * (bw + Cm(0.4)), Cm(7.2), bw, Cm(3.0),
        bg_color=BOXBG, border=NAVY, size=15, align=PP_ALIGN.CENTER)

txt(sl, '5 morfologías distintas   →   1 función: escapar de la escuela',
    ML, Cm(11.2), CW - Cm(1), Cm(1.5),
    SERIF, 22, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

txt(sl, '"El AF no pregunta cómo se ve la conducta, sino qué función cumple en ese contexto."',
    ML, Cm(13.2), CW - Cm(1), Cm(2.0),
    SANS, 17, italic=True, color=GRAY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 7 — 4 SUPUESTOS
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Antes de empezar: 4 supuestos',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 32, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

supuestos = [
    ('01', 'Analiza CUALQUIER conducta',
     'Incluyendo pensamientos,\nemociones y conductas encubiertas'),
    ('02', 'Las conductas son ADAPTATIVAS',
     'A corto plazo. El problema es\nque dejan de funcionar a largo plazo'),
    ('03', 'Las leyes son UNIVERSALES',
     'Aplican igual en Paraguay, España\no cualquier parte del mundo'),
    ('04', 'Considera MUCHAS variables',
     'Biológicas, psicológicas,\nhistóricas y contextuales'),
]
hw = CW / 2 - Cm(0.6)
for i, (num, titulo, desc) in enumerate(supuestos):
    col = i % 2
    row = i // 2
    x = ML + col * (hw + Cm(0.8))
    y = Cm(4.5) + row * Cm(5.8)
    s = slide_s = prs.slides[-1].shapes.add_shape(1, x, y, hw, Cm(5.3))
    s.fill.solid()
    s.fill.fore_color.rgb = BOXBG
    s.line.color.rgb = NAVY
    s.line.width = Pt(1)
    txt(sl, num,    x + Cm(0.5), y + Cm(0.4), Cm(2), Cm(1.2),
        SERIF, 22, bold=True, color=NAVY)
    txt(sl, titulo, x + Cm(0.5), y + Cm(1.7), hw - Cm(1.0), Cm(1.4),
        SANS, 15, bold=True, color=BLACK)
    txt(sl, desc,   x + Cm(0.5), y + Cm(3.2), hw - Cm(1.0), Cm(2.0),
        SANS, 14, color=GRAY)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 8 — PORTADA BLOQUE 2
# ════════════════════════════════════════════════════════
section_slide('Bloque 02', 'Las leyes\ndel aprendizaje')


# ════════════════════════════════════════════════════════
# SLIDE 9 — HABITUACIÓN Y SENSIBILIZACIÓN
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Habituación y Sensibilización',
    ML, Cm(2.0), CW - Cm(4), Cm(2.0),
    SERIF, 32, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

hw9 = CW / 2 - Cm(0.8)
box(sl, 'HABITUACIÓN', ML, Cm(4.5), hw9, Cm(1.5),
    bg_color=NAVY, border=NAVY, font=SANS, size=17, bold=True, color=WHITE)
paras(sl, [
    {'t': 'La respuesta BAJA con la exposición repetida', 'bold': True, 'size': 17},
    {'t': '→ El estímulo pierde fuerza', 'size': 15, 'color': GRAY},
    {'t': ' ', 'size': 8},
    {'t': 'Ej: Dejar de escuchar el ruido del aire\nacondicionado de la oficina', 'size': 16, 'italic': True},
    {'t': 'Ej: Dejar de notar el olor a tereré\nen la sala de espera', 'size': 16, 'italic': True},
], ML, Cm(6.3), hw9, Cm(9), SANS, 16, BLACK)

col2 = ML + hw9 + Cm(0.8)
box(sl, 'SENSIBILIZACIÓN', col2, Cm(4.5), hw9, Cm(1.5),
    bg_color=BLUE, border=BLUE, font=SANS, size=17, bold=True, color=WHITE)
paras(sl, [
    {'t': 'La respuesta SUBE con la exposición repetida', 'bold': True, 'size': 17},
    {'t': '→ El estímulo gana fuerza', 'size': 15, 'color': GRAY},
    {'t': ' ', 'size': 8},
    {'t': 'Ej: Los golpecitos en el hombro que\nse sienten cada vez más fuertes', 'size': 16, 'italic': True},
    {'t': 'Ej: Un ruido que parece cada vez\nmás intenso', 'size': 16, 'italic': True},
], col2, Cm(6.3), hw9, Cm(9), SANS, 16, BLACK)

txt(sl, '⚠  Habituación ≠ "acostumbrarse"  (eso es condicionamiento operante)',
    ML, Cm(15.5), CW - Cm(1), Cm(1.3),
    SANS, 15, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 10 — CONDICIONAMIENTO CLÁSICO (CORREGIDO)
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Condicionamiento Clásico: aprender a reaccionar',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 28, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

# Nota al margen sobre el EI correcto
txt(sl, 'EI = estímulo biológicamente\namenazante (no el pánico —\nese es la RI)',
    W - Cm(8), Cm(3.8), Cm(6), Cm(3.5),
    SANS, 12, italic=True, color=GRAY, align=PP_ALIGN.CENTER)

data10 = [
    ['Momento', 'Estímulo', '', 'Respuesta'],
    ['ANTES', 'Super Stock (neutro)', '→', 'Sin respuesta de ansiedad'],
    ['', 'Asalto en el Super Stock (EI)', '→', 'Miedo + taquicardia (RI)'],
    ['DURANTE', 'Super Stock + Asalto (EI)', '→', 'Miedo + taquicardia (RI)'],
    ['', '[Una sola vez — experiencia muy intensa]', '', ''],
    ['DESPUÉS', 'Super Stock (EC)', '→', 'Miedo + taquicardia (RC)'],
    ['', '↓ generalización: cualquier supermercado (EC)', '→', 'Miedo (RC)'],
]
tbl(sl, data10, ML, Cm(4.0), Cm(23), Cm(11.5), font_size=14)

txt(sl, 'Las conductas respondientes ocurren POR algo — son reacciones. No dependen de lo que haga el organismo después.',
    ML, Cm(16.2), CW - Cm(1), Cm(1.5),
    SANS, 15, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 11 — TRIPLE CONTINGENCIA
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Triple Contingencia',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 34, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

bw = Cm(9.0)
bh = Cm(7.0)
by = Cm(4.2)
gap = Cm(1.0)

box(sl, 'ANTECEDENTE\n(Señal)\n\nHomero dice:\n"¿Vamos al\nSuper Stock?"\n\n(Ed)',
    ML, by, bw, bh,
    bg_color=BOXBG, border=NAVY, size=16)

txt(sl, '▶', ML + bw + Cm(0.1), by + bh/2 - Cm(0.6), gap, Cm(1.4),
    SANS, 26, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

box(sl, 'RESPUESTA\n(Lo que hace)\n\n"Me duele\nla cabeza,\nno puedo ir."\n\n(Operante)',
    ML + bw + gap, by, bw, bh,
    bg_color=BOXBG, border=NAVY, size=16)

txt(sl, '▶', ML + bw*2 + gap + Cm(0.1), by + bh/2 - Cm(0.6), gap, Cm(1.4),
    SANS, 26, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

box(sl, 'CONSECUENTE\n(Lo que pasa)\n\nHomero va solo.\nMarge en casa.\nDesaparece\nla ansiedad.\n(Reforzador −)',
    ML + bw*2 + gap*2, by, bw, bh,
    bg_color=BOXBG, border=NAVY, size=16)

txt(sl, 'Las conductas operantes ocurren PARA algo — la historia de consecuencias determina si se repiten.',
    ML, Cm(12.5), CW - Cm(1), Cm(1.5),
    SANS, 16, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 12 — ESTÍMULO DISCRIMINATIVO (Ed) — NUEVO
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Antecedente vs Estímulo Discriminativo',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 30, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

hw12 = CW / 2 - Cm(0.7)
# Left: Antecedente
box(sl, 'ANTECEDENTE', ML, Cm(4.3), hw12, Cm(1.3),
    bg_color=BOXBG, border=NAVY, font=SANS, size=17, bold=True, color=BLACK)
paras(sl, [
    {'t': 'Concepto DESCRIPTIVO', 'bold': True, 'size': 16, 'color': NAVY},
    {'t': ' ', 'size': 6},
    'Solo indica una relación temporal:',
    'el estímulo está ANTES de la conducta.',
    ' ',
    {'t': 'No dice nada sobre si hay reforzador\ndisponible o no.', 'size': 15, 'color': GRAY},
], ML, Cm(5.9), hw12, Cm(8), SANS, 15, BLACK)

col2 = ML + hw12 + Cm(0.8)
# Right: Ed
box(sl, 'ESTÍMULO DISCRIMINATIVO  (Ed)', col2, Cm(4.3), hw12, Cm(1.3),
    bg_color=NAVY, border=NAVY, font=SANS, size=15, bold=True, color=WHITE)
paras(sl, [
    {'t': 'Concepto FUNCIONAL', 'bold': True, 'size': 16, 'color': NAVY},
    {'t': ' ', 'size': 6},
    'Señala que si emito esta respuesta,',
    'hay probabilidad de obtener ese reforzador.',
    ' ',
    {'t': 'Ed+: señala que el reforzador está disponible\n"Homero de buen humor" → pedir permiso', 'size': 14, 'italic': True},
    {'t': ' ', 'size': 4},
    {'t': 'Ed−: señala castigo o extinción\n"Homero de mal humor" → mejor no pedir nada', 'size': 14, 'italic': True},
], col2, Cm(5.9), hw12, Cm(10), SANS, 15, BLACK)

txt(sl, 'No todo lo que ocurre antes es un Ed.  El Ed se establece por la historia de aprendizaje.',
    ML, Cm(15.8), CW - Cm(1), Cm(1.3),
    SANS, 16, bold=True, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 13 — 4 PROCEDIMIENTOS OPERANTES
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, '4 procedimientos operantes básicos',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 32, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

data13 = [
    ['', 'APARECE algo después de la R', 'DESAPARECE algo después de la R'],
    ['La R\nSUBE',
     'Reforzamiento POSITIVO\n\nBart saca buena nota →\nmamá lo elogia →\nsigue estudiando',
     'Reforzamiento NEGATIVO\n\nMarge evita el Super Stock →\ndesaparece el miedo →\nsigue evitando'],
    ['La R\nBAJA',
     'Castigo POSITIVO\n\nBart hace una broma →\nHomero le grita →\ndeja de hacerlas',
     'Castigo NEGATIVO\n\nBart llega tarde →\nle quitan el skate →\nllega a horario'],
]
tbl(sl, data13, ML, Cm(4.2), CW - Cm(1), Cm(11.5),
    font_size=15, center=True)

txt(sl, '⚠  Positivo / Negativo = aparece / desaparece.  No significa bueno / malo.',
    ML, Cm(16.5), CW - Cm(1), Cm(1.2),
    SANS, 15, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 14 — VARIABLES: EXPLICACIÓN
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Variables que alteran la contingencia',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 32, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

hw14 = CW / 2 - Cm(0.7)
box(sl, 'DISPOSICIONALES\n(condiciones estables)',
    ML, Cm(4.3), hw14, Cm(1.5),
    bg_color=NAVY, border=NAVY, font=SANS, size=16, bold=True, color=WHITE)
paras(sl, [
    '• Biológicas: edad, enfermedades, medicación',
    '• Historia de aprendizaje',
    '• Repertorio conductual (habilidades/déficits)',
    '• Reglas internas  ("si hago X, pasa Y")',
    '• Condiciones del entorno físico y social',
], ML, Cm(6.1), hw14, Cm(8.5), SANS, 17, BLACK)

col2 = ML + hw14 + Cm(0.8)
box(sl, 'MOTIVADORAS\n(cambian en el momento)',
    col2, Cm(4.3), hw14, Cm(1.5),
    bg_color=BLUE, border=BLUE, font=SANS, size=16, bold=True, color=WHITE)
paras(sl, [
    '• Privación / saciación',
    '• Estado emocional actual',
    '• Anticipaciones verbales',
    '• Cambios en el contexto inmediato',
], col2, Cm(6.1), hw14, Cm(7), SANS, 17, BLACK)

txt(sl, 'No causan la conducta.  Modifican la PROBABILIDAD de que ocurra.',
    ML, Cm(15.5), CW - Cm(1), Cm(1.5),
    SANS, 17, bold=True, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 15 — EJEMPLOS DISPOSICIONALES Y MOTIVACIONALES (NUEVO)
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Ejemplos contextualizados (Paraguay)',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 30, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

data15 = [
    ['Variable', 'Tipo', 'Efecto sobre la conducta de Marge'],
    ['Asalto previo en el Super Stock',
     'Disposicional\n(historia de aprendizaje)',
     'El Super Stock adquirió función de EC aversivo.\nAumenta la probabilidad de evitación.'],
    ['Regla: "Si salgo sola, me van a asaltar de nuevo"',
     'Disposicional\n(regla de conducta)',
     'Amplifica el valor del Ed. Aumenta la taquicardia\nante cualquier supermercado.'],
    ['Estrés del hogar: Bart suspendió, Homero\nes despistado, Maggie no duerme bien',
     'Motivadora\n(estado emocional)',
     'Aumenta la activación general. Cualquier\nestímulo produce más ansiedad.'],
    ['Homero siempre va solo al Super Stock\nsi Marge no puede ir',
     'Motivadora\n(operación de abolición)',
     'Reduce la presión por salir. Refuerza la\nconducta de evitación por partida doble.'],
]
tbl(sl, data15, ML, Cm(4.2), CW - Cm(1), Cm(11.5), font_size=13)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 16 — PORTADA BLOQUE 3
# ════════════════════════════════════════════════════════
section_slide('Bloque 03', 'El procedimiento\npaso a paso')


# ════════════════════════════════════════════════════════
# SLIDE 17 — PASO 1: DESCRIBIR LA CONDUCTA
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Paso 1 — ¿Qué hace exactamente?',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 32, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

dims = [
    ('01', 'Frecuencia', '¿Cuántas veces\nocurre?'),
    ('02', 'Duración', '¿Cuánto\ntiempo dura?'),
    ('03', 'Localización', '¿Cuándo?\n¿Dónde?\n¿Con quién?'),
]
bw17 = CW / 3 - Cm(0.5)
for i, (num, nombre, preg) in enumerate(dims):
    x = ML + i * (bw17 + Cm(0.5))
    box(sl, f'{num}\n{nombre}\n\n{preg}',
        x, Cm(4.5), bw17, Cm(4.5),
        bg_color=BOXBG, border=NAVY, size=17)

txt(sl, '❌  "Marge tiene ansiedad"',
    ML, Cm(10.0), CW - Cm(1), Cm(1.3),
    SANS, 18, bold=True, color=RED, align=PP_ALIGN.CENTER)

txt(sl, '✓  "Marge evita supermercados, shoppings y reuniones sociales desde hace 2 años.\n'
       '   Ocurre en cualquier lugar concurrido de Asunción donde no esté Homero presente."',
    ML, Cm(11.5), CW - Cm(1), Cm(3.0),
    SANS, 17, color=GREEN)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 18 — PASO 2: ANTECEDENTES Y CONSECUENTES
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Paso 2 — ¿Qué pasa antes y después?',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 30, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

bw18 = Cm(9.5)
bh18 = Cm(7.0)
by18 = Cm(4.3)
gap18 = Cm(1.3)

box(sl, 'ANTES\n(Antecedentes)\n\n¿Dónde está?\n¿Con quién?\n¿Qué piensa?\n¿Qué siente\nfísicamente?',
    ML, by18, bw18, bh18,
    bg_color=BOXBG, border=NAVY, size=16)

txt(sl, '▶', ML + bw18 + Cm(0.1), by18 + bh18/2 - Cm(0.7), gap18, Cm(1.5),
    SANS, 26, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

box(sl, 'CONDUCTA',
    ML + bw18 + gap18, by18 + bh18/2 - Cm(1.2), Cm(6.5), Cm(2.5),
    bg_color=NAVY, border=NAVY, font=SANS, size=18, bold=True, color=WHITE)

txt(sl, '▶', ML + bw18*2 + gap18 + Cm(0.3), by18 + bh18/2 - Cm(0.7), gap18, Cm(1.5),
    SANS, 26, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

box(sl, 'DESPUÉS\n(Consecuentes)\n\n¿Qué obtiene?\n¿Qué evita?\n¿Cómo se siente?\n¿Qué hacen\nlos otros?',
    ML + bw18*2 + gap18*2 - Cm(0.2), by18, bw18, bh18,
    bg_color=BOXBG, border=NAVY, size=16)

txt(sl, '⚠  No todo lo que ocurre antes/después tiene relación funcional con la conducta.',
    ML, Cm(12.8), CW - Cm(1), Cm(1.3),
    SANS, 15, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 19 — E-R VS E-R-C
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, '¿La conducta ocurre POR algo o PARA algo?',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 30, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

data19 = [
    ['E-R  (Respondiente / Clásica)', 'E-R-C  (Operante)'],
    ['Es una REACCIÓN ante el ambiente', 'Es una ACCIÓN sobre el ambiente'],
    ['No depende de las consecuencias', 'Las consecuencias la moldean'],
    ['Es automática — no se puede evitar', 'El sujeto puede modificarla'],
    ['Ej: taquicardia ante el Super Stock', 'Ej: decir "no puedo ir" y quedarse'],
    ['Ocurre POR el estímulo antecedente', 'Ocurre PARA obtener algo'],
]
tbl(sl, data19, ML, Cm(4.3), CW - Cm(1), Cm(10.0),
    font_size=16, center=True)

txt(sl, 'En clínica, casi siempre aparecen las dos juntas.\n'
       'Marge tiene taquicardia (E-R)   y   evita el supermercado (E-R-C).',
    ML, Cm(15.2), CW - Cm(1), Cm(2.2),
    SANS, 16, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 20 — PASO 3: VARIABLES DISPOSICIONALES
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Paso 3 — ¿Qué facilita o dificulta que ocurra?',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 28, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

cuadros = [
    ('Biológicas', '¿Toma medicación?\n¿Tiene enfermedades?\n¿Duerme bien?'),
    ('Historia de aprendizaje', '¿Cuándo empezó?\n¿Qué pasó en ese momento?\n¿Hubo experiencias similares?'),
    ('Reglas', '¿Qué se dice a sí mismo?\n"Si salgo, me van a asaltar"\n"No puedo controlar mi ansiedad"'),
    ('Contexto', '¿Cuándo ocurre más?\n¿Cuándo NO ocurre?\n¿Qué personas o lugares influyen?'),
]
hw20 = CW / 2 - Cm(0.6)
for i, (titulo, contenido) in enumerate(cuadros):
    col = i % 2
    row = i // 2
    x = ML + col * (hw20 + Cm(0.8))
    y = Cm(4.3) + row * Cm(5.5)
    txt(sl, titulo, x, y, hw20, Cm(1.2),
        SANS, 17, bold=True, color=NAVY)
    hline(sl, x, y + Cm(1.2), hw20, NAVY)
    txt(sl, contenido, x, y + Cm(1.5), hw20, Cm(4.0),
        SANS, 16, color=BLACK)

txt(sl, 'No listar por listar — especificar CÓMO cada variable afecta a la contingencia.',
    ML, Cm(16.5), CW - Cm(1), Cm(1.2),
    SANS, 15, italic=True, color=GRAY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 21 — HIPÓTESIS FUNCIONAL
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'La hipótesis funcional: origen vs mantenimiento',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 28, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

hw21 = CW / 2 - Cm(0.7)
box(sl, 'Hipótesis de ORIGEN',
    ML, Cm(4.3), hw21, Cm(1.3),
    bg_color=BOXBG, border=NAVY, font=SANS, size=17, bold=True, color=BLACK)
paras(sl, [
    '¿Cómo se aprendió esta conducta?',
    ' ',
    {'t': '→ Puede ser desconocida', 'size': 15, 'color': GRAY},
    {'t': '→ No siempre necesaria para el tratamiento', 'size': 15, 'color': GRAY},
    {'t': '→ Útil para entender al paciente', 'size': 15, 'color': GRAY},
    ' ',
    {'t': '"Marge fue asaltada en el Super Stock.\nDesde ese día empezó a evitar salir."',
     'italic': True, 'size': 15},
], ML, Cm(5.9), hw21, Cm(10.5), SANS, 15, BLACK)

col21 = ML + hw21 + Cm(0.8)
box(sl, 'Hipótesis de MANTENIMIENTO',
    col21, Cm(4.3), hw21, Cm(1.3),
    bg_color=NAVY, border=NAVY, font=SANS, size=17, bold=True, color=WHITE)
paras(sl, [
    '¿Qué la sostiene HOY?',
    ' ',
    {'t': '→ Esta es la que guía el tratamiento', 'size': 15, 'bold': True},
    {'t': '→ Se establece desde las contingencias actuales', 'size': 15},
    ' ',
    {'t': '"La evitación reduce la taquicardia (RN). Homero resuelve las compras (RN adicional). La regla "me van a asaltar" amplifica la respuesta."',
     'italic': True, 'size': 15},
], col21, Cm(5.9), hw21, Cm(10.5), SANS, 15, BLACK)

txt(sl, 'El pasado no CAUSA la conducta actual.  La sostienen las contingencias PRESENTES.',
    ML, Cm(16.5), CW - Cm(1), Cm(1.2),
    SANS, 16, bold=True, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 22 — CIERRE DEL CASO MARGE
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Marge: del diagnóstico al análisis funcional',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 28, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

data22 = [
    ['Componente', 'Marge Simpson — Asunción, Paraguay'],
    ['Conducta (R)',
     'Evitar supermercados, shoppings y lugares concurridos sin compañía'],
    ['Antecedente (Ed)',
     'Homero dice "¿vamos al Super Stock?" / pensar en salir sola'],
    ['Consecuente (C)',
     'Homero va solo → Marge se queda → desaparece la ansiedad  (RN)'],
    ['Resp. condicionada',
     'Taquicardia + ahogo ante cualquier lugar concurrido  (E-R, CC)'],
    ['Variable disposicional',
     'Regla: "Si salgo sola, me van a asaltar de nuevo"'],
    ['Variable motivadora',
     'Estrés del hogar: Bart + Homero + Maggie potencia la respuesta'],
]
tbl(sl, data22, ML, Cm(4.2), CW - Cm(1), Cm(10.5), font_size=14)

txt(sl, 'La evitación se mantiene por DOS razones: produce alivio + Homero resuelve por ella.\n'
       'El tratamiento debe atacar ambas contingencias.',
    ML, Cm(15.5), CW - Cm(1), Cm(2.0),
    SANS, 16, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 23 — IDEAS CLAVE
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
dividers(sl)
top_label(sl)

txt(sl, 'Para llevarse hoy',
    ML, Cm(2.0), CW - Cm(4), Cm(1.8),
    SERIF, 36, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

ideas = [
    ('01', 'Lo que importa no es cómo se ve la conducta (morfología),\nsino para qué sirve en ese contexto (función).'),
    ('02', 'Las conductas se mantienen porque obtienen consecuencias.\nIdentificar cuáles es la tarea del psicólogo.'),
    ('03', 'El AF no es un diagnóstico.\nEs una hipótesis explicativa que guía la intervención.'),
]
for i, (num, texto) in enumerate(ideas):
    y = Cm(4.8) + i * Cm(4.0)
    txt(sl, num, ML, y, Cm(2.8), Cm(1.8),
        SERIF, 28, bold=True, color=NAVY)
    hline(sl, ML + Cm(3.2), y + Cm(1.0), CW - Cm(7.2), LGRAY)
    txt(sl, texto, ML + Cm(3.2), y, CW - Cm(7.5), Cm(3.8),
        SANS, 19, color=BLACK)

footer(sl)
add_logo(sl)


# ════════════════════════════════════════════════════════
# SLIDE 24 — CIERRE CON FOTO DE JEAN
# ════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)

# Foto como fondo completo
sl.shapes.add_picture(PHOTO, 0, 0, W, H)

# Overlay semitransparente izquierda (para texto legible)
overlay = sl.shapes.add_shape(1, 0, 0, W * 0.52, H)
overlay.fill.solid()
overlay.fill.fore_color.rgb = RGBColor(0xF0, 0xEB, 0xE0)
overlay.line.fill.background()
# Transparencia via XML
xPr  = overlay.fill._xPr
sf   = xPr.solidFill
clr  = sf.find(qn('a:srgbClr'))
if clr is None:
    clr = etree.SubElement(sf, qn('a:srgbClr'))
    clr.set('val', 'F0EBE0')
alpha = etree.SubElement(clr, qn('a:alpha'))
alpha.set('val', '82000')   # ~82% opaco

hline(sl, ML, Cm(1.6), Cm(16), BLACK, Pt(2))
hline(sl, ML, Cm(17.0), CW, BLACK, Pt(2))

txt(sl, '@PSICO_EDUCA20',
    ML, Cm(0.5), Cm(16), Cm(0.9),
    SANS, 12, color=GRAY)

txt(sl, 'Gracias por\nsu Atención',
    ML, Cm(4.0), Cm(16), Cm(6.5),
    SERIF, 52, bold=True, italic=True, color=BLACK)

txt(sl, 'Análisis Funcional de la Conducta\nFundamentos y práctica clínica',
    ML, Cm(11.5), Cm(16), Cm(3.0),
    SANS, 17, color=GRAY)

txt(sl, 'Lic. Jean Clemotte  |  PsicoEduca',
    ML, Cm(15.0), Cm(16), Cm(1.3),
    SANS, 15, italic=True, color=NAVY)

add_logo(sl)


# ════════════════════════════════════════════════════════
# GUARDAR
# ════════════════════════════════════════════════════════
output = r'C:\Users\MI PC\psicoeduca\materiales\presentacion-AF.pptx'
prs.save(output)
print('Listo: ' + output)
print('24 slides | v2 con todas las correcciones')
