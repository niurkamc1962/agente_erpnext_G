# watcher.py

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import Config
from vector_store import actualizar_documento_en_indice


class ErpSourceHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        # Filtramos por las extensiones que nos interesan
        file_path = event.src_path
        # Añadimos .docx y .pdf al filtro de usuario
        if file_path.endswith((".md", ".pdf", ".txt", ".docx")):
            actualizar_documento_en_indice(file_path, tipo="usuario")


def iniciar_vigilancia():
    event_handler = ErpSourceHandler()
    observer = Observer()

    # Vigilamos la carpeta de apps (Código)
    if Config.BENCH_PATH.exists():
        observer.schedule(event_handler, str(Config.BENCH_PATH), recursive=True)
        print(f"👀 Vigilando Código en: {Config.BENCH_PATH}")

    # Vigilamos la carpeta de documentos (Manuales)
    if Config.DOCS_PATH.exists():
        observer.schedule(event_handler, str(Config.DOCS_PATH), recursive=True)
        print(f"👀 Vigilando Manuales en: {Config.DOCS_PATH}")

    # Solo iniciamos si hay algo que observar
    try:
        observer.start()
        print("👀 Vigilando cambios...")
        while True:
            time.sleep(1)
    except Exception as e:
        print(f"❌ Error al iniciar el observador: {e}")
