# config.py
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class Config:
    # Esta línea detecta automáticamente la carpeta donde está config.py
    BASE_DIR = Path(__file__).resolve().parent

    # Unimos la base con la ruta del .env para tener una ruta absoluta dinámica
    # Si en el .env dice "info_erp/apps", se convertirá en "/ruta/actual/del/proyecto/info_erp/apps"
    BENCH_PATH = BASE_DIR / os.getenv("BENCH_PATH", "info_erp/apps")
    DOCS_PATH = BASE_DIR / os.getenv("DOCS_PATH", "info_erp/documentacion")

    MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5-1.5b-instruct-q4_k_m.0:latest")
    EMBED_MODEL = "nomic-embed-text"

    # La base de datos vectorial también relativa a la raíz
    # Separando los indices para los usuarios y para los tecnicos
    STORAGE_DIR_USUARIO = str(BASE_DIR / "storage_usuario")
    STORAGE_DIR_TECNICO = str(BASE_DIR / "storage_tecnico")
