"""
Funciones de preprocesado de texto para las HCE.
"""

import re
import unicodedata
from typing import Optional

import pandas as pd


def strip_accents(text: str) -> str:
    """
    Elimina acentos manteniendo solo caracteres ASCII básicos.
    """
    if text is None:
        return ""
    text = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in text if not unicodedata.combining(ch))


def normalize_whitespace(text: str) -> str:
    """
    Sustituye múltiples espacios, saltos de línea, tabs, etc. por un solo espacio.
    """
    return re.sub(r"\s+", " ", text).strip()


def clean_text(text: Optional[str]) -> str:
    """
    Limpieza básica del texto clínico:
      - convierte a minúsculas
      - elimina acentos
      - normaliza espacios
    """
    if text is None:
        return ""

    text = str(text)
    text = text.lower()
    text = strip_accents(text)
    text = normalize_whitespace(text)
    return text


def add_clean_column(df: pd.DataFrame,
                     text_col: str = "texto_clinico",
                     new_col: str = "texto_clean") -> pd.DataFrame:
    """
    Devuelve una copia del DataFrame con una columna nueva `new_col`
    que contiene la versión limpia de `text_col`.
    """
    df = df.copy()
    df[new_col] = df[text_col].apply(clean_text)
    return df
