Estructura del Proyecto Inicial 

agente_erpnext_G/
├── .env                # Variables de entorno (Rutas y Modelo)
├── pyproject.toml      # Gestionado por uv
├── config.py           # Configuración centralizada
├── vector_store.py     # Gestión de la Base de Datos Vectorial (RAG)
├── agent.py            # El cerebro del Agente (ReAct + Contexto)
└── main.py             # Interfaz de usuario con NiceGUI

## Primero ejecutar ingest.py que es el que lee las carpetas donde se encuentra la informacion para el agente.

## Despues ejecutar main.py que ya hace uso de los archivos vectorizados.