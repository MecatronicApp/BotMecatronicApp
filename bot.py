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
    "Cuales son las fechas limites para dar de baja una clase": "Estas fechas se publican en el cronograma académico: https://www.ecci.edu.co/cronograma-academico/",
    "Donde realizar la evaluación de profesores": "Entra al SIA y busca la sección 'Evaluación docente'. Es obligatoria para ver notas finales.",
    "Como descargar el recibo de la matricula": "Desde el SIA, selecciona 'Finanzas' y luego 'Recibo de matrícula'.",
    "Precuniarios": "Consulta información sobre los cursos precuniarios aquí: https://www.ecci.edu.co/precuniarios/",
    "Correos importantes": "Puedes ver una lista de correos de contacto aquí: https://www.ecci.edu.co/contacto/",
    "Aulas Virtuales": "Accede a las aulas virtuales desde https://aulasvirtuales.ecci.edu.co/",
    "Ubicacion de las sedes": "Consulta la ubicación de las sedes aquí: https://www.ecci.edu.co/nuestras-sedes/",
    "Curso de Inglés": "Los cursos se inscriben al inicio del semestre en el SIA, en la sección de Idiomas.",
    "Examen de Inglés": "Puedes presentar el examen de clasificación o validación. Consulta fechas en el aula virtual de idiomas."
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
