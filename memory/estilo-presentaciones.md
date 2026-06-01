---
name: estilo-presentaciones
description: Prompt maestro de estilo para todas las presentaciones de PsicoEduca. Usar siempre que Jean pida una presentación, sin necesidad de que lo solicite explícitamente.
metadata:
  type: project
---

# Estilo maestro — Presentaciones PsicoEduca

Cuando Jean pida una presentación, aplicar SIEMPRE este estilo sin preguntar.
Solo adaptar el **contenido** — el diseño es fijo.

---

## 1. IDENTIDAD VISUAL

### Colores (valores exactos)
| Uso | Hex | RGB |
|-----|-----|-----|
| Fondo de todos los slides | `#E8E3D8` | (232, 227, 216) |
| Acento principal (navy) | `#1B3A5C` | (27, 58, 92) |
| Texto principal | `#1A1A1A` | (26, 26, 26) |
| Texto secundario / notas | `#666666` | (102, 102, 102) |
| Líneas sutiles | `#CCC8C0` | (204, 200, 192) |
| Fondo de cajas | `#D8D2C5` | (216, 210, 197) |
| Acento azul (segunda columna) | `#2E76A0` | (46, 118, 160) |
| Blanco | `#FFFFFF` | (255, 255, 255) |
| Rojo (negativo) | `#CC3333` | (204, 51, 51) |
| Verde (positivo) | `#227744` | (34, 119, 68) |

### Tipografía
| Elemento | Fuente | Tamaño | Estilo |
|---------|--------|--------|--------|
| Título principal (portada) | Georgia | 52–58pt | Bold |
| Títulos de slide | Georgia | 28–34pt | Bold, **centrado** |
| Títulos de sección (portadas de bloque) | Georgia | 44–52pt | Bold, centrado |
| Cuerpo de texto | Calibri | 16–19pt | Normal |
| Bullets principales | Calibri | 17–19pt | Normal |
| Texto en tablas | Calibri | 13–16pt | Header bold |
| Texto en cajas (box) | Calibri | 15–17pt | Centrado |
| Footer | Calibri | 11pt | Italic, gris |
| Etiqueta superior | Calibri | 9pt | Gris |
| Números de bloque (01, 02...) | Georgia | 20–24pt | Bold, navy |

### Logo
- Archivo: `C:\Users\MI PC\Desktop\PsicoEduca\Marketing\PsicoEduca Logo final_Mesa de trabajo 1 copia 4.png`
- Posición: esquina superior derecha
- Coordenadas: `x = W - 4.2cm`, `y = 0.2cm`
- Tamaño: `3.8cm × 3.0cm`
- Aparece en **TODOS** los slides sin excepción

---

## 2. DIMENSIONES Y MÁRGENES

```
Ancho slide:   33.87cm  (widescreen 16:9)
Alto slide:    19.05cm
Margen izq:    1.8cm
Ancho útil:    30.27cm  (CW = W - ML - MR aprox)
```

---

## 3. TIPOS DE SLIDE Y SU ESTRUCTURA

### A. PORTADA (slide 1)
```
- Fondo: #E8E3D8
- 1 línea horizontal gruesa (Pt 2) arriba, a ~1.8cm del top (sin llegar al logo)
- 1 línea horizontal gruesa (Pt 2) abajo, a ~17.2cm del top
- Título grande (Georgia 52–58pt bold) a la izquierda
- Subtítulo (Calibri 16pt) abajo del título
- "Presentación por Lic. Jean Clemotte" (Georgia 15pt italic) al final
- Logo arriba derecha
- Footer abajo izquierda
```

### B. SLIDE DE SECCIÓN / PORTADA DE BLOQUE (slides 4, 8, 16)
```
- Fondo: #E8E3D8
- 1 línea horizontal (Pt 0.8, navy) horizontal a mitad de slide (~8cm)
- "Bloque 0X" (Calibri 22pt, navy, centrado) arriba de la línea
- Título del bloque (Georgia 44–52pt bold, centrado) debajo de la línea
- Logo arriba derecha
- Footer abajo izquierda
```

### C. SLIDE DE CONTENIDO (todos los demás)
```
Estructura fija:
  - Fondo: #E8E3D8
  - TOP: etiqueta "ANÁLISIS FUNCIONAL DE LA CONDUCTA" (9pt, gris, izq) + "PSICOEDUCA" (9pt, gris, der)
  - 2 líneas finas negras arriba (~1.5cm y ~1.8cm) — dejan espacio para el logo
  - Título del slide (Georgia, 28–34pt, bold, CENTRADO, navy o negro)
  - Área de contenido: empieza a ~4.0–4.5cm del top
  - 2 líneas finas negras abajo (~17.3cm y ~17.6cm)
  - Footer: "Lic. Jean Clemotte  |  @Psico_Educa20" (11pt italic gris, izq)
  - Logo arriba derecha (siempre)
```

### D. SLIDE DE CIERRE (último slide)
```
- Foto de Jean como fondo completo (sentado.JPG)
  Ruta: C:\Users\MI PC\Desktop\PsicoEduca\Marketing\BOOK\sentado.JPG
- Overlay semitransparente crema (~82% opacidad) en la mitad izquierda
- 2 líneas horizontales gruesas (arriba y abajo)
- "@PSICO_EDUCA20" pequeño arriba
- "Gracias por su Atención" (Georgia 52pt, bold italic)
- Subtítulo de la presentación (Calibri 17pt, gris)
- "Lic. Jean Clemotte  |  PsicoEduca" (Calibri 15pt italic, navy)
- Logo arriba derecha
```

---

## 4. ELEMENTOS REUTILIZABLES

### Tabla estándar
```python
- Header row: fondo navy, texto blanco, Calibri bold 14–16pt
- Filas impares: fondo #E8E3D8
- Filas pares: fondo #D8D2C5
- Texto: Calibri 13–16pt
- Centrado o left según contenido
```

### Caja (box)
```python
- Fondo: #D8D2C5
- Borde: navy 1pt
- Texto: Calibri 15–17pt centrado
- Esquinas redondeadas (MSO_SHAPE 5 = rounded rectangle)
```

### Schema de 2 columnas (comparativo)
```python
- Izquierda: header navy + cuerpo
- Derecha: header azul (#2E76A0) + cuerpo
- Texto izquierda: 16–18pt
```

### Triple contingencia (3 cajas + flechas)
```python
- 3 cajas iguales en fila horizontal
- Flechas "▶" (Calibri 26pt navy) entre cajas
- Cada caja: ~9cm ancho × 7cm alto
- Texto caja: Calibri 16pt centrado
```

---

## 5. ESTRUCTURA ESTÁNDAR DE UNA PRESENTACIÓN

```
Slide 1:  Portada
Slide 2:  Gancho — caso de Los Simpsons con contexto Paraguay
Slide 3:  Índice (3 bloques)
Slide 4:  Portada Bloque 01
Slides 5–N: Contenido Bloque 1
Slide N+1: Portada Bloque 02
Slides ...: Contenido Bloque 2
Slide M:  Portada Bloque 03
Slides ...: Contenido Bloque 3
Slide X:  Ideas clave (3 puntos con número + texto + línea separadora)
Slide X+1: Cierre con foto
```

---

## 6. REGLAS DE CONTENIDO

### Personajes de Los Simpsons como ejemplos
- Usar personajes de Los Simpsons para los casos clínicos guía
- El caso guía acompaña TODA la presentación
- Personajes disponibles: Marge, Homero, Bart, Lisa, Maggie
- Elegir el personaje según el tema (Marge = ansiedad/agorafobia, Bart = conducta disruptiva/evitación escolar, Homer = hábitos, Lisa = sobreexigencia)

### Contexto Paraguay siempre
- Lugares: Super Stock, Shopping del Sol, Villa Morra, Asunción, CDE
- Referencias culturales: tereré, chipa, asado del domingo, partido de fútbol
- Ejemplos clínicos adaptados a la realidad paraguaya

### Proporcionalidad de texto
- Si un slide tiene 2–3 bullets: usar 20–22pt
- Si tiene 4–5 bullets: usar 17–19pt
- Si tiene tabla con muchas celdas: usar 13–15pt
- NUNCA dejar más del 30% del área útil vacía

### Una idea por slide
- Máximo 1 concepto central por slide
- Si el contenido es mucho, dividir en 2 slides

---

## 7. PYTHON — FUNCIONES BASE (copiar al inicio de cada script)

```python
from pptx import Presentation
from pptx.util import Cm, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from lxml import etree
from pptx.oxml.ns import qn

# COLORES
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

def bg(slide, color=BG):
    f = slide.background.fill
    f.solid()
    f.fore_color.rgb = color

def hline(slide, x, y, w, color=BLACK, thick=Pt(1.5)):
    s = slide.shapes.add_shape(1, x, y, w, thick)
    s.fill.solid(); s.fill.fore_color.rgb = color; s.line.fill.background()

def txt(slide, text, x, y, w, h, font=SANS, size=16, bold=False,
        italic=False, color=BLACK, align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = align
    r = p.add_run(); r.text = text
    r.font.name=font; r.font.size=Pt(size); r.font.bold=bold
    r.font.italic=italic; r.font.color.rgb=color
    return tb

def paras(slide, lines, x, y, w, h, font=SANS, size=16, color=BLACK, align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = True
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.alignment = align
        if isinstance(ln, dict):
            r = p.add_run(); r.text=ln.get('t','')
            r.font.name=ln.get('font',font); r.font.size=Pt(ln.get('size',size))
            r.font.bold=ln.get('bold',False); r.font.italic=ln.get('italic',False)
            r.font.color.rgb=ln.get('color',color)
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

def top_label(slide, label='TEMA DE LA PRESENTACIÓN'):
    txt(slide, label, ML, Cm(0.6), Cm(20), Cm(0.8), SANS, 9, color=GRAY)

def tbl(slide, data, x, y, w, h, hdr_bg=NAVY, hdr_fg=WHITE,
        odd=BG, even=BOXBG, font_size=14, center=False):
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
                    run.font.name=SANS; run.font.size=Pt(font_size)
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

def box(slide, text, x, y, w, h, bg_color=BOXBG, border=NAVY,
        font=SANS, size=16, bold=False, color=BLACK, align=PP_ALIGN.CENTER):
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
    txt(sl, titulo, 0, Cm(8.3), W, Cm(6), SERIF, 46, bold=True, color=BLACK, align=PP_ALIGN.CENTER)
    footer(sl); add_logo(sl)
    return sl
```

---

## 8. PROMPT PARA PEDIR UNA NUEVA PRESENTACIÓN

Cuando Jean diga: **"Preparame una presentación sobre [TEMA]"**, hacer lo siguiente:

1. **Leer este archivo** para aplicar el estilo sin preguntar
2. **Preguntar únicamente:**
   - ¿Cuál es el contenido de cada bloque? (si no lo provee)
   - ¿Qué personaje de Los Simpsons usamos como caso guía?
3. **Generar directo** el script Python con las funciones base + contenido nuevo
4. **Ejecutar** el script y entregar el `.pptx` listo
5. **No preguntar** nada sobre colores, fuentes, logos, márgenes, estructura

---

## 9. ARCHIVOS NECESARIOS (siempre en el mismo lugar)

```
Logo:  C:\Users\MI PC\Desktop\PsicoEduca\Marketing\PsicoEduca Logo final_Mesa de trabajo 1 copia 4.png
Foto:  C:\Users\MI PC\Desktop\PsicoEduca\Marketing\BOOK\sentado.JPG
Output: C:\Users\MI PC\psicoeduca\materiales\[nombre-presentacion].pptx
Script: C:\Users\MI PC\psicoeduca\materiales\crear_[nombre].py
```

---

**Why:** Jean invirtió tiempo refinando este estilo. El objetivo es que cada presentación sea consistente con la identidad de PsicoEduca sin rehacer el diseño cada vez.
**How to apply:** En cada nueva presentación, importar las funciones base de la sección 7, aplicar la estructura de la sección 5, y solo cambiar el contenido.
