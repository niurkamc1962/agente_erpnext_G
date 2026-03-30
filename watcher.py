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

    # Programamos la vigilancia para ambas carpetas
    observer.schedule(event_handler, str(Config.BENCH_PATH), recursive=True)
    observer.schedule(event_handler, str(Config.DOCS_PATH), recursive=True)

    observer.start()
    print(f"👀 Vigilando cambios en:\n - {Config.BENCH_PATH}\n - {Config.DOCS_PATH}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
