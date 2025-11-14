from dataclasses import dataclass
from pathlib import Path

# Ruta raíz del proyecto (tfg_chatbot/)
PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass
class Paths:
    data_raw: Path = PROJECT_ROOT / "data" / "raw"
    data_interim: Path = PROJECT_ROOT / "data" / "interim"
    data_processed: Path = PROJECT_ROOT / "data" / "processed"
    experiments: Path = PROJECT_ROOT / "experiments_results"
    docs: Path = PROJECT_ROOT / "docs_memoria"

paths = Paths()

# Parámetros globales
SEED: int = 42
RANDOM_STATE: int = SEED
