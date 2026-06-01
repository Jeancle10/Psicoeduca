"""
Presentacion: Bases filosoficas del Analisis de la Conducta
Fuente: Cap 3 - Frojan et al. "Cuestiones filosoficas en torno al AC"
Audiencia: Psicologos recien egresados sin base en AF ni conductismo
Caso guia: Homero Simpson
"""
from pptx import Presentation
from pptx.util import Cm, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from lxml import etree
from pptx.oxml.ns import qn

BG    = RGBColor(0xE8, 0xE3, 0xD8)
NAVY  = RGBColor(0x1B, 0x3A, 0x5C)
BLACK = RGBColor(0x1A, 0x1A, 0x1A)
GRAY  = RGBColor(0x66, 0x66, 0x66)
LGRAY = RGBColor(0xCC, 0xC8, 0xC0)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BLUE  = RGBColor(0x2E, 0x76, 0xA0)
BOXBG = RGBColor(0xD8, 0xD2, 0xC5)
RED   = RGBColor(0xCC, 0x33, 0x33)
GREEN = RGBColor(0x22, 0x77, 0x44)

SERIF = 'Georgia'
SANS  = 'Calibri'

W  = Cm(33.87)
H  = Cm(19.05)
ML = Cm(1.8)
CW = Cm(30.27)

LOGO  = r'C:\Users\MI PC\Desktop\PsicoEduca\Marketing\PsicoEduca Logo final_Mesa de trabajo 1 copia 4.png'
PHOTO = r'C:\Users\MI PC\Desktop\PsicoEduca\Marketing\BOOK\sentado.JPG'

prs = Presentation()
prs.slide_width  = W
prs.slide_height = H
blank = prs.slide_layouts[6]

# ── HELPERS ─────────────────────────────────────────────

def bg(slide, color=BG):
    f = slide.background.fill; f.solid(); f.fore_color.rgb = color

def hline(slide, x, y, w, color=BLACK, thick=Pt(1.5)):
    s = slide.shapes.add_shape(1, x, y, w, thick)
    s.fill.solid(); s.fill.fore_color.rgb = color; s.line.fill.background()

def txt(slide, text, x, y, w, h,
        font=SANS, size=16, bold=False, italic=False,
        color=BLACK, align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = align
    r = p.add_run(); r.text = text
    r.font.name=font; r.font.size=Pt(size)
    r.font.bold=bold; r.font.italic=italic; r.font.color.rgb=color
    return tb

def paras(slide, lines, x, y, w, h,
          font=SANS, size=15, color=BLACK, align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = True
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.alignment = align
        if isinstance(ln, dict):
            r = p.add_run()
            r.text=ln.get('t',''); r.font.name=ln.get('font',font)
            r.font.size=Pt(ln.get('size',size)); r.font.bold=ln.get('bold',False)
            r.font.italic=ln.get('italic',False); r.font.color.rgb=ln.get('color',color)
        else:
            r = p.add_run(); r.text=str(ln)
            r.font.name=font; r.font.size=Pt(size); r.font.color.rgb=color

def add_logo(slide):
    slide.shapes.add_picture(LOGO, W-Cm(4.2), Cm(0.2), Cm(3.8), Cm(3.0))

def footer(slide):
    txt(slide,'Lic. Jean Clemotte  |  @Psico_Educa20',
        ML, H-Cm(1.2), Cm(22), Cm(0.9), SANS, 11, italic=True, color=GRAY)

def dividers(slide):
    hline(slide, ML, Cm(1.5), CW-Cm(4.5))
    hline(slide, ML, Cm(1.8), CW-Cm(4.5))
    hline(slide, ML, H-Cm(1.6), CW)
    hline(slide, ML, H-Cm(1.3), CW)

def label(slide, t='BASES FILOSÓFICAS DEL ANÁLISIS DE LA CONDUCTA'):
    txt(slide, t, ML, Cm(0.6), Cm(20), Cm(0.8), SANS, 9, color=GRAY)

def tbl(slide, data, x, y, w, h,
        hdr_bg=NAVY, hdr_fg=WHITE, odd=BG, even=BOXBG, fs=13, center=False):
    rows=len(data); cols=max(len(r) for r in data)
    t=slide.shapes.add_table(rows,cols,x,y,w,h).table
    al=PP_ALIGN.CENTER if center else PP_ALIGN.LEFT
    for ri,row in enumerate(data):
        for ci in range(cols):
            val=row[ci] if ci<len(row) else ''
            cell=t.cell(ri,ci); cell.text=str(val)
            tf=cell.text_frame; tf.word_wrap=True
            for para in tf.paragraphs:
                para.alignment=al
                for run in para.runs:
                    run.font.name=SANS; run.font.size=Pt(fs)
                    run.font.bold=(ri==0)
                    run.font.color.rgb=hdr_fg if ri==0 else BLACK
            tcPr=cell._tc.get_or_add_tcPr()
            for old in tcPr.findall(qn('a:solidFill')): tcPr.remove(old)
            sf=etree.SubElement(tcPr,qn('a:solidFill'))
            clr=etree.SubElement(sf,qn('a:srgbClr'))
            if ri==0: clr.set('val','{:02X}{:02X}{:02X}'.format(*hdr_bg))
            elif ri%2==1: clr.set('val','{:02X}{:02X}{:02X}'.format(*odd))
            else: clr.set('val','{:02X}{:02X}{:02X}'.format(*even))
    return t

def box(slide, text, x, y, w, h,
        bg_color=BOXBG, border=NAVY, font=SANS, size=15,
        bold=False, color=BLACK, align=PP_ALIGN.CENTER):
    s=slide.shapes.add_shape(5,x,y,w,h)
    s.fill.solid(); s.fill.fore_color.rgb=bg_color
    s.line.color.rgb=border; s.line.width=Pt(1)
    tf=s.text_frame; tf.word_wrap=True
    p=tf.paragraphs[0]; p.alignment=align
    r=p.add_run(); r.text=text
    r.font.name=font; r.font.size=Pt(size)
    r.font.bold=bold; r.font.color.rgb=color
    return s

def section_slide(num, titulo):
    sl=prs.slides.add_slide(blank); bg(sl)
    hline(sl, 0, Cm(8.0), W, NAVY, Pt(0.8))
    txt(sl, num, 0, Cm(5.8), W, Cm(1.8), SANS, 22, color=NAVY, align=PP_ALIGN.CENTER)
    txt(sl, titulo, 0, Cm(8.3), W, Cm(6),
        SERIF, 44, bold=True, color=BLACK, align=PP_ALIGN.CENTER)
    footer(sl); add_logo(sl)
    return sl


# ═══════════════════════════════════════════════════════
# SLIDE 1 — PORTADA
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl)
hline(sl, ML, Cm(1.8), CW-Cm(4.5), BLACK, Pt(2))
hline(sl, ML, Cm(17.2), CW, BLACK, Pt(2))

txt(sl, 'Fundamentos filosóficos | Para psicólogos en formación',
    ML, Cm(0.7), Cm(20), Cm(0.9), SANS, 11, color=GRAY)

txt(sl, '¿Puede la mente\ncausar el\ncomportamiento?',
    ML, Cm(2.5), Cm(22), Cm(11),
    SERIF, 50, bold=True, color=BLACK)

txt(sl, 'Bases filosóficas del Análisis de la Conducta',
    ML, Cm(14.5), Cm(28), Cm(1.5), SANS, 17, color=GRAY)

txt(sl, 'Presentación por Lic. Jean Clemotte',
    ML, Cm(16.2), Cm(22), Cm(1.2),
    SERIF, 15, italic=True, color=GRAY)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 2 — GANCHO: HOMERO
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, 'Homero va al psicólogo (porque Marge lo mandó)',
    ML, Cm(2.0), CW-Cm(4.5), Cm(2.0),
    SERIF, 30, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

txt(sl,
    '"El psicólogo diagnostica: Homero tiene personalidad impulsiva, '
    'baja autoestima y conducta compulsiva. Sus pensamientos negativos '
    'y su falta de voluntad causan que coma donuts y no vaya al trabajo."',
    ML, Cm(4.5), Cm(20), Cm(5.5),
    SANS, 16, italic=True, color=BLACK)

paras(sl, [
    {'t': '¿Eso explica POR QUÉ Homero come donuts?', 'size': 19, 'bold': True, 'color': NAVY},
    {'t': '¿Eso nos dice QUÉ hay que cambiar?', 'size': 19, 'bold': True, 'color': NAVY},
], Cm(21.5), Cm(4.2), Cm(10.5), Cm(5), SANS, 19, NAVY, PP_ALIGN.CENTER)

txt(sl, 'No.\nSolo le puso etiquetas.',
    Cm(21.5), Cm(10.0), Cm(10.5), Cm(4.0),
    SERIF, 28, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

txt(sl, 'Vamos a aprender por qué esas explicaciones no son científicas\ny qué propone el Análisis de la Conducta en su lugar.',
    ML, Cm(13.5), CW-Cm(1), Cm(2.2),
    SANS, 16, italic=True, color=GRAY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 3 — ÍNDICE
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, '¿Qué vamos\na ver?',
    ML, Cm(2.2), Cm(10), Cm(5),
    SERIF, 38, bold=True, color=BLACK)

bloques = [
    ('01', 'El problema mente-cuerpo',
     'Folk psychology  •  Imagen manifiesta vs científica  •  El error categorial'),
    ('02', '¿Qué significa "lo mental"?',
     'Descriptivismo  •  Reduccionismo  •  Anti-descriptivismo (Wittgenstein)  •  2 tipos de explicación'),
    ('03', 'El AF como ciencia del comportamiento',
     'Nivel agencial vs subagencial  •  Nexos temporales  •  Pensamiento y lenguaje como conducta'),
]
for i, (num, titulo, items) in enumerate(bloques):
    y = Cm(2.8) + i * Cm(4.3)
    txt(sl, num, Cm(12.5), y, Cm(2.5), Cm(1.5), SERIF, 22, bold=True, color=NAVY)
    txt(sl, titulo, Cm(15.2), y, Cm(16.5), Cm(1.3), SANS, 18, bold=True, color=BLACK)
    txt(sl, items, Cm(15.2), y+Cm(1.5), Cm(16.5), Cm(2.5), SANS, 14, color=GRAY)
    if i < 2:
        hline(sl, Cm(12.5), y+Cm(4.0), Cm(19.5), LGRAY)

txt(sl, 'Caso guía a lo largo de toda la presentación: Homero Simpson',
    ML, Cm(15.8), CW-Cm(1), Cm(1.2),
    SANS, 14, italic=True, color=GRAY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 4 — PORTADA BLOQUE 1
# ═══════════════════════════════════════════════════════
section_slide('Bloque 01', 'El problema\nmente-cuerpo')


# ═══════════════════════════════════════════════════════
# SLIDE 5 — FOLK PSYCHOLOGY
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, 'Así explicamos el comportamiento en la vida cotidiana',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 30, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

ejemplos = [
    '"Homero come donuts PORQUE le gustan y no tiene voluntad."',
    '"Lisa estudia PORQUE desea ser médica y es responsable."',
    '"Bart molesta PORQUE busca atención y es travieso."',
    '"Marge aguanta PORQUE ama a su familia y es paciente."',
]
for i, e in enumerate(ejemplos):
    y = Cm(4.5) + i * Cm(2.3)
    box(sl, e, ML, y, CW-Cm(5), Cm(2.0),
        bg_color=BOXBG, border=NAVY, size=16, align=PP_ALIGN.LEFT)

txt(sl, 'Esto es la "Folk Psychology" (Sellars, 1956):\nexplicar el comportamiento con CREENCIAS, DESEOS e INTENCIONES.',
    ML, Cm(14.8), CW-Cm(1), Cm(2.2),
    SANS, 16, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

txt(sl, '¿Son estas explicaciones CIENTÍFICAS? ¿Nos dicen las CAUSAS del comportamiento?',
    ML, Cm(17.0), CW-Cm(1), Cm(1.3),
    SANS, 15, italic=True, color=GRAY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 6 — DOS IMÁGENES DEL MUNDO
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, 'Dos formas de ver el mismo comportamiento (Sellars, 1956)',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 28, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

hw = CW/2 - Cm(0.7)
box(sl, 'IMAGEN MANIFIESTA\n(Folk Psychology)',
    ML, Cm(4.3), hw, Cm(1.4),
    bg_color=BOXBG, border=NAVY, font=SANS, size=16, bold=True, color=BLACK)
paras(sl, [
    '"Homero come donuts porque los desea y no tiene autocontrol."',
    ' ',
    'Explica el comportamiento en términos de',
    'RAZONES: creencias, deseos, intenciones.',
    ' ',
    {'t': 'Útil para evaluar si el comportamiento\nes racional o irracional.', 'color': GRAY, 'size': 14},
], ML, Cm(6.0), hw, Cm(8), SANS, 15, BLACK)

col2 = ML + hw + Cm(0.8)
box(sl, 'IMAGEN CIENTÍFICA\n(Análisis de la Conducta)',
    col2, Cm(4.3), hw, Cm(1.4),
    bg_color=NAVY, border=NAVY, font=SANS, size=16, bold=True, color=WHITE)
paras(sl, [
    '"Homero come donuts porque comer donuts fue reforzado sistemáticamente en su historia."',
    ' ',
    'Explica el comportamiento en términos de',
    'CAUSAS: contingencias, historia de aprendizaje.',
    ' ',
    {'t': 'Útil para MODIFICAR el comportamiento.', 'color': LGRAY, 'size': 14},
], col2, Cm(6.0), hw, Cm(8), SANS, 15, BLACK)

txt(sl, 'La ciencia del comportamiento necesita explicaciones CAUSALES, no solo evaluativas.',
    ML, Cm(15.5), CW-Cm(1), Cm(1.3),
    SANS, 16, bold=True, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 7 — EL ERROR CATEGORIAL (Ryle)
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, '"El fantasma en la máquina" — Gilbert Ryle (1949)',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 28, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

txt(sl, 'Descartes propuso que somos dos cosas: cuerpo (físico) + mente (inmaterial)',
    ML, Cm(4.2), CW-Cm(1), Cm(1.2), SANS, 17, bold=True, color=NAVY)

data = [
    ['El error', 'Por qué es un problema'],
    ['La mente se concibe como UNA COSA dentro del cuerpo\n(como si Homero tuviera un "motor de voluntad" dentro)',
     'La conducta no puede ser explicada por una cosa que,\npor definición, nadie puede observar ni medir directamente'],
    ['Se busca la mente en el cerebro: "la autoestima está\nen la amígdala", "el deseo en el sistema límbico"',
     'El cerebro no "desea" ni "quiere" — esos son términos\nde evaluación, no de descripción fisiológica'],
    ['"Homero tiene baja voluntad" suena a describir una\ncosa real dentro de Homero',
     'En realidad es una EVALUACIÓN de su comportamiento:\ndecimos que su conducta se desvía de una norma'],
]
tbl(sl, data, ML, Cm(5.5), CW-Cm(1), Cm(9.0), fs=13)

txt(sl, 'Concebir la mente como una "cosa" que CAUSA el comportamiento es un ERROR CATEGORIAL.',
    ML, Cm(15.3), CW-Cm(1), Cm(1.5),
    SANS, 16, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 8 — PORTADA BLOQUE 2
# ═══════════════════════════════════════════════════════
section_slide('Bloque 02', '¿Qué significa\n"lo mental"?')


# ═══════════════════════════════════════════════════════
# SLIDE 9 — DESCRIPTIVISMO Y SUS PROBLEMAS
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, 'Descriptivismo: el significado como descripción de hechos',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 28, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

txt(sl, 'Cuando decimos "Homero cree que los donuts son deliciosos", ¿a qué hecho nos referimos?',
    ML, Cm(4.2), CW-Cm(1), Cm(1.2), SANS, 17, bold=True, color=NAVY)

data = [
    ['Posición', 'Propuesta', 'Problema con Homero'],
    ['REDUCCIONISMO',
     'Lo mental = estados cerebrales.\n"Homero come donuts porque su sistema dopaminérgico responde al azúcar."',
     'Realización múltiple: la misma conducta puede ocurrir con distintos estados cerebrales. ¿Qué neurona específica es "la voluntad de Homero"?'],
    ['ELIMINATIVISMO',
     'Lo mental no existe. Hay que eliminar "autoestima", "voluntad", "deseos" del vocabulario psicológico.',
     'Perdemos la capacidad de decir que Homero actúa IRRACIONALMENTE. No podemos evaluar su comportamiento.'],
]
tbl(sl, data, ML, Cm(5.5), CW-Cm(1), Cm(9.0), fs=12)

txt(sl, 'Ambas estrategias fracasan porque lo mental NO es un hecho que se puede describir como una silla o un átomo.',
    ML, Cm(15.3), CW-Cm(1), Cm(1.5),
    SANS, 15, bold=True, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 10 — ANTI-DESCRIPTIVISMO (Wittgenstein)
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, 'Anti-descriptivismo: el significado depende del USO',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 28, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

txt(sl, 'Wittgenstein (1953): el lenguaje no sirve solo para DESCRIBIR — sirve para hacer cosas socialmente.',
    ML, Cm(4.2), CW-Cm(1), Cm(1.2), SANS, 17, bold=True, color=NAVY)

hw10 = CW/2 - Cm(0.7)
paras(sl, [
    {'t': 'Cuando decimos...', 'bold': True, 'size': 16},
    ' ',
    '"Homero cree que los donuts son deliciosos."',
    '"Homero desea comer."',
    '"Homero tiene baja autoestima."',
    ' ',
    {'t': 'No estamos describiendo un objeto mental.\nEstamos diciendo QUÉ ESPERAR de Homero.', 'size': 15, 'bold': True, 'color': NAVY},
], ML, Cm(5.8), hw10, Cm(10), SANS, 15, BLACK)

paras(sl, [
    {'t': 'El significado es NORMATIVO', 'bold': True, 'size': 18, 'color': NAVY},
    ' ',
    'Si Homero "cree que los donuts son deliciosos",',
    'esperamos que:',
    '→ Elija donuts sobre otras comidas',
    '→ Hable bien de los donuts',
    '→ Vaya al Super Stock a buscarlos',
    '→ Comparta donuts con quien quiere',
    ' ',
    {'t': 'El significado vive en el COMPORTAMIENTO ESPERADO,\nno en un objeto dentro de su cabeza.', 'size': 14, 'italic': True, 'color': GRAY},
], ML + hw10 + Cm(0.8), Cm(5.8), hw10, Cm(10), SANS, 15, BLACK)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 11 — NORMATIVAS VS NOMOLÓGICAS
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, 'Dos tipos de explicación del comportamiento',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 30, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

hw11 = CW/2 - Cm(0.7)

box(sl, 'EXPLICACIÓN NORMATIVA\n(Razones)', ML, Cm(4.3), hw11, Cm(1.4),
    bg_color=BOXBG, border=NAVY, font=SANS, size=16, bold=True, color=BLACK)
paras(sl, [
    '¿Por qué Homero no fue al trabajo?',
    ' ',
    {'t': '"Porque creyó que era feriado."', 'italic': True, 'size': 16},
    ' ',
    '→ Evalúa el comportamiento según normas.',
    '→ Nos dice si actuó racional o irracionalmente.',
    '→ NO nos explica la CAUSA física del comportamiento.',
    ' ',
    {'t': 'Usa: creencias, deseos, intenciones.', 'bold': True, 'size': 14, 'color': NAVY},
    {'t': 'Necesaria para la ética y la vida cotidiana.', 'size': 13, 'color': GRAY},
], ML, Cm(6.0), hw11, Cm(9), SANS, 15, BLACK)

col2 = ML + hw11 + Cm(0.8)
box(sl, 'EXPLICACIÓN NOMOLÓGICA\n(Causas)', col2, Cm(4.3), hw11, Cm(1.4),
    bg_color=NAVY, border=NAVY, font=SANS, size=16, bold=True, color=WHITE)
paras(sl, [
    '¿Por qué Homero no fue al trabajo?',
    ' ',
    {'t': '"Porque faltar tuvo consecuencias reforzantes en el pasado y ninguna consecuencia aversiva consistente."', 'italic': True, 'size': 15},
    ' ',
    '→ Establece las CAUSAS del comportamiento.',
    '→ Permite PREDECIR y MODIFICAR la conducta.',
    '→ No juzga si Homero es racional o irracional.',
    ' ',
    {'t': 'Usa: contingencias, historia de aprendizaje.', 'bold': True, 'size': 14, 'color': LGRAY},
    {'t': 'Necesaria para la intervención psicológica.', 'size': 13, 'color': LGRAY},
], col2, Cm(6.0), hw11, Cm(9), SANS, 15, BLACK)

txt(sl, 'La psicología clínica necesita las DOS — pero sin confundirlas.',
    ML, Cm(16.2), CW-Cm(1), Cm(1.3),
    SANS, 16, bold=True, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 12 — PORTADA BLOQUE 3
# ═══════════════════════════════════════════════════════
section_slide('Bloque 03', 'El Análisis de la Conducta\ncomo ciencia natural')


# ═══════════════════════════════════════════════════════
# SLIDE 13 — NIVEL AGENCIAL VS SUBAGENCIAL
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, '¿Desde dónde explicamos la conducta?',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 30, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

hw13 = CW/2 - Cm(0.7)
box(sl, 'NIVEL SUBAGENCIAL\n(Neurociencia)',
    ML, Cm(4.3), hw13, Cm(1.4),
    bg_color=BOXBG, border=NAVY, font=SANS, size=16, bold=True, color=BLACK)
paras(sl, [
    'Estudia lo que ocurre DENTRO del organismo.',
    '→ Neuronas, dopamina, amígdala',
    '→ Relaciones de contigüidad FÍSICA',
    ' ',
    {'t': 'Responde: ¿qué procesos biológicos están activos?', 'italic': True, 'size': 14},
    ' ',
    {'t': 'Limitaciones:', 'bold': True},
    '• No puede intervenir directamente sobre neuronas',
    '• Problema de realización múltiple',
    '• No predice mejor el comportamiento concreto',
], ML, Cm(6.0), hw13, Cm(9.5), SANS, 15, BLACK)

col2 = ML + hw13 + Cm(0.8)
box(sl, 'NIVEL AGENCIAL\n(Análisis de la Conducta)',
    col2, Cm(4.3), hw13, Cm(1.4),
    bg_color=NAVY, border=NAVY, font=SANS, size=16, bold=True, color=WHITE)
paras(sl, [
    'Estudia la INTERACCIÓN entre el organismo y su entorno.',
    '→ Contingencias, historia de aprendizaje',
    '→ Relaciones de contigüidad TEMPORAL',
    ' ',
    {'t': 'Responde: ¿qué relaciones causales mantienen la conducta?', 'italic': True, 'size': 14, 'color': LGRAY},
    ' ',
    {'t': 'Ventajas:', 'bold': True, 'color': LGRAY},
    {'t': '• Intervención directa sobre contingencias', 'color': LGRAY},
    {'t': '• Predicción precisa del comportamiento', 'color': LGRAY},
    {'t': '• Base de las técnicas terapéuticas efectivas', 'color': LGRAY},
], col2, Cm(6.0), hw13, Cm(9.5), SANS, 15, BLACK)

txt(sl, 'Ambos niveles son válidos y COMPLEMENTARIOS — pero no reducibles entre sí.',
    ML, Cm(16.5), CW-Cm(1), Cm(1.2),
    SANS, 16, bold=True, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 14 — ¿PUEDE LA NEUROCIENCIA EXPLICAR LA CONDUCTA?
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, '¿Puede la neurociencia explicar por qué Homero come donuts?',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 26, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

data14 = [
    ['Criterio', 'Neurociencia', 'Análisis de la Conducta'],
    ['¿Explica la misma conducta en distintas personas?',
     'Difícil: realización múltiple — distintas neuronas pueden producir la misma conducta',
     'Sí: las leyes del aprendizaje operan igual en todos los organismos'],
    ['¿Permite intervención efectiva?',
     'Limitado: no podemos manipular neuronas individuales en el consultorio',
     'Sí: podemos modificar antecedentes y consecuentes directamente'],
    ['¿Predice el comportamiento futuro?',
     'Parcialmente: correlaciones estadísticas, no predicciones individuales precisas',
     'Sí: si sabemos la historia de reforzamiento, predecimos la conducta futura'],
    ['¿Explica por qué Homero come donuts?',
     '"Su sistema dopaminérgico responde al azúcar." ¿Pero por qué no para? ¿Por qué en el trabajo no?',
     '"Comer donuts fue reforzado en contextos específicos. El trabajo es un Ed− activo."'],
]
tbl(sl, data14, ML, Cm(4.2), CW-Cm(1), Cm(11.0), fs=12)

txt(sl, 'La neurociencia describe el SUSTRATO — el AF explica la FUNCIÓN. Los dos son necesarios pero distintos.',
    ML, Cm(16.0), CW-Cm(1), Cm(1.5),
    SANS, 15, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 15 — NEXOS TEMPORALES: EL AF COMO DARWIN
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, 'El AF es la "selección natural" del comportamiento individual',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 28, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

txt(sl, 'Darwin: el ambiente selecciona los rasgos por sus CONSECUENCIAS a lo largo de la historia de la especie.',
    ML, Cm(4.2), CW-Cm(1), Cm(1.3), SANS, 17, bold=True, color=NAVY)

bw15 = CW/2 - Cm(0.7)
box(sl, 'SELECCIÓN NATURAL\n(evolución de la especie)',
    ML, Cm(5.8), bw15, Cm(1.3),
    bg_color=BOXBG, border=NAVY, font=SANS, size=15, bold=True, color=BLACK)
paras(sl, [
    'Los organismos con rasgos adaptativos SOBREVIVEN.',
    'El ambiente "selecciona" con sus consecuencias.',
    'Nexo causal: TEMPORAL — no mecánico.',
    ' ',
    {'t': 'Ej: el cuello largo de la jirafa no se explica\npor la física del cuello, sino por las consecuencias\nde tener cuello largo en ese ambiente.', 'italic': True, 'size': 14},
], ML, Cm(7.4), bw15, Cm(7), SANS, 15, BLACK)

col2 = ML + bw15 + Cm(0.8)
box(sl, 'SELECCIÓN POR CONTINGENCIAS\n(historia individual)',
    col2, Cm(5.8), bw15, Cm(1.3),
    bg_color=NAVY, border=NAVY, font=SANS, size=15, bold=True, color=WHITE)
paras(sl, [
    'Las conductas con consecuencias reforzantes SE REPITEN.',
    'El ambiente "selecciona" comportamientos durante la vida.',
    'Nexo causal: TEMPORAL — no mecánico.',
    ' ',
    {'t': 'Ej: Homero come donuts no se explica\npor sus neuronas, sino por las consecuencias\nde comer donuts en su historia.', 'italic': True, 'size': 14, 'color': LGRAY},
], col2, Cm(7.4), bw15, Cm(7), SANS, 15, BLACK)

txt(sl, 'El AF no busca nexos físico-contiguos (neurona → conducta) sino nexos TEMPORALES-FUNCIONALES (contingencia → conducta).',
    ML, Cm(15.8), CW-Cm(1), Cm(1.8),
    SANS, 15, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 16 — CONDUCTA ENCUBIERTA: EL PENSAMIENTO
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, 'El pensamiento no CAUSA la conducta — ES conducta',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 30, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

txt(sl, 'Conductismo radical (Skinner): los "eventos privados" son conducta encubierta, no causas.',
    ML, Cm(4.2), CW-Cm(1), Cm(1.2), SANS, 17, bold=True, color=NAVY)

data16 = [
    ['Visión tradicional (mentalista)', 'Visión conductista radical'],
    ['"Homero piensa: \'me merezco un donut\' →\n[eso CAUSA que] → Homero come el donut."',
     '"Homero emite conducta verbal encubierta \'me merezco un donut\' EN EL MISMO CONTEXTO en que come donuts.'],
    ['Los pensamientos son la CAUSA de la conducta.',
     'Los pensamientos son PARTE de la conducta — también hay que explicarlos.'],
    ['Para cambiar la conducta: cambiar los pensamientos\n(terapia cognitiva clásica).',
     'Para cambiar la conducta: cambiar las contingencias\n(que también modificarán los pensamientos).'],
    ['La conducta verbal ("lo haré mejor") predice el comportamiento.',
     'Lo que Homero DICE puede no coincidir con lo que HACE. El comportamiento es la evidencia.'],
]
tbl(sl, data16, ML, Cm(5.5), CW-Cm(1), Cm(9.5), fs=12)

txt(sl, 'Implicación clínica: el autoinforme del paciente es un DATO, no la evidencia principal.',
    ML, Cm(15.8), CW-Cm(1), Cm(1.3),
    SANS, 16, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 17 — EL EJEMPLO DE DECIR VS HACER
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, 'Decir "voy a cambiar" no es lo mismo que cambiar',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 30, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

txt(sl, 'Homero después de cada crisis dice: "Lo juro por mis hijos, voy a comer menos donuts y trabajar más."',
    ML, Cm(4.2), Cm(28), Cm(1.5), SANS, 17, italic=True, color=NAVY)

paras(sl, [
    {'t': 'Visión mentalista:', 'bold': True, 'size': 16},
    '"Homero cree en lo que dice. Si su motivación fuera real, cambiaría."',
    '→ La terapia busca cambiar sus pensamientos y creencias.',
    ' ',
    {'t': 'Visión conductual (anti-descriptivista):', 'bold': True, 'size': 16, 'color': NAVY},
    '"Lo que Homero dice es conducta verbal moldeada por consecuencias sociales."',
    '→ Decir "voy a cambiar" es reforzado por las reacciones de Marge.',
    '→ No garantiza cambio conductual porque los reforzadores del donut siguen intactos.',
    ' ',
    {'t': 'La pregunta clínica correcta no es "¿Homero lo cree de verdad?" sino\n"¿Qué contingencias mantienen la conducta de comer donuts?"', 'bold': True, 'size': 15, 'color': NAVY},
], ML, Cm(6.0), CW-Cm(1), Cm(9), SANS, 15, BLACK)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 18 — VOLVEMOS A HOMERO
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, 'Homero: del diagnóstico al análisis filosófico-conductual',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 26, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

data18 = [
    ['Nivel de análisis', 'Explicación de la conducta de Homero', 'Utilidad clínica'],
    ['Folk psychology\n(normativa)',
     '"Homero es impulsivo, tiene baja autoestima\ny falta de voluntad."',
     'Evalúa si su conducta es racional.\nNo explica las causas ni permite intervenir.'],
    ['Neurociencia\n(subagencial)',
     '"Su sistema de recompensa responde intensamente\nal azúcar y la grasa."',
     'Describe el sustrato biológico.\nNo indica cómo cambiar la conducta.'],
    ['Análisis de la Conducta\n(agencial)',
     'Donut disponible (Ed) → come (R) → placer inmediato + evitar pensamientos de trabajo (C).\nHistoria masiva de reforzamiento positivo con donuts.',
     'Explica qué MANTIENE la conducta.\nPermite diseñar la intervención directamente.'],
    ['Conducta encubierta',
     '"Me lo merezco" / "Total uno más no cambia nada" son verbalizaciones encubiertas\nque también forman parte de la cadena conductual.',
     'También son objetivo de intervención,\npero no las causas — son parte del patrón.'],
]
tbl(sl, data18, ML, Cm(4.2), CW-Cm(1), Cm(10.5), fs=12)

txt(sl, 'El AF no dice que Homero "tiene" algo. Explica POR QUÉ hace lo que hace y CÓMO cambiarlo.',
    ML, Cm(15.5), CW-Cm(1), Cm(1.8),
    SANS, 16, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 19 — IDEAS CLAVE
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
bg(sl); dividers(sl); label(sl)

txt(sl, 'Para llevarse hoy',
    ML, Cm(2.0), CW-Cm(4.5), Cm(1.8),
    SERIF, 36, bold=True, color=BLACK, align=PP_ALIGN.CENTER)

ideas = [
    ('01',
     'Las atribuciones mentales ("tiene ansiedad", "tiene baja autoestima") son NORMATIVAS:\nevalúan el comportamiento según una norma, no explican sus causas.'),
    ('02',
     'El AF busca explicaciones NOMOLÓGICAS: establece las contingencias que CAUSAN y MANTIENEN\nla conducta. Eso es lo que permite modificarla.'),
    ('03',
     'El pensamiento no CAUSA la conducta — es parte de ella. La evidencia clínica\nes el COMPORTAMIENTO, no lo que el paciente dice (ni lo que dice que piensa).'),
]
for i, (num, texto) in enumerate(ideas):
    y = Cm(4.8) + i * Cm(4.0)
    txt(sl, num, ML, y, Cm(2.8), Cm(1.8), SERIF, 28, bold=True, color=NAVY)
    hline(sl, ML+Cm(3.2), y+Cm(1.0), CW-Cm(7.2), LGRAY)
    txt(sl, texto, ML+Cm(3.2), y, CW-Cm(7.5), Cm(3.8), SANS, 18, color=BLACK)

footer(sl); add_logo(sl)


# ═══════════════════════════════════════════════════════
# SLIDE 20 — CIERRE CON FOTO
# ═══════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
sl.shapes.add_picture(PHOTO, 0, 0, W, H)

overlay = sl.shapes.add_shape(1, 0, 0, W*0.52, H)
overlay.fill.solid(); overlay.fill.fore_color.rgb = RGBColor(0xF0,0xEB,0xE0)
overlay.line.fill.background()
xPr = overlay.fill._xPr; sf = xPr.solidFill
clr = sf.find(qn('a:srgbClr'))
if clr is None:
    clr = etree.SubElement(sf, qn('a:srgbClr')); clr.set('val','F0EBE0')
alpha = etree.SubElement(clr, qn('a:alpha')); alpha.set('val','82000')

hline(sl, ML, Cm(1.6), Cm(16), BLACK, Pt(2))
hline(sl, ML, Cm(17.0), CW, BLACK, Pt(2))

txt(sl, '@PSICO_EDUCA20', ML, Cm(0.5), Cm(16), Cm(0.9), SANS, 12, color=GRAY)

txt(sl, 'Gracias por\nsu Atención',
    ML, Cm(4.0), Cm(16), Cm(6.5),
    SERIF, 52, bold=True, italic=True, color=BLACK)

txt(sl, 'Bases filosóficas del Análisis de la Conducta',
    ML, Cm(11.5), Cm(16), Cm(2.0), SANS, 16, color=GRAY)

txt(sl, 'Lic. Jean Clemotte  |  PsicoEduca',
    ML, Cm(14.5), Cm(16), Cm(1.3), SANS, 15, italic=True, color=NAVY)

add_logo(sl)


# ═══════════════════════════════════════════════════════
# GUARDAR
# ═══════════════════════════════════════════════════════
output = r'C:\Users\MI PC\psicoeduca\materiales\presentacion-bases-filosoficas.pptx'
prs.save(output)
print('Listo: ' + output)
print('20 slides | Caso: Homero Simpson | Bases filosoficas del AC')
