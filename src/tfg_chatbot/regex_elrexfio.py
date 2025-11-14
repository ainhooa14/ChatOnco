"""
Detección por expresiones regulares de ELREXFIO / elranatamab
en texto clínico ya preprocesado.
"""

import re
from typing import Optional

import pandas as pd


# Patrón general para el fármaco (marca + genérico + posibles variantes)
ELREXFIO_PATTERN = re.compile(
    r"\b(elrexfio|elranatamab)\b",
    flags=re.IGNORECASE,
)


def has_elrexfio(text: Optional[str]) -> int:
    """
    Devuelve 1 si el texto contiene alguna mención a ELREXFIO / elranatamab,
    0 en caso contrario.
    """
    if not text:
        return 0
    return int(bool(ELREXFIO_PATTERN.search(text)))


def add_elrexfio_regex_column(
    df: pd.DataFrame,
    text_col: str = "texto_clean",
    new_col: str = "pred_regex_elrexfio",
) -> pd.DataFrame:
    """
    Devuelve una copia del DataFrame con una columna binaria `new_col`
    indicando si se detecta ELREXFIO / elranatamab por regex.
    """
    df = df.copy()
    df[new_col] = df[text_col].apply(has_elrexfio)
    return df
