# main.py

from nicegui import ui, run
from agent import ErpAgent
from watcher import iniciar_vigilancia
import threading

# Inicializamos el agente
agent = ErpAgent()


# Función para correr el watcher en segundo plano
def start_watcher():
    t = threading.Thread(target=iniciar_vigilancia, daemon=True)
    t.start()


@ui.page("/")
def main_page():
    ui.label("ERPNext Copilot Enterprise").classes("text-2xl font-bold p-4")

    chat_container = ui.column().classes(
        "w-full h-96 border p-4 overflow-y-auto bg-slate-50"
    )

    with ui.row().classes("w-full p-4 items-center"):
        input_txt = ui.input(placeholder="¿Cómo registro un nuevo...?").classes(
            "flex-grow"
        )
        btn_enviar = ui.button("Enviar").classes("ml-2")

    async def enviar():
        pregunta = input_txt.value
        if not pregunta:
            return

        input_txt.value = ""
        with chat_container:
            ui.chat_message(pregunta, sent=True)
            spin = ui.spinner(size="md")

        # Ejecución asíncrona para no bloquear la UI
        response = await run.io_bound(agent.consultar, pregunta)

        chat_container.remove(spin)
        with chat_container:
            ui.chat_message(str(response), name="Copiloto", bg_color="indigo-1")

        # Auto-scroll al final
        chat_container.run_method("scrollTo", 0, 10000)

    btn_enviar.on_click(enviar)
    input_txt.on("keydown.enter", enviar)


# Iniciamos el watcher al arrancar la app
ui.on_startup(start_watcher)
ui.run(title="ERP Copilot", port=8080)
