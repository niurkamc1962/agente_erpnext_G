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
Settings.llm = Ollama(
    model=Config.MODEL,
    request_timeout=300.0,
    temperature=0.1,  # <-- MUY IMPORTANTE: Mantenerlo entre 0.0 y 0.2
    additional_kwargs={"top_p": 0.1},
)

# Definimos el modelo de embeddings (debe ser el mismo usado en ingest.py)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")


class ErpAgent:

    def __init__(self, modo="usuario"):  # Añadimos el modo
        # Cargamos SOLO el índice que corresponde al modo
        self.index = obtener_o_crear_indice(tipo=modo)

        if modo == "usuario":
            self.system_prompt = (
                "Eres un Consultor Funcional amable. Solo hablas de la interfaz de ERPNext.\n"
                "Tu conocimiento proviene de manuales de usuario. Si no sabes algo, no inventes código."
            )
        else:
            self.system_prompt = (
                "Eres un Desarrollador Senior de Frappe. Responde con detalles técnicos, "
                "menciona archivos .py y estructuras JSON."
            )

        # Configuramos el motor de chat en modo 'context'
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
