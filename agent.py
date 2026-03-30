from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import (
    OllamaEmbedding,
)  # <-- Necesario para evitar error de OpenAI
from llama_index.core import Settings
from vector_store import obtener_o_crear_indice
from config import Config

# --- CONFIGURACIÓN GLOBAL DE LLAMA-INDEX ---
# Esto asegura que todo el motor use Ollama localmente ademas se 
# puso la temperatura baja para que sea mas preciso y no alucine
Settings.llm = Ollama(model=Config.MODEL, request_timeout=300.0, temperature=0.1)

# Definimos el modelo de embeddings (debe ser el mismo usado en ingest.py)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")


class ErpAgent:
    def __init__(self):
        # 1. Cargamos el índice (el cerebro con el conocimiento de ERPNext)
        self.index = obtener_o_crear_indice()

        # 2. Definimos la personalidad del Consultor
        self.system_prompt = (
            "Eres un Consultor Funcional de ERPNext experto en procesos de negocio.\n"
            "Tu objetivo es guiar a un usuario final que NO sabe programar.\n\n"
            "REGLAS CRÍTICAS:\n"
            "1. PROHIBIDO mencionar nombres de archivos (.json, .py) o rutas de carpetas.\n"
            "2. PROHIBIDO mostrar fragmentos de código o lógica de programación.\n"
            "3. Si lees un archivo .json, interpreta los 'labels' como nombres de campos en la pantalla.\n"
            "   Ejemplo: Si el JSON dice 'fieldname': 'bank_name', dile al usuario 'Escribe el nombre del banco'.\n"
            "4. Transforma la estructura técnica en pasos de navegación.\n"
            "   Ejemplo: 'Para crear un Banco, ve al módulo de Tesorería, haz clic en Nuevo Banco y rellena los siguientes campos...'\n"
            "5. Si no encuentras el proceso exacto, explica cómo crees que funciona basándote en los campos que ves en el sistema."
        )

        # 3. Configuramos el motor de chat en modo 'context'
        # para que busque automáticamente en la base vectorial.
        self.chat_engine = self.index.as_chat_engine(
            chat_mode="context",
            system_prompt=self.system_prompt,
            similarity_top_k=8,  # Recupera hasta 8 fragmentos de texto para mayor precisión
        )

    def consultar(self, pregunta):
        """Envía la pregunta al motor de chat y devuelve la respuesta del LLM."""
        try:
            return self.chat_engine.chat(pregunta)
        except Exception as e:
            return f"Lo siento, ocurrió un error al procesar tu consulta: {str(e)}"
