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
        if event.src_path.endswith((".json", ".py", ".md", ".pdf", ".txt")):
            print(f"🔄 Cambio detectado en: {event.src_path}")
            # Llamamos a nuestra función de actualización inteligente
            actualizar_documento_en_indice(event.src_path)


def iniciar_vigilancia():
    event_handler = ErpSourceHandler()
    observer = Observer()

    # Solo programamos si las rutas existen
    if Config.BENCH_PATH.exists():
        observer.schedule(event_handler, str(Config.BENCH_PATH), recursive=True)
    else:
        print(f"⚠️ ADVERTENCIA: No se encontró la ruta de apps: {Config.BENCH_PATH}")

    if Config.DOCS_PATH.exists():
        observer.schedule(event_handler, str(Config.DOCS_PATH), recursive=True)
    else:
        print(f"⚠️ ADVERTENCIA: No se encontró la ruta de docs: {Config.DOCS_PATH}")

    # Solo iniciamos si hay algo que observar
    try:
        observer.start()
        print("👀 Vigilando cambios...")
        while True:
            time.sleep(1)
    except Exception as e:
        print(f"❌ Error al iniciar el observador: {e}")
