from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import (
    OllamaEmbedding,
)  # <-- Necesario para evitar error de OpenAI
from llama_index.core import Settings
from vector_store import obtener_o_crear_indice
from config import Config

# --- CONFIGURACIÓN GLOBAL DE LLAMA-INDEX ---
# Esto asegura que todo el motor use Ollama localmente
Settings.llm = Ollama(model=Config.MODEL, request_timeout=300.0)

# Definimos el modelo de embeddings (debe ser el mismo usado en ingest.py)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")


class ErpAgent:
    def __init__(self):
        # 1. Cargamos el índice (el cerebro con el conocimiento de ERPNext)
        self.index = obtener_o_crear_indice()

        # 2. Definimos la personalidad del Consultor
        self.system_prompt = (
            "Eres el Consultor Senior de ERPNext. Tu objetivo es ayudar a usuarios finales.\n"
            "REGLAS DE ORO:\n"
            "1. Si la respuesta está en los manuales (.md, .pdf), úsalos para dar pasos simples.\n"
            "2. Si la información solo está en los archivos .json o .py, traduce eso a lenguaje humano.\n"
            "   Ejemplo: Si ves 'status': 'Draft', dile al usuario 'La factura debe estar en estado Borrador'.\n"
            "3. Siempre responde con una guía paso a paso, clara y sin tecnicismos innecesarios.\n"
            "4. Si el usuario pregunta algo técnico, responde de forma funcional a menos que pida detalles de desarrollador.\n"
            "5. Si no encuentras la respuesta en el contexto, di amablemente que no tienes ese manual disponible."
        )

        # 3. Configuramos el motor de chat en modo 'context'
        # para que busque automáticamente en la base vectorial.
        self.chat_engine = self.index.as_chat_engine(
            chat_mode="context",
            system_prompt=self.system_prompt,
            similarity_top_k=7,  # Recupera hasta 7 fragmentos de texto para mayor precisión
        )

    def consultar(self, pregunta):
        """Envía la pregunta al motor de chat y devuelve la respuesta del LLM."""
        try:
            return self.chat_engine.chat(pregunta)
        except Exception as e:
            return f"Lo siento, ocurrió un error al procesar tu consulta: {str(e)}"
