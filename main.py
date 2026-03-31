from nicegui import app, ui, run
from agent import ErpAgent
from watcher import iniciar_vigilancia
import threading
from fastapi import Request

# Inicializamos el agente
agent = ErpAgent()


def start_watcher():
    print("📢 Iniciando hilo del Watcher...")
    t = threading.Thread(target=iniciar_vigilancia, daemon=True)
    t.start()


# Añadiendo este endpoint  para crear el chat dentro del erpnext
@app.post("/consultar")
async def api_consultar(request: Request):
    data = await request.json()
    pregunta = data.get("pregunta")
    # Usamos tu clase ErpAgent para obtener la respuesta
    # Nota: Asegúrate de que el agente esté inicializado en modo "usuario"
    respuesta = agent.consultar(pregunta)
    return {"respuesta": str(respuesta)}


@ui.page("/")
def main_page():
    ui.label("ERPNext Copilot Enterprise").classes("text-2xl font-bold p-4")

    # Contenedor del chat
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

        # 1. Mostrar mensaje del usuario
        with chat_container:
            ui.chat_message(pregunta, sent=True)
            # Creamos un contenedor para el "Pensando..."
            thinking_indicator = ui.column()
            with thinking_indicator:
                ui.spinner(size="md")
                ui.label("Consultando ERPNext...").classes("text-xs italic")

        try:
            # 2. Consultar al agente
            # Usamos str(response) porque chat_engine devuelve un objeto Response
            response = await run.io_bound(agent.consultar, pregunta)

            # 3. Quitar el indicador de carga (sin usar .children)
            thinking_indicator.delete()

            # 4. Mostrar respuesta con clases de CSS en lugar de argumentos de fondo
            with chat_container:
                ui.chat_message(str(response), name="Copiloto").classes(
                    "bg-indigo-100 p-2 rounded-lg"
                )

        except Exception as e:
            print(f"Error en envío: {e}")
            try:
                thinking_indicator.delete()
            except:
                pass
            ui.notify(f"Error de conexión: {e}", type="negative")

        # Scroll al final
        chat_container.run_method("scrollTo", 0, 10000)

    btn_enviar.on_click(enviar)
    input_txt.on("keydown.enter", enviar)


# Registro del inicio
app.on_startup(start_watcher)

ui.run(title="ERP Copilot", port=8080)
