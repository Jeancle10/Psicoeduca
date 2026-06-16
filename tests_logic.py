"""
Lógica de cálculos para tests psicométricos
STAI, BDI, BFI-5, SCL-90-R
"""

# Baremo STAI Estado (de la tabla Baremo del Excel)
BAREMO_STAI_ESTADO = {
    20: 1, 21: 2, 22: 3, 23: 4, 24: 5, 25: 7, 26: 8, 27: 10, 28: 12, 29: 14,
    30: 16, 31: 18, 32: 20, 33: 23, 34: 26, 35: 29, 36: 32, 37: 35, 38: 39,
    39: 42, 40: 46, 41: 50, 42: 54, 43: 57, 44: 61, 45: 64, 46: 67, 47: 70,
    48: 72, 49: 74, 50: 76, 51: 78, 52: 79, 53: 81, 54: 82, 55: 84, 56: 85,
    57: 86, 58: 87, 59: 88, 60: 89
}

# Baremo STAI Rasgo (de la tabla Baremo del Excel)
BAREMO_STAI_RASGO = {
    20: 2, 21: 3, 22: 4, 23: 6, 24: 7, 25: 9, 26: 11, 27: 13, 28: 15, 29: 17,
    30: 19, 31: 22, 32: 24, 33: 27, 34: 30, 35: 33, 36: 36, 37: 39, 38: 42,
    39: 45, 40: 48, 41: 51, 42: 54, 43: 57, 44: 60, 45: 63, 46: 66, 47: 68,
    48: 71, 49: 73, 50: 75, 51: 77, 52: 79, 53: 80, 54: 82, 55: 83, 56: 84,
    57: 85, 58: 86, 59: 87, 60: 88
}


def calcular_stai(respuestas):
    """
    Calcula STAI-E (Estado) y STAI-R (Rasgo)
    STAI-E: Preguntas 4-23 (20 items, escala 0-3)
    STAI-R: Preguntas 24-43 (20 items, escala 0-3)

    Retorna: {
        'estado': {'puntuacion': int, 'percentil': int, 'categoria': str},
        'rasgo': {'puntuacion': int, 'percentil': int, 'categoria': str}
    }
    """
    # STAI Estado: P4-P23 (índices 3-22 en array 0-indexed)
    stai_e_items = [respuestas.get(f'p{i}', 0) for i in range(4, 24)]
    stai_e_suma = sum(int(x) for x in stai_e_items if x)

    # STAI Rasgo: P24-P43 (índices 23-42)
    stai_r_items = [respuestas.get(f'p{i}', 0) for i in range(24, 44)]
    stai_r_suma = sum(int(x) for x in stai_r_items if x)

    # Buscar percentil en baremo
    stai_e_percentil = BAREMO_STAI_ESTADO.get(stai_e_suma, 0)
    stai_r_percentil = BAREMO_STAI_RASGO.get(stai_r_suma, 0)

    # Categorizar
    def categorizar_stai(percentil):
        if percentil > 75:
            return "SEVERO"
        elif percentil >= 25:
            return "MODERADO"
        else:
            return "LEVE"

    return {
        'estado': {
            'puntuacion': stai_e_suma,
            'percentil': stai_e_percentil,
            'categoria': categorizar_stai(stai_e_percentil)
        },
        'rasgo': {
            'puntuacion': stai_r_suma,
            'percentil': stai_r_percentil,
            'categoria': categorizar_stai(stai_r_percentil)
        }
    }


def calcular_bdi(respuestas):
    """
    Calcula BDI (Beck Depression Inventory)
    Preguntas 44-66 (23 items, escala 0-3)

    Categorización:
    - 0-9: Ausente o Mínimo
    - 10-16: LEVE
    - 17-29: MODERADO
    - 30+: SEVERO
    """
    bdi_items = [respuestas.get(f'p{i}', 0) for i in range(44, 67)]
    bdi_suma = sum(int(x) for x in bdi_items if x)

    if bdi_suma <= 9:
        categoria = "Ausente o Mínimo"
    elif bdi_suma <= 16:
        categoria = "LEVE"
    elif bdi_suma <= 29:
        categoria = "MODERADO"
    else:
        categoria = "SEVERO"

    return {
        'puntuacion': bdi_suma,
        'categoria': categoria
    }


def calcular_bfi5(respuestas):
    """
    Calcula BFI-5 (Big Five Inventory - 5 items)
    Preguntas 67-71 (5 items, escala 1-5)

    Retorna 5 scores individuales (1-5 cada uno)
    """
    bfi_items = {
        'neuroticismo': int(respuestas.get('p67', 0)),
        'extraversion': int(respuestas.get('p68', 0)),
        'apertura': int(respuestas.get('p69', 0)),
        'amabilidad': int(respuestas.get('p70', 0)),
        'responsabilidad': int(respuestas.get('p71', 0))
    }

    return bfi_items


def calcular_scl90(respuestas):
    """
    Calcula SCL-90-R (Symptom Checklist 90 items - Revised)
    Preguntas 72-135 (64 items, escala 0-4)

    Categorización:
    - 0-3: Normal
    - 4-10: LEVE
    - 11-20: MODERADO
    - 21+: SEVERO
    """
    scl90_items = [respuestas.get(f'p{i}', 0) for i in range(72, 136)]
    scl90_suma = sum(int(x) for x in scl90_items if x)

    if scl90_suma <= 3:
        categoria = "Normal"
    elif scl90_suma <= 10:
        categoria = "LEVE"
    elif scl90_suma <= 20:
        categoria = "MODERADO"
    else:
        categoria = "SEVERO"

    return {
        'puntuacion': scl90_suma,
        'categoria': categoria
    }


def procesar_todas_evaluaciones(respuestas):
    """
    Procesa todas las evaluaciones de una vez
    Retorna dict con resultados de todos los tests
    """
    return {
        'stai': calcular_stai(respuestas),
        'bdi': calcular_bdi(respuestas),
        'bfi': calcular_bfi5(respuestas),
        'scl90': calcular_scl90(respuestas)
    }
