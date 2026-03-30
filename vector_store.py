import os
from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
    Document,
    SimpleDirectoryReader,
    Settings,  # Importante: Controla el motor de embeddings
)
from llama_index.embeddings.ollama import OllamaEmbedding
from config import Config

# --- CONFIGURACIÓN CRÍTICA ---
# Forzamos a LlamaIndex a usar Ollama para convertir texto a números (embeddings)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")


def obtener_o_crear_indice():
    """Carga el índice existente o devuelve uno nuevo."""
    if os.path.exists(Config.STORAGE_DIR) and os.listdir(Config.STORAGE_DIR):
        storage_context = StorageContext.from_defaults(persist_dir=Config.STORAGE_DIR)
        return load_index_from_storage(storage_context)

    return VectorStoreIndex.from_documents([])


def cargar_todo_el_conocimiento():
    """Indexa código y manuales desde las carpetas configuradas."""
    documentos_totales = []

    # 1. Indexar Código/JSON
    if Config.BENCH_PATH.exists():
        print(f"🔍 Indexando código en {Config.BENCH_PATH}...")
        reader_apps = SimpleDirectoryReader(
            input_dir=str(Config.BENCH_PATH),
            recursive=True,
            required_exts=[".py", ".json"],
        )
        documentos_totales.extend(reader_apps.load_data())

    # 2. Indexar Manuales (.md, .txt, .pdf)
    if hasattr(Config, "DOCS_PATH") and Config.DOCS_PATH.exists():
        print(f"🔍 Indexando manuales en {Config.DOCS_PATH}...")
        reader_docs = SimpleDirectoryReader(
            input_dir=str(Config.DOCS_PATH),
            recursive=True,
            required_exts=[".md", ".pdf", ".txt"],
        )
        documentos_totales.extend(reader_docs.load_data())

    if not documentos_totales:
        print("⚠️ No se encontraron archivos para indexar.")
        return None

    # Crear el índice unificado usando el embed_model definido en Settings
    index = VectorStoreIndex.from_documents(documentos_totales)
    index.storage_context.persist(persist_dir=Config.STORAGE_DIR)
    print(f"✅ Memoria inicial creada: {len(documentos_totales)} archivos procesados.")
    return index


def actualizar_documento_en_indice(file_path):
    """Actualización en tiempo real para el Watcher."""
    try:
        index = obtener_o_crear_indice()
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        doc = Document(
            text=text,
            doc_id=file_path,
            extra_info={"file_path": file_path},
        )

        # Borrar referencia vieja y refrescar
        try:
            index.delete_ref_doc(file_path, delete_from_storage=True)
        except:
            pass

        index.insert(doc)
        index.storage_context.persist(persist_dir=Config.STORAGE_DIR)
        print(f"🚀 Actualizado: {file_path}")
    except Exception as e:
        print(f"❌ Error actualizando {file_path}: {e}")
