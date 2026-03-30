import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class Config:
    BASE_DIR = Path(__file__).resolve().parent
    BENCH_PATH = Path(os.getenv("BENCH_PATH", "./apps"))
    # Asegúrate de tener esta carpeta creada o cambia la ruta
    DOCS_PATH = Path(os.getenv("DOCS_PATH", "./documentacion_local"))

    MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5-7b-instruct-q4_k_m")
    # Usaremos el mismo modelo para embeddings o uno ligero como 'nomic-embed-text'
    EMBED_MODEL = "nomic-embed-text"

    STORAGE_DIR = str(BASE_DIR / "storage_vectorial")
