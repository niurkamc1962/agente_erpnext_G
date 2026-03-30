# agent.py

from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from vector_store import obtener_o_crear_indice
from config import Config

# Configuración global de LlamaIndex
Settings.llm = Ollama(model=Config.MODEL, request_timeout=300.0)


class ErpAgent:
    def __init__(self):
        self.index = obtener_o_crear_indice()
        self.system_prompt = (
            "Eres el Consultor Senior de ERPNext. Tu objetivo es ayudar a usuarios finales.\n"
            "REGLAS DE ORO:\n"
            "1. Si la respuesta está en los manuales (.md, .pdf), úsalos para dar pasos simples.\n"
            "2. Si la información solo está en los archivos .json o .py, traduce eso a lenguaje humano.\n"
            "Ejemplo: Si ves 'status': 'Draft', dile al usuario 'La factura debe estar en estado Borrador'.\n"
            "3. Siempre responde con una guía paso a paso.\n"
            "4. Si el usuario pregunta algo técnico, responde de forma funcional a menos que pida detalles de desarrollador."
        )
        # Aumentamos similarity_top_k para que lea más fragmentos de manuales
        self.chat_engine = self.index.as_chat_engine(
            chat_mode="context", system_prompt=self.system_prompt, similarity_top_k=7
        )

    def consultar(self, pregunta):
        return self.chat_engine.chat(pregunta)
