from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
import sys

# Respuestas frecuentes
FAQ = {
    "Links de Practicas Libres": "https://docs.google.com/forms/d/e/1FAIpQLSeDIdpoZFaWkOJAZNzz4uuVCC1TX5LbRSSwhPbhY3xdWH6e-w/viewform",
    "Fechas importantes": "https://www.ecci.edu.co/cronograma-academico/",
    "Otra duda": "Por favor consulta con el coordinador o envía un correo a info@mechatronica.edu",
    "Como ver las calificaciones del corte": "Debes ingresar al sistema académico SIA y dirigirte a la sección de 'Notas'.",
    "Cuales son las fechas limites para dar de baja una clase": "La fecha límite para dar de baja una clase sin beneficio económico es hasta la segunda semana del semestre.",
    "Donde realizar la evaluación de profesores": "La ruta para la evaluación de docentes es: Evaluaciones institucionales → Evaluación estudiante ECCI.",
    "Como descargar el recibo de la matricula": "La ruta para descargar el recibo de matrícula es: Cuenta financiera → Resumen facturas alumno → Seleccione el recibo → Generar recibo de pago.",
    "Precuniarios": "https://www.ecci.edu.co/derechos-pecuniarios/",
    "Correos importantes": "financiera@ecci.edu.co\nevaluame@ecci.edu.co\nasistente.mecatronicabta@ecci.edu.co",
    "Aulas Virtuales": "https://aulas.ecci.edu.co",
    "Ubicacion de las sedes": "https://www.ecci.edu.co/bogota/directorio-de-sedes/?sede=5/&fbclid=PAQ0xDSwKaPJVleHRuA2FlbQIxMAABp_my-CWb9QEGzYTNg3t3rwf76Rsu7vjQv5-6yBHRFpVTkSRzEfAhwhWk9Z12_aem_ShAq23B8IJ4qHJXDi4UggA",
    "Curso de Inglés": "https://arca.ecci.edu.co/psc/arca_1/EMPLOYEE/SA/c/EC_FORM_MN.LC_CRL_FORMULARIO.GBL?&",
    "Examen de Inglés": "https://centrodelenguas.ecci.edu.co/examenes/"
}

# Teclado principal (sin "Horario general")
menu_opciones = [
    ["Links de Practicas Libres", "Fechas importantes"],
    ["Como ver las calificaciones del corte", "Cuales son las fechas limites para dar de baja una clase"],
    ["Donde realizar la evaluación de profesores", "Como descargar el recibo de la matricula"],
    ["Precuniarios", "Correos importantes"],
    ["Aulas Virtuales", "Ubicacion de las sedes"],
    ["Cursos y Exámenes de Ingles"],
    ["Otra duda"]
]
teclado_principal = ReplyKeyboardMarkup(menu_opciones, one_time_keyboard=True, resize_keyboard=True)

# Submenú para inglés
teclado_ingles = ReplyKeyboardMarkup(
    [["Curso de Inglés"], ["Examen de Inglés"]],
    one_time_keyboard=True,
    resize_keyboard=True
)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy el Asistente Mecatrónico 🤖\nSelecciona una opción o escribe tu pregunta.",
        reply_markup=teclado_principal
    )

# mensajes
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    if texto == "Cursos y Exámenes de Ingles":
        await update.message.reply_text("¿Te interesa información sobre el *Curso* o el *Examen* de inglés?", reply_markup=teclado_ingles)
    elif texto in FAQ:
        await update.message.reply_text(FAQ[texto])
    else:
        await update.message.reply_text("No entiendo tu mensaje 😅. Elige una opción del menú o escribe /start para comenzar.")

# EJECUTAR
def main():
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app = Application.builder().token("7521983171:AAFykiXcgVA1UBjT8B6ghtnQz_FvWyN_lQM").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot en marcha...")
    app.run_polling()

if __name__ == '__main__':
    main()
