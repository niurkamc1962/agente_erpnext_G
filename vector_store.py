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


def obtener_o_crear_indice(tipo="usuario"):
    """Carga el índice específico: 'usuario' o 'tecnico'."""
    path = (
        Config.STORAGE_DIR_USUARIO if tipo == "usuario" else Config.STORAGE_DIR_TECNICO
    )

    if os.path.exists(path) and os.listdir(path):
        storage_context = StorageContext.from_defaults(persist_dir=path)
        return load_index_from_storage(storage_context)

    # Si no existe, devuelve un índice vacío para empezar
    return VectorStoreIndex.from_documents([])


def cargar_todo_el_conocimiento():
    """Crea los dos cerebros por separado."""

    # --- CEREBRO USUARIO (Manuales Multiformato) ---
    if Config.DOCS_PATH.exists():
        print(f"📚 Indexando manuales en {Config.DOCS_PATH}...")
        reader_docs = SimpleDirectoryReader(
            input_dir=str(Config.DOCS_PATH),
            recursive=True,
            # Añadimos .docx y .pdf a la lista
            required_exts=[".md", ".pdf", ".txt", ".docx"],
        )
        # LlamaIndex detectará automáticamente que es un PDF o DOCX
        # y usará el "parser" adecuado.
        docs_usuario = reader_docs.load_data()
        index_user = VectorStoreIndex.from_documents(docs_usuario)
        index_user.storage_context.persist(persist_dir=Config.STORAGE_DIR_USUARIO)
        print("✅ Índice de Usuario (Multiformato) guardado.")

    # --- 2. CEREBRO TÉCNICO (Solo código) ---
    if Config.BENCH_PATH.exists():
        print(f"💻 Creando Índice TÉCNICO en {Config.BENCH_PATH}...")
        reader_apps = SimpleDirectoryReader(
            input_dir=str(Config.BENCH_PATH),
            recursive=True,
            required_exts=[".py", ".json"],
        )
        docs_tech = reader_apps.load_data()
        index_tech = VectorStoreIndex.from_documents(docs_tech)
        index_tech.storage_context.persist(persist_dir=Config.STORAGE_DIR_TECNICO)
        print("✅ Índice Técnico guardado.")


def actualizar_documento_en_indice(file_path, tipo="usuario"):
    """Actualización mejorada para soportar archivos binarios (PDF/DOCX)."""
    try:
        index = obtener_o_crear_indice(tipo=tipo)
        persist_path = (
            Config.STORAGE_DIR_USUARIO
            if tipo == "usuario"
            else Config.STORAGE_DIR_TECNICO
        )

        # --- CAMBIO CRÍTICO AQUÍ ---
        # En lugar de f.read(), usamos el Reader de LlamaIndex que sabe leer binarios
        reader = SimpleDirectoryReader(input_files=[file_path])
        docs = (
            reader.load_data()
        )  # Esto devuelve una lista de Documentos (páginas en caso de PDF)

        # Borrar referencia vieja
        try:
            index.delete_ref_doc(file_path, delete_from_storage=True)
        except:
            pass

        # Insertamos los nuevos documentos (si el PDF tiene 10 páginas, insertará las 10)
        for doc in docs:
            doc.doc_id = file_path  # Mantenemos el ID para futuras actualizaciones
            index.insert(doc)

        index.storage_context.persist(persist_dir=persist_path)
        print(f"🚀 [Índice {tipo.upper()}] Actualizado: {file_path}")

    except Exception as e:
        print(f"❌ Error actualizando {file_path}: {e}")
